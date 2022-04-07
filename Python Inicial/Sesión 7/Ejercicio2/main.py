import time

horaActual = time.strftime('%H:%M:%S')

H = time.strftime('%H')
M = time.strftime('%M')
S = time.strftime('%S')

cH = 18 - int(H)
cM = 59 - int(M)
cS = 59 - int(S)

trabaja = f"Aún toca trabajar, quedan {cH} horas, {cM} minutos y {cS} segundos para terminar"


print("Son las", horaActual)

if int(H) >= 19:
    print("Go home bro")

else:
    print(trabaja)
