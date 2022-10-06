#Bibliotecas

import mysql.connector


#Conexion
#cnx = mysql.connector.connect(user = 'Zuriel',password='117',host='localhost',database='codigoIoT')
cnx = mysql.connector.connect(user='Zuriel', password='117',
                              host='127.0.0.1',
                              database='codigoIoT')


#cursor
cursor = cnx.cursor()


#query

query = ("SELECT id,nombre,temp,hum FROM clima WHERE nombre='Zuriel';")


#Ejecutar cursor

cursor.execute (query)

res = cursor.fetchall ()

for x in res:
    print (x)


