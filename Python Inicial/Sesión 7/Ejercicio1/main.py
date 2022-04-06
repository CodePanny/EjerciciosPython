import operaciones as op  # AL poner el as le damos el nombre que queramos para este módulo


def main():
    num1 = 5
    num2 = 3
    num3 = 12
    num4 = 2
    num5 = 15

    suma = op.suma(num1, num2)
    resta = op.resta(num3, num4)
    mult = op.multiplicar(num1, num2)
    divide = op.dividir(num5, num2)

    print("El resultado de la suma de", num1, "+", num2, "es", suma)
    print("El resultado de la resta de", num3, "-", num4, "es", resta)
    print("El resultado de la multiplicación de", num1, "por", num2, "es", mult)
    print("El resultado de la división de", num5, "entre", num2, "es", divide)


if __name__ == '__main__':
    main()
