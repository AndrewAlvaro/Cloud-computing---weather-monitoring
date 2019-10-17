#!/usr/bin/env python3
import requests
import json
import os
import datetime
import csv

class pushNotification:


    def send_notification_via_pushbullet(self, title, body):
        ACCESS_TOKEN = "o.T3YzoJfL2PpiSk54KMTsTm9Y0VtSjjdS"
        timestamp = datetime.datetime.now().strftime('%d/%m/%Y')

        data = { "type": "note", "title": title, "body": body }

        response = requests.post("https://api.pushbullet.com/v2/pushes", data = json.dumps(data),
            headers = { "Authorization": "Bearer " + ACCESS_TOKEN, "Content-Type": "application/json" })

        if(response.status_code != 200):
            raise Exception()
        
        if(response.status_code == 200):
            print("Notification sent.")


    def send(self, temperature, humidity):
        push = pushNotification()
        push.send_notification_via_pushbullet("Weather update", "Temperature: " + str(temperature) + "\nHumidity: " + str(humidity) + "\nFrom weather monitor")
    