# para comentarios de una sola línea usar #
# Para comentarios de varias líneas usar 3 comillas dobles ( " )

"""***********************************************
1. Variables y Tipos de Datos Básicos
************************************************"""

"""
 Variables: En Python, las variables se crean al asignarles un valor. 
            No necesitas declarar el tipo de dato explícitamente.
"""

nombre = "Juan"  # Cadena (string)
edad = 30       # Entero (integer)
altura = 1.75   # Flotante (float)
es_estudiante = True  # Booleano (boolean)

# usando f-string
print(f"La variable nombre es de tipo: {type(nombre)}")
print(f"La variable edad es de tipo: {type(edad)}")
print(f"La variable altura es de tipo: {type(altura)}")
print(f"La variable es_estudiante es de tipo: {type(es_estudiante)}")

# Si solo necesitas el nombre del tipo como una cadena
print(f"El tipo de nombre es: {type(nombre).__name__}")
print(f"El tipo de edad es: {type(edad).__name__}")
print(f"El tipo de altura es: {type(altura).__name__}")
print(f"El tipo de es_estudiante es: {type(es_estudiante).__name__}")

print("Agregado por colaborador")
