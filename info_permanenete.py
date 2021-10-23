import pickle

class Persona():
    def __init__(self,nombre,genero,edad) -> None:
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f"Se ha creado una persona nueva con el nombre de {nombre}")

    def __str__(self) -> str:
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas():

    personas = []
    def __init__(self) -> None:
        listaDePersonas = open("ficheroExterno","ab+")
        listaDePersonas.seek(0)
        
        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    def guardarPersonasEnFicheroExterno(self):
        ListaPersonas = open("ficheroExterno","wb")
        pickle.dump(self.personas,ListaPersonas)
        ListaPersonas.close()
        del(ListaPersonas)

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()
persona = Persona("posmo","perrito",5)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()