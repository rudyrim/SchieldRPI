import smbus
import time
bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
i2c_addr= 0x50  
read_addr = 0x00
for i in range(0,6):
    value=bus.read_byte(i2c_addr)
    print("read:" + str(read_addr) + " val:" + str(value))
    read_addr += 1
    time.sleep(0.5)
    