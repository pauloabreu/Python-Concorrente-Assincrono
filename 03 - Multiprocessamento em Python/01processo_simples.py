import multiprocessing

print(f'Iniciado o processo com nome: {multiprocessing.current_process().name}')

def faz_algo(valor):
    print(f'Fazendo algo com o valor {valor}')

def main():
    pc = multiprocessing.Process(target=faz_algo, args=('Pássaro',), name="Processo Teste")

    print(f'Iniciado o processo com nome: {pc.name}')

    pc.start()
    pc.join()


if __name__ == "__main__":
    main()