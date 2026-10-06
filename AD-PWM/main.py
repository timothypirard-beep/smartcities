import machine
import utime

pot = machine.ADC(26)
buzzer = machine.PWM(machine.Pin(16))
led = machine.Pin(18, machine.Pin.OUT)
bp = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)

sound_mode = 1
last_time = 0

def bp_handler(pin):
    global sound_mode, last_time
    now = utime.ticks_ms()
    if utime.ticks_diff(now, last_time) > 250:
        last_time = now
        sound_mode += 1
        if sound_mode > 2:
            sound_mode = 1

bp.irq(trigger=machine.Pin.IRQ_RISING, handler=bp_handler)

while True:
    val = pot.read_u16()
    
    if val < 2000:
        volume = 0
    else:
        volume = val // 2

    if sound_mode == 1:
        buzzer.freq(1000)
        t_on = 0.3
        t_off = 0.3
    else:
        buzzer.freq(2000)
        t_on = 0.1
        t_off = 0.1

    if volume > 0:
        buzzer.duty_u16(volume)
        led.value(1)
    else:
        buzzer.duty_u16(0)
        led.value(0)
    utime.sleep(t_on)

    buzzer.duty_u16(0)
    led.value(0)
    utime.sleep(t_off)
