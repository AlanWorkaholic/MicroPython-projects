import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
led_onboard.value(0)
i = 0
while True:
    if button.value() == 0:
        i += 1
        print('кнопка нажата',i,'раз')
        led_onboard.toggle()
        utime.sleep_ms(200)
#        led_onboard.value(1)
#        utime.sleep_ms(1000)
#        led_onboard.value(0)
#        utime.sleep_ms(1000)

#    else:
#        led_onboard.value(1)
#        utime.sleep_ms(100)
#        led_onboard.value(0)
#        utime.sleep_ms(100)