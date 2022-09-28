import config
import internal.tour
import mysql.connector


class TourManager:
    def add(self, tour: internal.tour.Tour):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                add_tour = f"""
                    INSERT INTO Tour
                    (price, transportation_id, hotel_id, days, Departure_date, Arrival_date, name)
                    VALUES
                     ('('{tour.price}, {tour.transportation_id}, {tour.hotel_id}, {tour.days}, {tour.Departure_date}, {tour.Arrival_date}, {tour.name}')"""
                with connection.cursor() as cursor:
                    cursor.execute(add_tour)
                    connection.commit()
        except Exception as Error:
            return Error

    def change(self, tour: internal.tour.Tour):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                change_Transport = f"""
                    UPDATE Client SET
                    NAME = '{tour.name}'
                    WHERE id = {tour.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Transport)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, tour: internal.tour.Tour):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                delete_Transport = f"""
                DELETE FROM Client
                WHERE id = {tour.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_Transport)
                    connection.commit()
        except Exception as Error:
            return Error

class SoldToursManager:
    def add(self, tour: internal.tour.SoldTours):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                add_Country = f"""
                    INSERT INTO Client
                    (name)
                    VALUES
                     ('{tour.tur_id}')"""
                with connection.cursor() as cursor:
                    cursor.execute(add_Country)
                    connection.commit()
        except Exception as Error:
            return Error

    def change(self, tour: internal.tour.SoldTours):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                change_Transport = f"""
                    UPDATE Client SET
                    NAME = '{tour.tur_id}'
                    WHERE id = {tour.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(change_Transport)
                    connection.commit()
        except Exception as Error:
            return Error

    def delete(self, tour: internal.tour.SoldTours):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=str(config.password),
                                         database=config.database,
                                         ) as connection:
                delete_Transport = f"""
                DELETE FROM Client
                WHERE id = {tour.id}"""
                with connection.cursor() as cursor:
                    cursor.execute(delete_Transport)
                    connection.commit()
        except Exception as Error:
            return Error