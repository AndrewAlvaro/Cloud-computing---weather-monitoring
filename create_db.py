#!/usr/bin/env python3

import sqlite3
import sys


class CreateDB:
    
    def createData(self):
        connection = sqlite3.connect("sensehat.db")

        with connection:
            connection.execute("CREATE TABLE environment_data(timestamp DATETIME, temperature NUMERIC, humidity NUMERIC)")
        connection.close()

create = CreateDB()

def main():
    create.createData()

if __name__ == "__main__":
    main()

    
