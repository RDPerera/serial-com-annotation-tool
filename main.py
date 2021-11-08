# Importing Libraries
import serial
import time
import random
from playsound import playsound

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)


def read():
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8').rstrip()
    return data

musicList=["HAHV1","HAHV2","HAHV3","HAHV4","LAHV1","LAHV2","LAHV3","LAHV4","HALV1","HALV2","HALV3","HALV4","LALV1","LALV2","LALV3","LALV4"]
musicList=["HAHV1"]
log = open("log.txt", "a")
while True:
    value = read()
    print(value)
    if value == "1":
        randomIdx=random.randint(0, len(musicList)-1)
        music = musicList[randomIdx]
        musicList.remove(music)
        #start counting time
        start = time.time()
        playsound('/'+music+'.wav')
        print('playing Music'+)
        




