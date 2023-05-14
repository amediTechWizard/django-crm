import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = ''

	)

cusrsorObject = dataBase.cursor()

cusrsorObject.execute("CREATE DATABASE website")

print("All Done!")