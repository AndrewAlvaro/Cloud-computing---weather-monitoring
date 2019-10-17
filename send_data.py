#!/usr/bin/env python3
import json 
import csv
import datetime
from pushBullet import pushNotification

class Data:

    def sendData(self, temperature, humidity):
        sendPushBullet = pushNotification()
        sendPushBullet.send(temperature, humidity)
  