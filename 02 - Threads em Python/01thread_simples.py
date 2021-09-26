import threading
import time

def main():
    th = threading.Thread(target=contar, args=("elefante", 10))
    
    th.start() #Adiciona a Thread a pool de threads prontas pra execução
    
    print("Fazendo outras coisas..")
    
    th.join() #Avisa para ficar aguardando até a thread terminar

    print("Pronto")


def contar(objeto, numero):
    for n in range(1, numero+1):
        print(f"{n} {objeto}(s)..")
        time.sleep(1)


if __name__ == "__main__":
    main()

"""
1 elefante(s)..
Fazendo outras coisas..
2 elefante(s)..
3 elefante(s)..
4 elefante(s)..
5 elefante(s)..
6 elefante(s)..
7 elefante(s)..
8 elefante(s)..
9 elefante(s)..
10 elefante(s)..
Pronto
"""