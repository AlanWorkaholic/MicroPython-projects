import machine
import utime
import lib_BME280

sda = machine.Pin(16)
scl = machine.Pin(17)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=10000000)
led_onboard = machine.Pin(25, machine.Pin.OUT)
#print(i2c.scan())

data_list = list()
count = 500
#опрос датчика влажности 1 раз в секунду
while True:
  bme = BME280.BME280(i2c=i2c)
  temp = bme.temperature
  hum = bme.humidity
  pres = bme.pressure
  data_list.append(temp)
  if len(data_list) >= count:
         break
#  print(temp, '  ', hum)
#  print('Temperature: ', temp)
#  print('Humidity: ', hum)
#  print('Pressure: ', pres)
#  utime.sleep(1)
print(data_list)