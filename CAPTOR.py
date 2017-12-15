import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Magnetic Contact
GPIO.setup(21,GPIO.IN)
GPIO.setup(26,GPIO.IN)
#Output Contact Led 
GPIO.setup(18,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

counters=0
max_counters=int(raw_input("\nHow many times do I need to iterate the loop? :\n\n "))
while counters<max_counters:
  if (GPIO.input(21)):
    print "\nValue Contact BAS =====> ",GPIO.input(21)
    print "\nValue Contact HAUT =====> ",GPIO.input(26)
    print("Open Contact")
    GPIO.output(4,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    counters+=1
    print "\nCounters => " + str(counters)
  else:
    print "\nValue Contact BAS =====> ",GPIO.input(21)
    print "\nValue Contact HAUT =====> ",GPIO.input(26)
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
