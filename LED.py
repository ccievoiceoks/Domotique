import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.HIGH)
time.sleep(5)
print "Circuit on"
GPIO.output(4,GPIO.LOW)
GPIO.output(18,GPIO.HIGH)
time.sleep(20)
print "Circuit off"
GPIO.output(4,GPIO.HIGH)
GPIO.output(18,GPIO.LOW)
time.sleep(20)
