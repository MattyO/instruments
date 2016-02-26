import Adafruit_ADS1x15
import time
print Adafruit_ADS1x15.__file__
adc = Adafruit_ADS1x15.ADS1015()
while True: 
    print adc.read_adc(0, gain=1)
    #time.sleep(.5)
