# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista
# No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados
# alfabéticamente y separados por comas.

entrada = input("Introduce una lista de paises separados por coma:")
entradaK = entrada.replace(" ", "")     # Evitamos que nos detecte paises como diferentes en caso de haber espacios
entradaL = entradaK.split(",")          # Partimos la str por las comas y obtenemos una lista
entradaM = list(set(entradaL))          # Al hacer un set se borran por defecto todos los duplicados

print(sorted(entradaM))                 # Usamos sorted para ordenar alfabéticamente 
