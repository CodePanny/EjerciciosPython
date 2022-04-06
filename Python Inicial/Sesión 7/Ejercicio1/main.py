import operaciones as op #AL poner el as le damos el nombre que queramos para este módulo

def main():

    suma = op.suma(5, 3)
    resta = op.resta(12, 2)
    mult = op.multiplicar(5, 3)
    divide = op.dividir(15, 3)

    print("El resultado de la suma es", suma)
    print("El resultado de la resta es", resta)
    print("El resultado de la multiplicación es", mult)
    print("El resultado de la división es", divide)

if __name__ == '__main__':
    main()
