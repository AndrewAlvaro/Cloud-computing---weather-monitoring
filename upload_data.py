import os, pymysql
import pymysql.cursors
class upload_data:
    def upload(self, timestamp, temperature, humidity):

        connection = pymysql.connect(
                                    host='35.232.83.178',
                                    user='s3559384',
                                    password='root',
                                    db='greenhouse')
        
        with connection:
                    cursor = connection.cursor()
                    query = "INSERT INTO environment_data (timestamp, temperature, humidity) VALUES (%s, %s, %s)"
                    data = (timestamp, temperature, humidity)
                    cursor.execute(query, data)
                    results = cursor.fetchall()