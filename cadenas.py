nombreUsuario = input("Introduzca su nombre de usuario: ")

print("El nombre es {}".format(nombreUsuario.upper()))
print("El nombre es {}".format(nombreUsuario.lower()))
print("El nombre es {}".format(nombreUsuario.capitalize()))

edad = input("Introduce la edad: ")

while(edad.isdigit() == False):
    print("Por favor, introduce un valor numerico")
    edad = input("Introduce la edad: ")    

if (int(edad)<18):
    print("No puede pasar")
else:
    print("Puede pasar")