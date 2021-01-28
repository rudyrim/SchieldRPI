# Importing modules
import spidev # To communicate with SPI devices
from numpy import interp    # To scale values
from time import sleep  # To add delay
import RPi.GPIO as GPIO # To use GPIO pins
import time
# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)   

# Initializing LED pin as OUTPUT pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
# Creating a PWM channel at 100Hz frequency
pwm1 = GPIO.PWM(36, 100)
pwm2= GPIO.PWM(38, 100)
pwm3 = GPIO.PWM(40, 100)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0) 

# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

fin = time.time() + 10
while time.time() < fin :
    output1 = analogInput(0) # Reading from CH0
    output1 = interp(output1, [0, 1023], [0, 100])
    output2 = analogInput(1) # Reading from CH0
    output2 = interp(output2, [0, 1023], [0, 100])
    output3 = analogInput(2) # Reading from CH0
    output3 = interp(output3, [0, 1023], [0, 100])
    #print(output)
    pwm1.ChangeDutyCycle(output1)
    pwm2.ChangeDutyCycle(output2)
    pwm3.ChangeDutyCycle(output3)
    sleep(0.1)
    pass