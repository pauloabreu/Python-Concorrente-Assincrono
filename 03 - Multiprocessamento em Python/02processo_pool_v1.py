import multiprocessing


def calcular(dado):
    return dado ** 2


def main():
    tamanho_pool = multiprocessing.cpu_count() * 2 # 4 * 2 -> 8

    print(f'Tamanho da Pool {tamanho_pool}')
    
    pool = multiprocessing.Pool(processes=tamanho_pool)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'Saídas: {saidas}')

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()

"""
Tamanho da Pool 8
Saídas: [0, 1, 4, 9, 16, 25, 36]
"""