# Se importa el modulo que contiene las funciones a utilizar
import modulo


def main(lado: float) -> float:
    return modulo.area_sombreada(lado) # Se retorna el valor de la función area_sombreada del módulo 'modulo' con el valor del 'lado' del cuadrado como parámetro

# Se valida que el valor ingresado sea un número mayor a 0, se repite siempre que no se cumpla la condición
while True:
        try: 
            lado = float(input("Digite el valor del lado del cuadrado: ")) # Se solicita el valor del lado del cuadrado
            if lado > 0:
                print(f"El área sombreada es: {main(lado)}")
                break # Se rompe el ciclo si el valor ingresado es válido
            else:
                print("El valor ingresado debe ser mayor a 0. Ingrese un valor válido") # Se imprime un mensaje de error si el valor ingresado no es mayor a 0  
        except ValueError:
            print("El valor ingresado no es válido") # Se imprime un mensaje de error si el valor ingresado no es un número