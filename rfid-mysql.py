#Blibliotecas incorporadas

from time import sleep 
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import mysql.connector

#Iniciar el sensor
reader = SimpleMFRC522()

#Conexión
cnx = mysql.connector.connect(user='Zuriellan', password='117', host='192.168.100.33', database='rfid')

#Cursor
cursor = cnx.cursor()

#Cuerpo del programa
try:
    #Leer el tag
    while True:
        print("Acercar el tag al lector")
        id,text = reader.red()
        print("ID: %s\nText: %s" % (id,text))
        query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Zuriel','"+text+"','"+str(id)+");"


        #Ejecutar cursor
        cursor.execute (query_insert)
        #Asegurarse de realizar la operación en BD
        cnx.commit()
        print("Query OK")

        sleep(5)


except KeyboardInterrupt:
    #cerrar
    cursor.close()
    cnx.close()
    GPIO.cleanup()
    raise





