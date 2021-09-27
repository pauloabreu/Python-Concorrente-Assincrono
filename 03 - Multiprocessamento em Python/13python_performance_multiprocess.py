import datetime
import math

import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor


def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizando o processamento matemático com {qtd_cores} core(s).')


    inicio = datetime.datetime.now()

    with ProcessPoolExecutor() as executor:
        for n in range(1, qtd_cores+1):
            ini = 20_000_000 * (n - 1) / qtd_cores
            fim = 20_000_000 * n / qtd_cores
            print(f'Core {n} processando de {ini} até {fim}')
            executor.submit(computar, {'inicio': ini, 'fim': fim})


    tempo = datetime.datetime.now() - inicio

    print(f"Terminiou em {tempo.total_seconds():.2f} segundos..")


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos-fator) * (pos-fator))


if __name__ == "__main__":
    main()


"""
Terminiou em 0.20 segundos..
"""