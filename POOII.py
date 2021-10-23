class Coche():

    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4 #variable  encapsulada
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        if (self.__enmarcha):
            chequeo=self.__chequeoInterno()

        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha salido mal durante el chequeo"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene {} ruedas. Un ancho de {} y un largo de {} \n".format(self.__ruedas,self.__anchoChasis,self.__largoChasis))
    
    def __chequeoInterno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False


jetta = Coche()
print(jetta.arrancar(True))
jetta.estado()

print("----------------------A continuacion creamos el segundo objeto------------------------\n")

vochito = Coche()
print(vochito.arrancar(False))
vochito.estado()



