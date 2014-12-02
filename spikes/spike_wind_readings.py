import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def print_me(chanel):
    print 'stuff happening'
GPIO.add_event_detect(12, GPIO.FALLING, callback=print_me, bouncetime=30) 
while True:
    pass
