nombre = "Zuriel"
texto = "Texto del RFID"
rfid = "29635458"

#Query de insersecion 
#query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Zuriel','Test Python 1',2963)"



insertquery = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('"+ nombre +"','"+ texto +"'," + str(rfid)+")"

print(insertquery)


