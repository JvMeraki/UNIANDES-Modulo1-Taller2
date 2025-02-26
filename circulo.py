import math


def area_circulo(radio: float) -> float:
    area = math.pi * radio ** 2
    return round(area, 2)

# Se imprime el llamado a la función area_circulo con el radio X
# print(area_circulo(X))