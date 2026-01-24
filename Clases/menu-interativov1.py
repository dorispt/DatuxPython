
msg = """
    Bievenido a SISTEMA-DATUX-IN
    1. Login
    2. Salir
"""

usuarios =[
    {
        'id':1,
        'name': 'Ana',
        'lastName': 'Torres',
        'perfil': 'Administrador',
        'email': 'ana.torres@sistema.com',
        'password': 'Admin123',
        'status': True
    }
]

def MenuInteractivoUserLogueado():
    msgv2= """
        1. Crear producto
        2. Listar producto
        3. Evaluar clientes
        4. Salir
    """

    logueado = True
    while logueado:
        print(msgv2)
        opcionv2 = int(input("Ingrese una opción: "))
        if opcionv2 == 1:
            pass
        elif opcionv2 == 2:
            pass
        elif opcionv2 == 3:
            pass
        elif opcionv2 == 4:
            logueado = False
        else:
            print("Ingrese una opción válida")


def buscarUsuario(email):
    for i in usuarios:
        if email == i['email']:
            return i
    return False



def login():
    #usuario y password
    #Comparar en una "Base de Datos"
    email= input("ingrese su email: ")
    usuario=buscarUsuario(email)
    if type(usuario) == dict:
        if usuario.get('status'):
            password = input("ingrese su password: ")
            if password ==usuario["password"]:
                print(f"LOGIN CORRECTO {usuario["name"]} ")
                return usuario
            else:
                print("error de password")
        else:
            print("usuario no activo")
    else:
        print("usuario no encontrado")

#manejar variable global para el usuario
#logica para que si el usuario no se loguea no entre a a proxima vista


n=1
while True:
    print(msg)
    opcion = int(input("Ingrese una opción: "))
    # se puede usar match case o if
    if opcion == 1:
        usuarioLogueado = login()
        MenuInteractivoUserLogueado()
    elif opcion ==2:
        usuarioLogueado = False
        print("saliendo del sistema...")
        break
    else:
        print("ingrese una opción válida: ")
    
#Aplicando divide y venceras 

