import queue
import time
import colorama

from threading import Thread
from queue import Queue


def gerador_de_dados(queue):
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f'Dados {i} Gerado.', flush=True)
        time.sleep(2)
        queue.put(i)


def consumidor_de_dados(queue):
    while queue.qsize() > 0:
        valor = queue.get()
        print(colorama.Fore.RED + f'Dado {valor * 2} Processado', flush=True)
        time.sleep(1)
        queue.task_done()


if __name__ == "__main__":
    print(colorama.Fore.WHITE + 'Sistema Inicidado', flush=True)
    
    queue = Queue()

    th1 = Thread(target=gerador_de_dados, args=(queue,))
    th2 = Thread(target=consumidor_de_dados, args=(queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()


"""
Nesse caso a Th2 depende dos dados gerados pela Th1


Sistema Inicidado
Dados 1 Gerado.
Dados 2 Gerado.
Dados 3 Gerado.
Dados 4 Gerado.
Dados 5 Gerado.
Dados 6 Gerado.
Dados 7 Gerado.
Dados 8 Gerado.
Dados 9 Gerado.
Dados 10 Gerado.
Dado 2 Processado
Dado 4 Processado
Dado 6 Processado
Dado 8 Processado
Dado 10 Processado
Dado 12 Processado
Dado 14 Processado
Dado 16 Processado
Dado 18 Processado
Dado 20 Processado
"""