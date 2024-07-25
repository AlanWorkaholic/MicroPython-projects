import machine
import utime
import _thread

button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 0:
            button_pressed = True
        utime.sleep(0.01)
_thread.start_new_thread(button_reader_thread, ())

file = open("log", "w")
i = 0
while True:
    if button_pressed == True:
        i += 1
        print('кнопка нажата',i,'раз')
        utime.sleep_ms(200)
        global button_pressed
        button_pressed = False
    file.write(str(temp) + "\n")
    file.flush()
    utime.sleep(10)