import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
sensor_temp = machine.ADC(4)
conv_factor = 3.3/65535
while True:
    reading = sensor_temp.read_u16()*conv_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print('Temp = ', temperature)
    if temperature < 20:
        led_onboard.value(0)
    else:
        led_onboard.value(1)
    utime.sleep(2)