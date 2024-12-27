import mysql.connector;
from mysql.connector import errorcode;

try:
	connection = mysql.connector.connect(host='localhost', user='root', password='495499', database='db_gedesmg')
	print("Database connection made!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)
else:
	connection.close()

connection = mysql.connector.connect(host="localhost", user="root", passwd="495499", database="db_gedesmg")
cursor = connection.cursor()
	