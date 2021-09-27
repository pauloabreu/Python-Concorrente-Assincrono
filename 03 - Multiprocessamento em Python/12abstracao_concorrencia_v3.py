import multiprocessing
import time

#from concurrent.futures.thread import ThreadPoolExecutor as Executer
from concurrent.futures.process import ProcessPoolExecutor as Executer


def processar():
    print('[', end='', flush=True)

    for _ in range(1, 11):
        print('#', end="", flush=True)
        time.sleep(1)

    print(']', end='', flush=True)


if __name__ == "__main__":
    with Executer() as executer:
        future = executer.submit(processar)
