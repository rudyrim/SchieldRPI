import os
import subprocess
import RPi.GPIO as GPIO
import time
import spidev # To communicate with SPI devices
from numpy import interp    # To scale values
import smbus
import sys

bus = smbus.SMBus(1)
EEPROM = 0x50             # 24LC256 i2c bus address
TEMP = 0x4F
#os.system("python stats.py")

try :
    bus.write_byte(EEPROM,0)
    os.system("gpio -g mode 13 pwm")
    os.system("gpio -g pwm 13  1023")

except :
    os.system("gpio -g mode 13 pwm")
    os.system("gpio -g pwm 13  256")   

try :
    bus.read_byte_data(TEMP, 0xEE)
    os.system("gpio -g mode 19 pwm")
    os.system("gpio -g pwm 19  1023")
    
except :
    os.system("gpio -g mode 19 pwm")
    os.system("gpio -g pwm 19  256")
    
time.sleep(1)    
DI0=7
DI1=11
DI2=13
DI3=15
DI4=12

GPIO.setmode(GPIO.BOARD)#Board

GPIO.setup(DI0, GPIO.IN)
GPIO.setup(DI0, GPIO.IN)
GPIO.setup(DI1, GPIO.IN)
GPIO.setup(DI2, GPIO.IN)
GPIO.setup(DI3, GPIO.IN)
GPIO.setup(DI4, GPIO.IN)

os.system("gpio mode 7 in")
os.system("gpio mode 0 in")
os.system("gpio mode 2 in")
os.system("gpio mode 3 in")
os.system("gpio mode 1 in")

os.system("gpio mode 21 out")
os.system("gpio mode 22 out")
os.system("gpio mode 23 out")
os.system("gpio mode 24 out")
os.system("gpio mode 25 out")

os.system("gpio mode 27 out")
os.system("gpio mode 28 out")
os.system("gpio mode 29 out")


os.system("gpio write 21 1")
os.system("gpio write 22 1")
os.system("gpio write 23 1")
os.system("gpio write 24 1")
os.system("gpio write 25 1")
os.system("gpio write 27 1")
os.system("gpio write 28 1")
os.system("gpio write 29 1")
time.sleep(1)
os.system("gpio write 21 0")
os.system("gpio write 22 0")
os.system("gpio write 23 0")
os.system("gpio write 24 0")
os.system("gpio write 25 0")

os.system("gpio write 27 0")
os.system("gpio write 28 0")
os.system("gpio write 29 0")

spi = spidev.SpiDev() # Created an object
spi.open(0,0)   

# Initializing LED pin as OUTPUT pin
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
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
    if GPIO.input(DI0) :
        os.system("gpio toggle 21")
    if GPIO.input(DI1) :
        os.system("gpio toggle 22")
    if GPIO.input(DI2) :
        os.system("gpio toggle 23")
    if GPIO.input(DI3) :
        os.system("gpio toggle 24")
    if GPIO.input(DI4) :
        os.system("gpio toggle 25")


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
    time.sleep(0.1)
    pass