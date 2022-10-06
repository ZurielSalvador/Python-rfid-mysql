#Bibliotecas
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user = 'Zuriel',password='117',host='127.0.0.1',database='rfid')

#Cursor
cursor = cnx.cursor()

#Query de insersecion 
query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Zuriel','Test Python 1',2963)"


#Ejecutar cursor
cursor.execute (query_insert)


#Asegurarse de realizar la operacion en BD

cnx.commit()

print("Query Ok")


#Cerrar

cursor.close()

cnx.close()
