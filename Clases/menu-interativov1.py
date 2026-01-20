
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
        'perfil': 'Adminitrador',
        'email': 'ana.torres@sistema.com',
        'password': 'Admin123',
        'status': True
    }
]

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
            password = input("inrese su password: ")
            if password ==usuario["password"]:
                print(f"LOGIN CORRECTO {USUARIO} ")

           
    else:
        print("usuario no encontrado")

 
n=1
while True:
    print(msg)
    opcion = int(input("Ingrese una opción: "))
    # se puede usar match case o if
    if opcion == 1:
        pass
       # usuarioLogueado =
    elif opcion ==2:
        pass
    else:
        print("ingrese una opción válida: ")
    
#Aplicando divide

