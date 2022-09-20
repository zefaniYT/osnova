import config
import variants.transportation as transportation
import mysql.connector


class TransportationManager:
    def add(self, path: transportation.Transport):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                add_Transport = f"""
                    INSERT INTO transportation
                    (name, price)
                    VALUES
                    ('{path.name}', {path.price})"""
                with connection.cursor() as cursor:
                                cursor.execute(add_Transport)
                                connection.commit()
        except Exception as Error:
            return Error

    def change(self, path: transportation.Transport):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                change_Transport = f"""
                    UPDATE Transport SET
                    NAME = '{path.name}', price = '{path.price}'
                    WHERE id = {path.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Transport)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, path: transportation.Transport):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                delete_Transport = f"""
                DELETE FROM Transport
                WHERE id = {path.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_Transport)
                    connection.commit()
        except Exception as Error:
            return Error