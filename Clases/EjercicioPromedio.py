#notas
dni = input("Ingrese su DNI: ")
fullname = input("Ingrese su nombre completo: ")
nota1 = float(input("Ingrese su nota de practica nro 1: "))
nota2 = float(input("Ingrese su nota de practica nro 2: "))
nota3 = float(input("Ingrese su nota de practica nro 3: ")) 
nota4 = float(input("Ingrese su nota de practica nro 4: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

if promedio >= 11:
    print(f"aprobaste {fullname}")
else:
    print(f"desaprobaste {fullname}")