def funciones():
    pass
    """                 FUNCIONES           

    def suma(num1, num2):         #video 6, Curso python - pildorasinformaticas
        resultado=num1+num2
        return resultado
    print(suma(5,7))
    suma(2,3)

    """ 
def listas():
    pass
    """                 LISTAS              

    miLista = ["posmo","gissi",5, True, "joaquin", "mami", "suegris", 75.3]
    miLista.append("giselo")
    print(miLista[:])
    miLista.insert(2,"posma")
    print(miLista[:])
    miLista.extend(["carl","jake","sister"])
    print(miLista[:])
    print(miLista.index("giselo"))
    print("pepe" in miLista) 
    print("posma" in miLista)

    """
def tuplas():
    pass
    """                 TUPLAS                 

    mitupla=("posmo",13,14,1995,13) #Se declara entre parentesis
    milista=list(mitupla) #convierte tupla en lista
    print(milista)
    mitupla=tuple(milista) #convierte lista en tupla
    print(mitupla)
    print("posmo" in mitupla) #Busca su "posmo" esta en tupla, si -> True

    print(mitupla.count(13)) #cuantas veces se encuentra "13"

    print(len(mitupla)) #cuantos elementos hay en la tupla

    tuplaunitaria = ("gis",) #tupla unitaria
    print(len(tuplaunitaria))

    mitupla=("posmo",13,14,1995) #otra forma de declarar tuplas, que no se recomienda
    nombre,dia,mes,ano = mitupla #desempaquetado de tuplas
    print(nombre)
    print(mes)
    print(dia)
    print(ano)

    """
def diccionarios():
    pass
    """                 DICCIONARIOS            

    miDiccionario = {"Alemania":"Berlin"
                    ,"Francia":"Paris"
                    ,"Reino Unido":"Londres"
                    ,"España":"Madrid"} #Sintaxis de un diccionario

    miDiccionario["Italia"]="Lisboa" #Agregar un clave:valor
    print(miDiccionario)
    miDiccionario["Italia"]="Roma"  #Sobreescribe el valor
    print(miDiccionario)
    del miDiccionario["Reino Unido"] #Elimina la clave:valor
    print(miDiccionario)
    print("\n")

    miDiccionario_2 = {"alemania":"berlin",23:"jordan","mosqueteros":3} # Clave y Valor pueden ser numeros
    print(miDiccionario_2)
    print("\n")

    mitupla=["España","Francia","Reino Unido","Alemania"]
    miDiccionario_3 = {mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[2]:"Berlin"} #Diccionario con tupla
    print(miDiccionario_3)
    print(miDiccionario_3["Francia"])
    print("\n")

    miDiccionario_4 = {23:"Jordan","Nombre":"Gis","Equipo":"Chicago","Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}} # Temporadas es un diccionario dentro de otro diccionario, El valor de temporadas es una tupla
    print(miDiccionario_4)
    print(miDiccionario_4["Equipo"])
    print(miDiccionario_4["Anillos"])
    print("\n")

    print(miDiccionario_4.keys())
    print(miDiccionario_4.values())
    print(len(miDiccionario_4))
    print("\n")

    """
def condicionalesI():
    pass
    """                 CONDICIONALES I         

    print("Introduzca el valor de la nota")

    nota_alumno = int(input()) #<--- Acepta datos por consola :o

    def evaluacion(nota):
        valoracion="aprobado"
        if nota < 5:
            valoracion = "reprobado"
        return valoracion

    print(evaluacion(nota_alumno)) 

    """
def condicionalesII():
    pass
    """                 CONDICIONALES II         

    print("Verificavion de acceso")

    edadUsuario = int(input("Introduce tu edad: "))

    if 14 < edadUsuario < 18:
        print("No puedes pasar")
    elif edadUsuario > 100:
        print("Ya estas muerto mijo, nel")
    else:
        print("Puedes pasar")

    print("El programa ha finalizado")

    """
def condicionalesIII():
    pass
    """                 CONDICIONALES III         

    salarioPresidente = int(input("Introduce salario de presidente: "))
    print("Salario del presidente introducido: " + str(salarioPresidente))

    salarioDirector = int(input("Introduce salario de Director: "))
    print("Salario del Director introducido: " + str(salarioDirector))

    salarioJefeArea = int(input("Introduce salario de Jefe de Area: "))
    print("Salario del Jefe de Area introducido: " + str(salarioJefeArea))

    salarioAdministrativo = int(input("Introduce salario de Administrativo: "))
    print("Salario del Administrativo introducido: " + str(salarioAdministrativo))

    if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
        print("Todo funciona correctamente")
    else:
        print("Algo falla en la empresa mmmmm que raro ")

    """
def condicionalesIV():
    pass
    """                 CONDICIONALES IV         

    #print("Programa de BECAS")

    #distanciaEscuela = int(input("¿A que distancia vive del centro (km)?: "))
    #numeroHermanos = int(input("Introduce el numero de hermanos: "))
    #salarioFamiliar = int(input("Introduce el salario bruto: "))

    #if distanciaEscuela > 40 and numeroHermanos > 2 or salarioFamiliar <= 20000:
    #    print("Tienes derecho a beca")
    #else: 
    #    print("No tienes derecho a beca")

    print("Asignaturas optativas Año 2021 ")
    print("Asignaturas optativas: Informatica grafica - Prueba de software - Usabilidad y accesabilidad")
    asignatura = input("Escribe la asignatura escogida: ")
    asignatura = asignatura.lower()

    if asignatura in ("informatica grafica","prueba de software","usabilidad y accesibilidad"):
        print("Asignatura escogida " + asignatura)
    else:
        print("La asignatura escogida no esta contemplada")

    """
