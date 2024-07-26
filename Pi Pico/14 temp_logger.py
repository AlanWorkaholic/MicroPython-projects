import machine
import utime
import lib_BME280
from machine import I2C
from machine import Pin
from lib_lcd1602_i2c_pico import I2cLcd

#датчик влажности
i2c = I2C(id=0, sda=Pin(16), scl=Pin(17), freq=10000)
led_onboard = Pin(25, machine.Pin.OUT)
#дисплей
i2c_d = I2C(id=1,sda=Pin(18),scl=Pin(19),freq=10000)
lcd = I2cLcd(i2c_d, 0x27, 2, 16)
#кнопка
button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

def one_write(x):#x - номер отсчета в логе
    bme = BME280.BME280(i2c=i2c)
    temp = bme.temperature
    hum = bme.humidity
    pres = bme.pressure
    print(temp, '  ', hum)
    lcd.move_to(0,0)
    lcd.putstr('T=  ')
    lcd.putstr(temp)
    lcd.move_to(0,1)
    lcd.putstr('Hum=')
    lcd.putstr(hum)    
    utime.sleep(0.01)
    file.write(str(x) + ' ' + str(temp) + ' ' + str(hum) + "\n")
    file.flush()
#приветственная надпись
lcd.move_to(2,0)
lcd.putstr('Privet, Bro')
lcd.move_to(0,1)
lcd.putstr('Push the button')
#ждем первого нажатия кнопки
while True:
    if button.value() == 0:
        utime.sleep_ms(200)
        break
lcd.clear()
lcd.move_to(2,0)
lcd.putstr('Log starting')
utime.sleep(1)
lcd.clear()
#поиск номера файла
i = -1
while True:
    i += 1
    name = 'temp_log_' + str(i)
    try:
        file = open(name)
        file.close()
    except OSError:
    #    print('файла не существует')
        break
file = open(name, 'w')
j = 1
one_write(j)
interval = 1000 #интервал логирования
timestamp = utime.ticks_ms() #отметка времени

#основнй цикл
while True:
    if (utime.ticks_diff(utime.ticks_ms(), timestamp) >= interval):
        timestamp +=interval
        j +=1
        one_write(j)
    if button.value() == 0:
        lcd.clear()
        lcd.move_to(2,0)
        lcd.putstr('Log stopped')
        file.close()
        break