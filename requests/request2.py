import config
import mysql.connector

class request1:
    def __init__(self, id):
        print("succes")
        self.id = id
        self.mistake = ""

    def processing_report(self, id):
        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                select_dates = f"""{id} {id}"""
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute(select_dates)
                    result = cursor.fetchall()
                    print(result)
                    res = []
                    for i in result:
                        res.append(i)

                    return res


        except Exception as e:
            self.mistake = e