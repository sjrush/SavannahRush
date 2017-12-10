

import ftplib
import sys
import os
import RPi.GPIO as GPIO
import time
from subprocess import call

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pin = GPIO.PWM(12,50)
pin.start(7.5)

value=1
def getFile1():

    ftp=ftplib.FTP("000kwdv.wcomhost.com", "ftp3285986", "gejFdjs0")
    ftp.cwd("/htdocs/lockdoor")
    gFile=open("doorstatus.txt", "wb")
    ftp.retrbinary('RETR doorstatus.txt', open('status.txt', 'wb').write)
    gFile.close()
    ftp.quit()


def sendPic():
    os.system("fswebcam --no-banner /home/pi/image.jpg")
    ftp=ftplib.FTP("000kwdv.wcomhost.com", "ftp3285986", "gejFdjs0")
    ftp.cwd("/htdocs/lockdoor")
    F=open("image.jpg", "rb")
    ftp.storbinary('STOR image.jpg', F, 1024)

while value==1:
    getFile1()
    sendPic()
    with open('status.txt') as myfile:
        if "un" in myfile.read():
            print("unlock")
            pin.ChangeDutyCycle(6)

        else:
            pin.ChangeDutyCycle(8.5)
            print("lock")

    time.sleep(5)
