from lib_lcd1602_i2c_pico import I2cLcd
from machine import I2C
from machine import Pin
import utime as time
 
 
i2c = I2C(id=1,scl=Pin(19),sda=Pin(18),freq=10000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
 
while True:
      lcd.move_to(0,1)
      lcd.putstr('Hello world')