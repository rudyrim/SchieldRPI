import time
import os
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess

RST = None     # on the PiOLED this pin isnt used
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()

while True:

    draw.rectangle((0,0,width,height), outline=0, fill=0)
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    try: 
        SSID = subprocess.check_output("iwgetid -r", shell = True )
    except:
        SSID = "still waiting ..."
    draw.text((x, top),       "Schield RPI v1.O ",  font=font, fill=255)
    draw.text((x, top+8),     "IP: " + str(IP),  font=font, fill=255)
    draw.text((x, top+16),    "User & Mdp:  ip",  font=font, fill=255)
    if SSID:
        draw.text((x, top+25),    "SSID: " + str(SSID),  font=font, fill=255)
    disp.image(image)
    disp.display()
    time.sleep(.1)