#!/usr/bin/env python3
from sense_hat import SenseHat
import datetime
import time
from logger import Logger
from upload_data import upload_data
import sqlite3

class Info:

   SAMPLE_FREQUENCY_SECONDS = 3

   def getInfo(self):
      
      sense = SenseHat()
      timestamp = datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S')
      temperature = sense.get_temperature()
      humidity = sense.get_humidity()
      
      if temperature is not None:
        temperature = round(temperature, 2)
        
      if humidity is not None:
        humidity = round(humidity, 2)
      
      return timestamp, temperature, humidity
   



def main():
   info = Info()
   logData = Logger()
   uploadData = upload_data()
   timestamp, temperature, humidity = info.getInfo()

   logData.dataLogger(timestamp, temperature, humidity)
   time.sleep(info.SAMPLE_FREQUENCY_SECONDS)

   uploadData.upload(timestamp, temperature, humidity)


if __name__ == "__main__":
        main()
