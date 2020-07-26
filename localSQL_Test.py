import mysql.connector

 
 
 
def saveToDB(name,age):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
  )
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE movieuserdatabase")
  #mycursor.execute("CREATE TABLE User (name VARCHAR(255), age int(20))")
  sql = "INSERT INTO user (name, age) VALUES (%s, %s)"
  val=(name,age)
  mycursor.execute(sql, val)
  mydb.commit()


  
   
     
