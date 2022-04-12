def main():

    f = open('fichero.txt', 'w')

    lista = [
    "Entrada de datos por lista 1\n",
    "Linea 2\n",
    "Linea 3\n"
    ]

    f.write("Entrada de datos 1\n")
    f.write("Entrada de datos 2\n")
    f.writelines(lista)
    f.close()


if __name__ == "__main__":
    main()
