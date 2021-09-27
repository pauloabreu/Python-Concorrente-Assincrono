import multiprocessing

"""
Prof of Concept: Resolvendo o Race Conditions
"""

def depositar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value + 1


def sacar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value - 1


def realizar_transacao(saldo, lock):
    pc1 = multiprocessing.Process(target=depositar, args=(saldo, lock))
    pc2 = multiprocessing.Process(target=sacar, args=(saldo, lock))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


if __name__ == "__main__":
    saldo = multiprocessing.Value("i", 100)
    print(f"Saldo Inicial: {saldo.value}")

    lock = multiprocessing.RLock()

    for _ in range(10):
        realizar_transacao(saldo, lock)

    print(f'Saldo final: {saldo.value}')


"""
Saldo Inicial: 100
Saldo final: 100
"""