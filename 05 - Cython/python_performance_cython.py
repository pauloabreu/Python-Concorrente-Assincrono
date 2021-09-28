import datetime
import computa


def main():
    inicio = datetime.datetime.now()

    computa.computar(fim=20_000_000)

    tempo = datetime.datetime.now() - inicio

    print(f"Terminiou em {tempo.total_seconds():.2f} segundos..")


if __name__ == "__main__":
    main()


"""
Terminiou em 0.00 segundos..
"""