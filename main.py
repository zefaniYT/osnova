import mysql.connector
from mysql.connector import Error                                                       #обработка ошибок и исключений
from External.config import db_config

def create_connection_mysql_db(db_host, user_name, user_password, db_name = None):      #функция соедениния к базе
    connection_db = None
    try:
        connection_db = mysql.connector.connect(
            host=db_host,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to the table is successful")
    except Error as db_connection_error:
        print("Error: ", db_connection_error)
    return connection_db

conn = create_connection_mysql_db(db_config["mysql"]["host"],
                                  db_config["mysql"]["user"],
                                  db_config["mysql"]["pass"])


cursor = conn.cursor(dictionary=True)                        #для взаимодействия (удаление, добавление и т.п)
cursor.execute(f"SELECT %d, %d", (1, 2))




class ManagmentClient():
    """модель возможности работы с клиентами"""
    def add(self, name):
        """функция добавления"""
        self.name = name

    def change(self, name):
        """функция замены"""
        self.name = name

    def delete(self, name):
        """фунцкия удаления"""
        self.name = name
