#Biblioteca

import mysql.connector


#Programa
cnx = mysql.connector.connect(user='Zuriel', password='117',
                              host='127.0.0.1',
                              database='codigoIoT')

print("Conexion realizada")
print(cnx)

print("Cerrar conexion")
cnx.close()
print("conexcion cerrada")
