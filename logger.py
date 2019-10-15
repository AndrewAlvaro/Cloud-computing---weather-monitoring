#!/usr/bin/env python3
import sqlite3

class Logger:

    def dataLogger(self, timestamp, temperature, humidity):
        DB_NAME = "sensehat.db"
        connection = sqlite3.connect(DB_NAME)
        with connection:
             connection.execute(
             """INSERT INTO environment_data(timestamp, temperature, humidity)
             VALUES (:timestamp, :temperature, :humidity)""", {"timestamp": timestamp, "temperature": temperature, "humidity": humidity })

    
    
    def displayData(self):
        DB_NAME = "sensehat.db"
        connection = sqlite3.connect(DB_NAME)
        connection.row_factory = sqlite3.Row 
        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM environment_data")
        
            print("Database content:")
            print("-----------------")
            print("Time              Temperature Humidity")
            for row in cursor:
                print(row["timestamp"], row["temperature"], row["humidity"], sep="   ")

