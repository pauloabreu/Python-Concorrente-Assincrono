import datetime
import math
import asyncio


def main():
    print('Realizando o processamento matemático de forma assícrona.')

    el = asyncio.get_event_loop()

    inicio = datetime.datetime.now()

    #el.run_until_complete(computar(inicio=1, fim=20_000_000))

    tarefa1 = el.create_task(computar(inicio=1, fim=5_000_000))
    tarefa2 = el.create_task(computar(inicio=5_000_000, fim=10_000_000))
    tarefa3 = el.create_task(computar(inicio=10_000_000, fim=20_000_000))

    tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3)
    el.run_until_complete(tarefas)

    tempo = datetime.datetime.now() - inicio

    print(f'Terminou em {tempo.total_seconds():.2f} segundos')


async def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == "__main__":
    main()

"""
Terminou em 9.62 segundos
"""