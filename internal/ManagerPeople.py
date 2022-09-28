import config
import internal.people
import mysql.connector


class ClientManager:
    def add(self, people: internal.people.Client):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                add_Client = f"""
                    INSERT INTO Client
                    (name)
                    VALUES
                     ('{people.name}')"""
                with connection.cursor() as cursor:
                    cursor.execute(add_Client)
                    connection.commit()
        except Exception as Error:
            return Error

    def change(self, people: internal.people.Client):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                change_Client = f"""
                    UPDATE Client SET
                    NAME = '{people.name}'
                    WHERE id = {people.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Client)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, people: internal.people.Client):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                delete_Client = f"""
                DELETE FROM Client
                WHERE id = {people.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_Client)
                    connection.commit()
        except Exception as Error:
            return Error

class PayerManager:
    def add(self, people: internal.people.Payer):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                add_Payer = f"""
                    INSERT INTO Payer
                    (name)
                    VALUES
                     ('{people.name}')"""
                with connection.cursor() as cursor:
                    cursor.execute(add_Payer)
                    connection.commit()
        except Exception as Error:
            return Error

    def change(self, people: internal.people.Payer):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                change_Payer = f"""
                    UPDATE Payer SET
                    NAME = '{people.name}'
                    WHERE id = {people.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Payer)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, people: internal.people.Client):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                delete_Payer = f"""
                DELETE FROM Payer
                WHERE id = {people.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_Payer)
                    connection.commit()
        except Exception as Error:
            return Error