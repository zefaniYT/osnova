import config
import variants.place as place
import mysql.connector


class PlaceManager:
    def add(self, path: place.Country):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                add_Hotel = f"""
                    INSERT INTO Country
                    (name)
                    VALUES
                     ('{path.name}')"""
                with connection.cursor() as cursor:
                                cursor.execute(add_Hotel)
                                connection.commit()
        except Exception as Error:
            return Error

    def change(self, path: place.Country):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_Hotel = f"""
                    UPDATE Country SET
                    NAME = '{path.name}'                   
                    WHERE id = {path.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Hotel)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, path: place.Country):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_Hotel = f"""
    DELETE FROM Country
    WHERE id = {path.id}
                   """
                with connection.cursor() as cursor:
                    cursor.execute(delete_Hotel)
                    connection.commit()
        except Exception as Error:
            return Error