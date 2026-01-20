propertys = ["casa nro1", "casa nro2", "casa nro3","casa nro4"]

countpropertys = len(propertys)       

msg = """
    ==Bienvenido al SISTEMA INDATUX ==
    1. Mostrar propiedades
    2. Ver cantidad de propiedades
    3. Ver primera y ultima propiedad
    4. Agregar propiedad
    5. Salir
"""
print(msg)

opcion = int(input("ingrese la opcion a realizar: "))

if opcion == 1:
    print(propertys)
elif opcion == 2:
    print(len(propertys))
elif opcion == 3:
    primera = propertys[0]
    ultima = propertys[-1]
    print(primera, ultima)
elif opcion == 4:
    new_property = input("Ingrese la nueva propiedad: ")
    property.append(new_property)
else:
    print("ingrese una opcion correcta")