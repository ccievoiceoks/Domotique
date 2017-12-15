import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
input = GPIO.input(21)
print input
counters=0
max_counters=int(raw_input(" How many times do I need to iterate the loop? :"))
while counters<max_counters:
      if (GPIO.input(21)):
              print "Value Contact =====> ",GPIO.input(21)
              print("Open Contact")
       	      GPIO.output(4,GPIO.LOW)
	      GPIO.output(18,GPIO.HIGH)
              time.sleep(1)
              counters+=1
              print "Counters => " + str(counters)
      else:
              print "Value Contact =====> ",GPIO.input(21)
              print ("Closed Contact")
              GPIO.output(18,GPIO.LOW)
	      GPIO.output(4,GPIO.HIGH)
              time.sleep(1)
              counters+=1
              print "Counters => " + str(counters)
GPIO.output(4,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
print " "
print " Script Terminated" 
