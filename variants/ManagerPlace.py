import config
import variants.place as place
import mysql.connector


class CountryManager:
    def add(self, path: place.Country):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                add_Country = f"""
                    INSERT INTO Country
                    (name)
                    VALUES
                     ('{path.name}')"""
                with connection.cursor() as cursor:
                                cursor.execute(add_Country)
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
                change_Country = f"""
                    UPDATE Country SET
                    NAME = '{path.name}'                   
                    WHERE id = {path.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Country)
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
                delete_Country = f"""
                DELETE FROM Country
                WHERE id = {path.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_Country)
                    connection.commit()
        except Exception as Error:
            return Error
        #Конец функций страны

class CityManager:
    def add(self, path: place.City):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                add_City = f"""
                    INSERT INTO City
                    (country_id, name)
                    VALUES
                     ('{path.country_id}  ,{path.name}')"""
                with connection.cursor() as cursor:
                    cursor.execute(add_City)
                    connection.commit()
        except Exception as Error:
            return Error

    def change(self, path: place.City):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_City = f"""
                    UPDATE City SET
                    NAME = '{path.name}, country_id = '{path.country_id}
                    WHERE id = {path.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_City)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, path: place.City):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_City = f"""
                DELETE FROM City
                WHERE id = {path.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_City)
                    connection.commit()
        except Exception as Error:
            return Error

class HotelManager:
    def add(self, path: place.Hotel):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                add_Hotel = f"""
                    INSERT INTO Hotel
                    (city_id, stars, price, name)
                    VALUES
                     ('{path.city_id}, {path.stars}, {path.price}  ,{path.name}')"""
                with connection.cursor() as cursor:
                    cursor.execute(add_Hotel)
                    connection.commit()
        except Exception as Error:
            return Error

    def change(self, path: place.Hotel):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_Hotel = f"""
                    UPDATE Hotel SET
                    NAME = '{path.name}, city_id = '{path.city_id}, stars = {path.stars}, price = {path.price}
                    WHERE id = {path.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Hotel)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, path: place.Hotel):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_Hotel = f"""
                DELETE FROM Hotel
                WHERE id = {path.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_Hotel)
                    connection.commit()
        except Exception as Error:
            return Error