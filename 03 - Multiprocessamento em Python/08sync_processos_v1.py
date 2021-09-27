import multiprocessing

"""
Prof of Concept: Race Conditions
"""

def depositar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value + 1


def sacar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value - 1


def realizar_transacao(saldo):
    pc1 = multiprocessing.Process(target=depositar, args=(saldo,))
    pc2 = multiprocessing.Process(target=sacar, args=(saldo,))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


if __name__ == "__main__":
    saldo = multiprocessing.Value("i", 100)
    print(f"Saldo Inicial: {saldo.value}")

    for _ in range(10):
        realizar_transacao(saldo)

    print(f'Saldo final: {saldo.value}')


"""
Saldo Inicial: 100
Saldo final: -7845
"""