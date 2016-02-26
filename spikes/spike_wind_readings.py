import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
import datetime
import time

ticks = dict()
def print_me(chanel):
    print int(time.time())
    #global ticks
    #temp_time = int(time.time())
    #if temp_time not in ticks:
    #    ticks[temp_time] = 0
    #ticks[temp_time] += 1

GPIO.add_event_detect(24, GPIO.FALLING, callback=print_me)#, bouncetime=1) 
while True:
    #print GPIO.input(24)
    pass
    #print len(ticks.keys())
    #print [key for key in ticks.keys() ]
    #if len(ticks.keys()) > 1:
    #    for key in sorted(ticks.keys())[:-1]:
    #        print str(ticks[key])
    #        del ticks[key]

