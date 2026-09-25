import machine
import utime

LED = machine.Pin(16, machine.Pin.OUT)
BP = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)

counter = 0
counter_old = 0
last_press_time = 0

def bp_handler(pin):
    global counter, last_press_time
    current_time = utime.ticks_ms()
    counter_old = counter
    
    if utime.ticks_diff(current_time, last_press_time) > 200:
        last_press_time = current_time
        counter += 1
        if counter > 3:
            counter = 1

BP.irq(trigger=machine.Pin.IRQ_RISING, handler=bp_handler)

def effect():
    for i in range(5):
        LED.value(1)
        utime.sleep(0.05)
        LED.value(0)
        utime.sleep(0.05)
        
while True:
    if counter == 1:
        if counter != counter_old:
            effect()
            counter_old = counter
        # Clignotement lent
        LED.value(1)
        utime.sleep(2)
        LED.value(0)
        utime.sleep(2)

    elif counter == 2:
        if counter != counter_old:
            effect()
            counter_old = counter
        # Clignotement rapide
        LED.value(1)
        utime.sleep(0.5)
        LED.value(0)
        utime.sleep(0.5)

    elif counter == 3:
        if counter != counter_old:
            effect()
            counter_old = counter
        # LED éteinte
        LED.value(0)
        utime.sleep(0.1)
