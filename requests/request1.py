import config
import mysql.connector

class request1:
    def __init__(self, data_start, data_stop):
        self.data_start = data_start
        self.data_stop = data_stop
        self.mistake = ""

    def internal_request(self, data_start, data_stop):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                select_dates = f"""{data_start} {data_stop}"""
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute(select_dates)
                    result = cursor.fetchall()
                    res = []
                    for i in result:
                        res.append(i)

                    return res

        except Exception as e:
            self.mistake = e