def buclesII():
    pass
    """                 BUCLES II         
    email = False
    contador = 0
    myEmail = input("Escriba su email: ")

    for i in myEmail:
        if i == "@" or i==".":
            contador += 1

    if contador == 2:
        print("Email es correcto")
    else:
        print("El email no es correcto")

    for i in range(5):
        print(i)

    """
def buclesIII():
    pass
    """                 BUCLES III         

    for i in range(5,50,10):
        print(f"valor de la variable {i}")
    print("\n")

    valido = False
    email = input("introduce el email: ")

    for i in range(len(email)):
        if email[i] == "@":
            valido = True

    if valido:
        print("Email correcto")
    else:
        print("Email incorrecto")

    """
def buclesIV():
    pass
    """                 BUCLES IV         

    i = 1

    while i <= 10:
        print("Ejecucion {}".format(i))
        i += 1

    print("Termino la ejecucion")

    edad = int(input("Introduce tu edad: "))

    while edad < 5 or edad >100:
        print("Haz introducido una edad erronea chango, otra vez!")
        edad=int(input("Introduce tu edad: "))

    print(f"La edad es correcta y es {edad}")

    import math
    print("PROGRAMA DE CALCULO DE RAIZ CUADRADA")

    numero = int(input("Introduce un numero: "))
    intentos = 0

    while numero < 0:
        print("No se puede hallar la raiz de un numero negativo")
        if intentos == 2:
            print("Se agotaron los intentos. Programa finalizado") 
            break
        numero = int(input("Introduce un numero: "))
        if numero < 0:
            intentos += 1 

    if intentos < 2:
        solucion = math.sqrt(numero)
        print("La raiz cuadrada de {} es {}".format(numero,solucion))

    """
def buclesV():
    pass
    """                 BUCLES V         
    #Continue__________________________
    for letra in "python":
        if letra =="h":
            continue
        print("Viendo la letra {}".format(letra))

    nombre ="Pildoras Informaticas"
    print(len(nombre))

    i = 0
    for letra in nombre:
        if letra  == " ":
            continue
        i += 1

    print (i)

    #Pass____________________________
    class MiClase:
        pass

    def miFincion():
        pass

    #Else___________________________
    while True:
        email  = input("Introduce tu email: ")
        for i in email:
            if i == "@":
                arroba = True
                break
        else:
            arroba = False

        print(arroba)

    """
def generadoresI():
    pass
    """                 GENERADORES I         
    #Usando funciones
    def funcionPares(limite):
        num = 1
        milista=[]
        while num<limite:
            milista.append(num*2)
            num += 1
        return milista

    print(funcionPares(10))
    #Usando generadores
    def generaPares(limite):
        num = 1
        while num<limite:
            yield num*2
            num += 1
    objetoIterable = generaPares(10)

    print(next(objetoIterable))
    print("Un saltito...")
    print(next(objetoIterable))
    print("Un saltito...")
    print(next(objetoIterable)) """
def generadoresII():
    pass
    """                 GENERADORES II         
    def devuelveCiudades(*ciudades): #Con * indicamos que no sabemos cuantos elementos recibira (tupla)
        #Blucle principal_________________
        for elemnto in ciudades:
            #Blucle anidado___________________
            #for subElemto in elemnto:
                yield from elemnto

    ciudadesDevueltas = devuelveCiudades("Madrid","Barcelona", "Bilbao", "Valencia")

    print(next(ciudadesDevueltas))
    print(next(ciudadesDevueltas)) """
def excepcionesI():
    pass
    """                 EXCEPCIONES I         
    def suma(num1, num2):
        return num1+num2

    def resta(num1, num2):
        return num1-num2

    def multiplica(num1, num2):
        return num1*num2

    def divide(num1,num2):	
        try:	
            return num1/num2
        except ZeroDivisionError:
            print("Error matematico: No es posible dividir entre 0")
            return "Operacion erronea"

    while True:
        try:
            op1=(int(input("Introduce el primer número: ")))
            op2=(int(input("Introduce el segundo número: ")))	
            break	
        except ValueError:
            print("No se aceptan letras, solo numeros")

    operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

    if operacion=="suma":
        print(suma(op1,op2))

    elif operacion=="resta":
        print(resta(op1,op2))

    elif operacion=="multiplica":
        print(multiplica(op1,op2))

    elif operacion=="divide":
        print(divide(op1,op2))

    else:
        print ("Operación no contemplada")


    print("Operación ejecutada. Continuación de ejecúción del programa ")"""
def excepcionesII():
    pass
    """                 EXCEPCIONES II         
    def divide():
        try:
            op1=(float(input("introduce el primer numero: ")))
            op2=(float(input("introduce el segundo numero: ")))
            print("La division es: "+ str(op1/op2))
        except ValueError:
            print("El valor introducido es erroneo")
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
        finally:
            print("calculo finalizado")

    divide() """
def ecxepcionesIII():
    pass
    """                 EXCEPCIONES III         
    def evaluaEdad(edad):
        if edad < 0:
            raise TypeError("La edad no puede ser menor que 0")
        if edad < 20:
            return "Eres muy joven arreh"
        elif edad < 40:
            return "Eres joven"
        elif edad < 65:
            return "Eres maduro"
        elif edad < 100:
            return "cuidate"

    try:
        print(evaluaEdad(70))
    except TypeError as EroorDeNumeroNegativo:
        print(EroorDeNumeroNegativo)

    try:
        print(evaluaEdad(-70))
    except TypeError as EroorDeNumeroNegativo:
        print(EroorDeNumeroNegativo)
        
    print("Programa terminado") """

