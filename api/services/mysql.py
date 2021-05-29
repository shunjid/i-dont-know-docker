import mysql.connector


def create_db_if_not_exists():
    mysqldb = mysql.connector.connect(
        host="db", user="root", passwd="root"
    )
    mysql_cursor = mysqldb.cursor()
    query = "CREATE DATABASE IF NOT EXISTS users_db"
    mysql_cursor.execute(query)
    mysql_cursor.execute("SHOW DATABASES")

    for eachdb in mysql_cursor:
        print(eachdb)
