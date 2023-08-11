import psycopg2

def conectarse():
    connection = psycopg2.connect(user = "******",password = "******",host = "******",port = "******",database = "******")
    cursor = connection.cursor()
    return cursor    


def consultardb(xdb, cadena):
    xdb.execute(cadena)
    tabla = xdb.fetchall()      

    if tabla != []: 
        for i in tabla:
            return tabla
    else:
        return None

def guardardb(xdb, cadena):
    xdb.execute(cadena)
    try:
        tabla = xdb.fetchall() 
        if tabla != []: 
            return tabla
    except:
        pass

     
     
    