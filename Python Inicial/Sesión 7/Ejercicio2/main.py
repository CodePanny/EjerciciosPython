import time

H = time.strftime('%H')
M = time.strftime('%M')
S = time.strftime('%S')

if int(H) >= 19:
    print("Go home bro")

else:
    print("Aún toca trabajar, quedan {} horas, {} minutos y {} segundos para terminar".format(18 - int(H), 59 - int(M), 59 - int(S)))
