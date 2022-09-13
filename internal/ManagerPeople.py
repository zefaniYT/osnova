import config
import internal.people
import mysql.connector


class Client:
    def add(self, people: internal.people.Client):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                add_Country = f"""
                    INSERT INTO Client
                    (name)
                    VALUES
                     ('{people.name}')"""
                with connection.cursor() as cursor:
                    cursor.execute(add_Country)
                    connection.commit()
        except Exception as Error:
            return Error

    def change(self, people: internal.people.Client):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_Transport = f"""
                    UPDATE Client SET
                    NAME = '{people.name}'
                    WHERE id = {people.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Transport)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, people: internal.people.Client):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_Transport = f"""
                DELETE FROM Client
                WHERE id = {people.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_Transport)
                    connection.commit()
        except Exception as Error:
            return Error

class Payer:
    def add(self, people: internal.people.Payer):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                add_Country = f"""
                    INSERT INTO Client
                    (name)
                    VALUES
                     ('{people.name}')"""
                with connection.cursor() as cursor:
                    cursor.execute(add_Country)
                    connection.commit()
        except Exception as Error:
            return Error

    def change(self, people: internal.people.Client):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_Transport = f"""
                    UPDATE Client SET
                    NAME = '{people.name}'
                    WHERE id = {people.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Transport)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, people: internal.people.Client):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_Transport = f"""
                DELETE FROM Client
                WHERE id = {people.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_Transport)
                    connection.commit()
        except Exception as Error:
            return Error