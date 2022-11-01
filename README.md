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




----------------------------------------------------------------------------------------------------------------


# Ejercicio-rfid-args-mysql.py



## Descripción:

Para este ejercicío se almacenara el rfid y texto que inserte el usuario por medio de un interfaz gráfica utilizando Node-RED, y almacenando en la bas de datos de MySQL.


### Intrucciones:


1. Se elebora un programa capaz del leer la tarjeta RFID y con ello almacenar en la base de datos lo que el usuario escriba.


2. Se elabora un interfaz gráfica utilizando Node-RED desde la Raspberry Pi 4.


3. Finalmente se elaboran un ejercicio con un texto aleatoria para dicha comprobación.




*Nota: Es importante conocer la ruta correcta del programa ubicado en la Raspberry Pi4*


*Nota2: La actualización de la IP ahora sera llamando a la maquina virtual.*



## Evidencias


Nodos de Node-Red:


[![201022-4.png](https://i.postimg.cc/N04GSbpm/201022-4.png)](https://postimg.cc/HJrC70Gk)



Se escribe un texto alazar para que podamos ver la diferencia con los que ya existen en la base datos:


[![201022-5.png](https://i.postimg.cc/Z5J5c1L4/201022-5.png)](https://postimg.cc/KRsbcpVH)



Por ultimo vamos a a la base de datos y obtenemos lo siguiente:


[![201022-2.png](https://i.postimg.cc/tTWK8gXf/201022-2.png)](https://postimg.cc/wyx4mgRc)


El texto fue ilustrado correctamente, y podemos ver que el número del RFID es el mismo.

