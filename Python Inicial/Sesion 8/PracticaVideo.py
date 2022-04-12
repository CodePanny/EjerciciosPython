def main():

    texto = textobien()
    for datos in texto:
        print(f"Texto: {datos}")


def textobien():

    f = open("C:/Users/panny/OneDrive/Desktop/ejercicio.txt", 'r')
    datos = f.readlines()
    f.close()

    resultado = []

    for linea in datos:
        if linea[0] == '\n':
            continue

        if linea[0] == '}':
            continue

        partes = linea.split(' ')

        resultado.append(partes[0])

    return resultado


if __name__ == '__main__':
    main()
