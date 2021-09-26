import threading
import time

def main():
    threads = [
        threading.Thread(target=contar, args=("elefante", 10)), #2
        threading.Thread(target=contar, args=("buraco", 8)),
        threading.Thread(target=contar, args=("moeda", 23)),
        threading.Thread(target=contar, args=("pato", 12))
    ]
    
    [th.start() for th in threads] #Adiciona as Threads a pool de threads prontas pra execução
    
    print("Fazendo outras coisas..")
    
    [th.join() for th in threads] #Avisa para ficar aguardando até a thread terminar

    print("Pronto")


def contar(objeto, numero):
    for n in range(1, numero+1):
        print(f"{n} {objeto}(s)..")
        time.sleep(1)


if __name__ == "__main__":
    main()

