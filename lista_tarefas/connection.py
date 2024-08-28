import mysql.connector

mydatabase = mysql.connector.connect(host="localhost", user="root", password="", database="lista_tarefas")

myqueries = mydatabase.cursor()