import config
import variants.place as place
import mysql.connector


class CountryManager:
    def add(self, place: place.Country):
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
                     ('{place.name}')"""
                with connection.cursor() as cursor:
                                cursor.execute(add_Country)
                                connection.commit()
        except Exception as Error:
            return Error

    def change(self, place: place.Country):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_Country = f"""
                    UPDATE Country SET
                    NAME = '{place.name}'                   
                    WHERE id = {place.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Country)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, place: place.Country):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_Country = f"""
                DELETE FROM Country
                WHERE id = {place.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_Country)
                    connection.commit()
        except Exception as Error:
            return Error
        #Конец функций страны

class CityManager:
    def add(self, place: place.City):
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
                     ('{place.country_id}  ,{place.name}')"""
                with connection.cursor() as cursor:
                    cursor.execute(add_City)
                    connection.commit()
        except Exception as Error:
            return Error

    def change(self, place: place.City):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_City = f"""
                    UPDATE City SET
                    NAME = '{place.name}, country_id = '{place.country_id}
                    WHERE id = {place.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_City)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, place: place.City):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_City = f"""
                DELETE FROM City
                WHERE id = {place.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_City)
                    connection.commit()
        except Exception as Error:
            return Error

class HotelManager:
    def add(self, place: place.Hotel):
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
                     ('{place.city_id}, {place.stars}, {place.price}  ,{place.name}')"""
                with connection.cursor() as cursor:
                    cursor.execute(add_Hotel)
                    connection.commit()
        except Exception as Error:
            return Error

    def change(self, place: place.Hotel):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                change_Hotel = f"""
                    UPDATE Hotel SET
                    NAME = '{place.name}, city_id = '{place.city_id}, stars = {place.stars}, price = {place.price}
                    WHERE id = {place.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Hotel)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, place: place.Hotel):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                delete_Hotel = f"""
                DELETE FROM Hotel
                WHERE id = {place.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_Hotel)
                    connection.commit()
        except Exception as Error:
            return Error