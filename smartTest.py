import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import grovepi
import subprocess
import picamera
from grove_i2c_barometic_sensor_BMP180 import BMP085
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import json
from threading import Thread
#from firebase import firebase

temp_humidity_sensor    = 7  

#API KEY - FIREBASE

cred = credentials.Certificate('/home/pi/Desktop/smartBabyMonitorProject/cred.json')
#Initializalize  the app with a service account, granting admin privilegeges

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-baby-monitor-d19e1.firebaseio.com/'
    })
#firebase = firebase.FirebaseApplication('https://smart-baby-monitor-d19e1.firebaseio.com', NONE)

sound_sensor = 0                # Connect the Grove Sound Sensor to analog port A0                 #Light Sensor Port Number
#dht_sensor_port = 7              #Temperature & Humidity sensor
#dht_sensor_type = 0
blue=0
white=1
therm_version = blue 

ref = db.reference('status')

while True:
    
    #humid, temp = DHT.read_retry(DHT.DHT11, 7)
    [Temperature,Humidity] = grovepi.dht(temp_humidity_sensor,therm_version)
    Sound = grovepi.analogRead(sound_sensor)
    #return temp, humid

    print("Let's start with getting python to read from the sensor..")
    print("humidity is", Humidity)
    print("temperature is", Temperature)
    print("sound is", Sound)

    #####


    print("Now let's upload that to Firebase")

    ref.push({
        "Humidity": Humidity,
        "Temperature":Temperature,
        "Sound": Sound
        })


    sleep(2)
    print("Give it a moment to upload...")
    sleep(20)
    
