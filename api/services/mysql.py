import mysql.connector


def create_db_if_not_exists():
    mysqldb = mysql.connector.connect(
        host="localhost", user="newscred", passwd="Mysql123456:P"
    )
    mysql_cursor = mysqldb.cursor()
    query = "CREATE DATABASE IF NOT EXISTS users_db"
    mysql_cursor.execute(query)
    mysql_cursor.execute("SHOW DATABASES")

    for eachdb in mysql_cursor:
        print(eachdb)
