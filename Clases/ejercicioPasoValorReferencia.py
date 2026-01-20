lista = [11,2,49,4]
a=10

def FxDemo(a,lista):
    a=a*2
    print(a)
    lista[-1]=2*lista[-1]
    print(a,lista)
FxDemo(a,lista)
print(a,lista)