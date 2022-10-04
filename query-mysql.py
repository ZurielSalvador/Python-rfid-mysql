#BIbliotecas
import mysql.connector

#conexion
cnx = mysql.connector.connect(user='Zuriel', password='117',host='127.0.0.1',database='codigoIoT')

#cursor = cnx.cursor()

#Query

query = ("SELECT id,nombre,temp,hum FROM clima WHERE temp=23.52;")

#Ejcucion
res = cnx.cmd_query(query)

#Imprimir resultado
print("Respuesta")
print(res)


#Cerrar
cnx.close()


