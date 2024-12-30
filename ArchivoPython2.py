#3. Estructuras de Control

"""
Condicionales (if, elif, else): Permiten ejecutar diferentes bloques de código según se cumplan 
        o no ciertas condiciones.
Python
"""
print("")
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres menor de edad.")

print("")

"""
Bucles (for, while): Permiten repetir un bloque de código múltiples veces.
"""

# for: Itera sobre una secuencia (como una lista, cadena o rango).
print("")
print("for: Itera sobre una secuencia (como una lista, cadena o rango).")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

print("")
print("for: Itera sobre una secuencia rango.")
for i in range(5): #recorre del 0 al 4
    print(i)

#while: Repite un bloque de código mientras se cumpla una condición.
print("")
print("while: Repite un bloque de código mientras se cumpla una condición.")

contador = 0
while contador < 5:
    print(contador)
    contador += 1 #equivale a contador = contador + 1