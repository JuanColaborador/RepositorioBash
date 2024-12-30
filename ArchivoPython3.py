"""***************************************************************
Parte 2: Estructura de un Programa Python y Funciones 

1. Organización del Código en Python :
    Indentación y su importancia en la sintaxis de Python.
    Comentarios y documentación del código. # Comentario en una sola lina o 3 comillas(")
    Concepto de módulos e importación (import).
2. Funciones :
    Definición y uso de funciones (def).
    Parámetros y argumentos.
    Retorno de valores (return).
    Ámbito de las variables (local y global).
    Ejemplos prácticos de creación y uso de funciones.
***********************************************************"""

# Indentación y su importancia en la sintaxis de Python.
def saludo(nombre):
    if nombre:  # Si el nombre no está vacío
        print("Hola, " + nombre + "!")
    else:
        print("Hola, invitado!")

saludo("Ana")  # Imprime "Hola, Ana!"
saludo("")     # Imprime "Hola, invitado!"

# Incorrecto. No tiene indentació el if
"""
def saludo(nombre):
if nombre: #Error aqui falta la indentacion
print("Hola, " + nombre + "!") #Error aqui falta la indentacion
else:
print("Hola, invitado!") #Error aqui falta la indentacion
"""

#Comentarios y Documentación

# Este es un comentario de una línea.
x = 10  # Asignamos el valor 10 a la variable x.

"""
Comentarios de varias líneas (docstrings): Se delimitan con tres comillas simples (') o dobles ("). 
            Se utilizan para documentar funciones, clases, módulos o el script en general.
"""                                                                                   
def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio.

    Args:
        radio: El radio del círculo (debe ser un número positivo).

    Returns:
        El área del círculo.

    Raises:
        TypeError: Si el radio no es un número.
        ValueError: Si el radio es negativo.
    """
    if not isinstance(radio, (int, float)):
        raise TypeError("El radio debe ser un número.")
    if radio < 0:
        raise ValueError("El radio debe ser positivo.")
    return 3.14159 * radio ** 2

print(calcular_area_circulo.__doc__) #imprime la documentacion de la funcion
print(calcular_area_circulo(2))

# Módulos e Importación (import)
import ArchivoPython3_mi_modulo #importa todo el modulo
from ArchivoPython3_mi_modulo import saludar #importa solo la funcion saludar
from ArchivoPython3_mi_modulo import PI #importa solo la constante PI
from ArchivoPython3_mi_modulo import * #importa todo el contenido del modulo (no recomendado)
import ArchivoPython3_mi_modulo as mm #importa el modulo con un alias

ArchivoPython3_mi_modulo.saludar("Carlos") #utilizando la importacion por modulo
saludar("Maria") #utilizando la importacion por funcion
print(PI) #utilizando la importacion por constante
mm.saludar("Pedro") #utilizando la importacion por alias

