import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="T0n1tO#313",
    database="testdatabase"
    )

myCursor = db.cursor()

#myCursor.execute("CREATE TABLE Person (name VARCHAR(50),age smallint UNSIGNED, personId int PRIMARY KEY AUTO_INCREMENT)")
#myCursor.execute("DESCRIBE Person")
#String formating para pasar de forma mas segura

#myCursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)",("Tony",20)) #insertamos un dato
#db.commit() #hacemos el cambio

#myCursor.execute("SELECT * FROM Person")

#for x in myCursor:
    #print(x)


#myCursor.execute("CREATE TABLE test(name varchar(50) NOT NULL ,created datetime NOT NULL, gender ENUM('M','F','O'), "
                 #"id int PRIMARY KEY NOT NULL AUTO_INCREMENT)") creando otra tabla

#myCursor.execute("INSERT INTO Test(name,created, gender) VALUES(%s,%s,%s)",( "Joe",datetime.now(),"M"))

#db.commit()

myCursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id DESC")
for x in myCursor:
    print(x)
