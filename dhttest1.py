
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT11, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11
# connected to GPIO23.
pin = 23
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
while True:
    if humidity is not None and temperature is not None:
        print('Temp={0:0.2f}*C  Humidity={1:0.2f}%'.format(temperature, humidity))
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity>60:
		print ("LED on")
		GPIO.output(24,GPIO.HIGH)
	else:
		print ("LED off")
		GPIO.output(24,GPIO.LOW)
        time.sleep(2)
    else:
        print('Failed to get reading. Try again!')
	
	
