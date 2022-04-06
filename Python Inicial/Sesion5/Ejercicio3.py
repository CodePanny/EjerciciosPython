
def bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("El año", year, "es bisiesto")

    else: 
        print("El año", year, "no es bisiesto")


bisiesto(2020)
bisiesto(2021)
bisiesto(2022)
bisiesto(2023)
bisiesto(2024)
bisiesto(2025)
bisiesto(2026)
