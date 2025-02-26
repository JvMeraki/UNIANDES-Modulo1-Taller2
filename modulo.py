#se importa el modulo circulo
import circulo


# función para calcular el área de un cuadrado, recibe el lado y retorna el área
def area_cuadrado(lado: float) -> float:
    area = lado ** 2
    return round(area, 2)

# función para calcular el área sombreada, recibe el lado de un cuadrado y retorna el área sombreada, restandole el area de la circunferencia interna
def area_sombreada(lado: float) -> float:
    radio = lado / 2
    area_circulo = circulo.area_circulo(radio)
    return round(area_cuadrado(lado) - area_circulo, 2)

# Se imprime el llamado a la función area_sombreada con el lado X
# print(area_sombreada(X))