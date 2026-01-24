propertys = ["casa nro1", "casa nro2", "casa nro3","casa nro4"]
address_propertys = ("calle1", "calle2", "calle3","calle4")
countpropertys = len(propertys)

propertys_v2 = {
    "propiedades": [
        {   
            "id":1,
            "nombre": "casa blanca",
            "direccion": ("av siempre viva", "lima"),
            "precio": 352100,
            "moneda": "USD",
            "disponible": False,
            "personas": []
        },
        {   
            "id":2,
            "nombre": "casa roja",
            "direccion": ("av los girasoles", "cusco"),
            "precio": 250000,
            "moneda": "USD",
            "disponible": True,
            "personas": []
        },
        {   
            "id":3,
            "nombre": "casa rosada",
            "direccion": ("av siempre felicidad", "lima"),
            "precio": 352345,
            "moneda": "USD",
            "disponible": True,
            "personas": []
        }
    ]
}

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
    print(propertys_v2["propiedades"])
elif opcion == 2:
    print(len(propertys_v2["propiedades"])) 
elif opcion == 3:
    primera = propertys[0]
    ultima = propertys[-1]
    print(primera, address_propertys[0], ultima, address_propertys[3])
elif opcion == 4:
    #new_property = input("Ingrese la nueva propiedad: ")
    #propertys.append(new_property)
    #print(propertys)
    id_new = len(propertys_v2["propiedades"]) + 1
    new_property= {}
    new_property["id"] = id_new
    name = input("Ingrese el nombre: ")
    new_property["nombre"] = name
    address1 = input("Ingrese su direccion 1: ")
    address2 = input("Ingrese su direccion 2: ")
    new_property["direccion"] = (address1, address2)
    new_property["precio"] = float(input("Ingrese el precio: "))
    propertys_v2["propiedades"].append(new_property)
    print(propertys_v2["propiedades"])
else:
    print("ingrese una opcion correcta")

#Base de datos

