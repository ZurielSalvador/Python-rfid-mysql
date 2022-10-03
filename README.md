# Python-rfid-mysql


Autor: Victor Zuriel Dominguez Salvador


Autor de programas: Codigo IoT


### Recomendaciones para el entendimiento del ejercicio


https://github.com/pimylifeup/MFRC522-python

https://pimylifeup.com/raspberry-pi-rfid-rc522/


 


Este repositorio contiene el ejercicio de Raspberry Pi que hace uso del sensor MFRC522, lee un tag RFID de 13.56Mhz y reporta en Base de Datos  MySQL




Buscar una biblioteca para manejar el sensor MFRC522


- pip install mfrc522 ó sudo pip3 install mfrc522
- Satisfacer dependencias: RPi.GPIO y spidev



*Nota: que se encuentre la interfaz de RAspberry Pi4, iremos a prefrencias-RaspBerry Pi Configuration-Interfacez-SPI, una vez echo anterior reiniciaremos la Raspberry Pi.*





### Ejecutar ejemplo de lectura y Ejecutar ejemplo de escritura


para ello es importante clonar el repositorio con lo programas ya establecidos.


Abrimos una terminal en dónde se ejecutan los siguiente comando:


- python3 write-tag.py
- python3 read-tag.py


*Nota2: Estos programas se encuentran en este mismo repositorio*



## Evidencias


Circuito en Físico:
[![Circuito-en-fisico-tag.jpg](https://i.postimg.cc/MHkgH5gL/Circuito-en-fisico-tag.jpg)](https://postimg.cc/qhL1ZsJc)


Terminal con la ejecución de los programas:
[![tag.png](https://i.postimg.cc/bNhKj6xD/tag.png)](https://postimg.cc/dD5W2jSw)



### Video con una breve explicación


YouTube: https://youtu.be/UrO7WBSpw5U 


