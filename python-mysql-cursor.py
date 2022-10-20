#Bibliotecas

import mysql.connector


#Conexion
#cnx = mysql.connector.connect(user = 'Zuriel',password='117',host='localhost',database='codigoIoT')
cnx = mysql.connector.connect(user='Zuriellan', password='117',
                              host='127.0.0.1',
                              database='rfid')


#cursor
cursor = cnx.cursor()


#query

query = ("SELECT id,fecha,nombre,texto,rfid FROM rfid WHERE id='8';")


#Ejecutar cursor

cursor.execute (query)

res = cursor.fetchall ()

for x in res:
    print (x)


