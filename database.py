import psycopg2


"""To create a new database 'project'."""
conn = psycopg2.connect(dbname="project", user="postgres", password="postgres", host="localhost")
cursor = conn.cursor()

conn.autocommit = True

sql = "CREATE DATABASE project"

cursor.execute(sql)
cursor.close()
conn.close()