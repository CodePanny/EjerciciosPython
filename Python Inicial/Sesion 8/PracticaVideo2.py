def main():

    f = open('fichero.txt', 'w')

    lista = [
    "a 1\n",
    "Linea 2\n",
    "Linea 3\n"
    ]

    def escribe(fichero, datos):
        f = open(fichero, 'w')

        for linea in datos:
            if not linea.endswith('\n'):
                linea = linea + '\n'  # linea =+ '\n'

            f.write(linea)

        f.close()

    escribe("fichero.txt", lista)

if __name__ == "__main__":
    main()
