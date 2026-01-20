#Realice un programa que muestre si una persona tiene linea de crédito.

msg="""
    Hola Bienvenido a Datux Banca
    1. Para realizar un proceso de evaluación ingrese los siguientes valores:
    - DNI
    - Edad
    - Nombre completo
    - salario
"""

print (msg)
dni = input ("Ingrese su el valor de su DNI: ")
edad = int(input ("Ingrese el valor de su edad: "))
nombre = input ("Ingrese el valor de su nombre completo: ")
salario = float(input ("Ingrese el valor de su salario: "))

aprobeCredit = edad>18 and salario >= 1500
print (f"Estimado {nombre} con DNI: {dni} su crédito esta: {aprobeCredit}")