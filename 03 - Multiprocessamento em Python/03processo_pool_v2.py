import multiprocessing


def calcular(dado):
    return dado ** 2


def imprimir_nome_processo():
    print(f'Iniciado o processo com nome: {multiprocessing.current_process().name}')


def main():
    tamanho_pool = multiprocessing.cpu_count() * 2 # 4 * 2 -> 8

    print(f'Tamanho da Pool {tamanho_pool}')
    
    pool = multiprocessing.Pool(processes=tamanho_pool, initializer=imprimir_nome_processo)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'Saídas: {saidas}')

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()


"""
Tamanho da Pool 8
Iniciado o processo com nome: SpawnPoolWorker-2
Saídas: [0, 1, 4, 9, 16, 25, 36]
Iniciado o processo com nome: SpawnPoolWorker-1
Iniciado o processo com nome: SpawnPoolWorker-5
Iniciado o processo com nome: SpawnPoolWorker-6
Iniciado o processo com nome: SpawnPoolWorker-3
Iniciado o processo com nome: SpawnPoolWorker-7
Iniciado o processo com nome: SpawnPoolWorker-4
Iniciado o processo com nome: SpawnPoolWorker-8
"""