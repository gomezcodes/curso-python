class Persona():
    def __init__(self,nombre,edad,lugarResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = lugarResidencia

    def descripcion(self):
        print(f"Nombre: {self.nombre} , Edad: {self.edad} , Residencia: {self.lugarResidencia}")

class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombreEmpleado,edadEmpleado,residenciaEmpleado):
        super().__init__(nombreEmpleado,edadEmpleado,residenciaEmpleado)
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario}, Antiguedad: {self.antiguedad}")

Gisela = Persona("Gisela",25,"Puebla")
Gisela.descripcion()
print(isinstance(Gisela, Empleado))

Posmo = Empleado(1500,15,"Posmo",6,"Casita")
Posmo.descripcion()
print(isinstance(Posmo, Persona))