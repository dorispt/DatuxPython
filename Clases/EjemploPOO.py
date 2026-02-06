class PropiedadInmobiliaria:
    dimensionV2 = float
    precioPropiedad = float

    def __init__(self,name,addreess,dimensiones: str,withSize:float,heightSize:float,precioUnit:float):
        #este es el constructor
        self.name = name
        self.addreess = addreess
        self.dimensiones = dimensiones # "7*4"
        self.withSize = withSize
        self.heightSize = heightSize
        self.precioUnit = precioUnit
        self.calculateDimensionV2()

    def getWidth(self):
        withPropiedad = self.dimensiones.split("*")[0]
        return int(withPropiedad)
    def getHeight(self):
        heightPropiedad = self.dimensiones.split("*")[1]
        return int(heightPropiedad)
    def calculateDimensionV1(self):
        size = self.dimensiones.split("*")
        dimension = float(size[0]) * float(size[1])
        return dimension
    def calculateDimensionV2(self):
        self.dimensionV2 = self.withSize * self.heightSize
    def calculatePriceAprox(self): 
        self.precioPropiedad = self.precioUnit * self.dimensionV2
        return self.precioPropiedad
    def comprar(self):
        self.enable = False
    def __str__(self):
        disponibilidad:str
        if self.enable:
            disponibilidad = "Disponible"
        else:
            disponibilidad = "No Disponible"
        #operador ternario
        disponibilidadV2 = "Disponible" if self.enable else "No esta disponible"

        return f"Propiedad: {self.name}, Direccion: {self.addreess}, Dimensiones: {self.dimensiones}, Precio Unitario: S/ {self.precioUnit}, DimensionV2: {self.dimensionV2}, Precio Aproximado: S/ {self.precioPropiedad}"


pr1 = PropiedadInmobiliaria("pr_1","Av. Siempre Viva 123","7*4",7,4,1200)      
pr2 = PropiedadInmobiliaria("pr_2","Calle Falsa 456","10*5",10,5,1000)
pr3 = PropiedadInmobiliaria("pr_3","Boulevard Central 789","8*6",8,6,1500)
pr4 = PropiedadInmobiliaria("pr_4","Avenida Libertad 321","12*7",12,7,900)
pr5 = PropiedadInmobiliaria("pr_5","Calle Luna 654","9*5",9,5,1100)

lista_propiedades = [pr1,pr2,pr3,pr4,pr5]

#me quede aqui
class Inmobiliario:
    def __init__(self,listaPropiedades:list[PropiedadInmobiliaria]):
        
        self.nombreInmobiliaria = nombreInmobiliaria
        self.direccionInmobiliaria = direccionInmobiliaria
        self.listaPropiedades = listaPropiedades