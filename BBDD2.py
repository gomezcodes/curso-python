import sqlite3

"""conexion = sqlite3.connect("GestionProductos")
cursor   = conexion.cursor()"""

"""cursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos = [
    ("AR01", "pelota"           ,20, "jugueteria"),
    ("AR02", "pantalon"         ,20, "confeccion"),
    ("AR03", "destornillador"   ,20, "ferreteria"),
    ("AR04", "jarron"           ,20, "ceramica"),
]

cursor.execute("INSERT INTO PRODUCTOS VALUES ('AR03','tren',15,'jugueteria')")
"""
conexion = sqlite3.connect("GestionProductos2")
cursor   = conexion.cursor()

cursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos = [
    ( "pelota"           ,20, "jugueteria"),
    ( "pantalon"         ,20, "confeccion"),
    ( "destornillador"   ,20, "ferreteria"),
    ( "jarron"           ,20, "ceramica"),
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)

conexion.commit()
conexion.close()