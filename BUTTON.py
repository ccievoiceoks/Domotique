import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.IN)
input = GPIO.input(21)
print input
while True:
      if (GPIO.input(21)):
              print GPIO.input(21)
              print("Open Contact")
              time.sleep(2)
      else:
              print GPIO.input(21)
              print ("Closed Contact")
              time.sleep(2)

