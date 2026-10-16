import machine
import utime
import dht

pot = machine.ADC(26)
capteur = dht.DHT11(machine.Pin(22))
led_pwm = machine.PWM(machine.Pin(18))
buzzer = machine.PWM(machine.Pin(16))

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9), freq=400000)
LCD_ADDR = 0x3E

def lcd_cmd(cmd):
    try:
        i2c.writeto_mem(LCD_ADDR, 0x80, bytes([cmd]))
    except:
        pass

def lcd_write(txt):
    try:
        for c in txt:
            i2c.writeto_mem(LCD_ADDR, 0x40, bytes([ord(c)]))
    except:
        pass

def lcd_init():
    utime.sleep_ms(50)
    lcd_cmd(0x38)
    lcd_cmd(0x0C)
    lcd_cmd(0x01)
    utime.sleep_ms(5)

def lcd_clear():
    lcd_cmd(0x01)
    utime.sleep_ms(2)

def lcd_set_cursor(col, row):
    col = col & 0x0F
    row = row & 0x01
    lcd_cmd(0x80 | (col + (0x40 if row == 1 else 0x00)))

lcd_init()
led_pwm.freq(1000)
buzzer.freq(1000)

temp_mesuree = 20
last_dht_read = 0
alarm_col = 0
alarm_blink = 0

while True:
    val_pot = pot.read_u16()
    temp_consigne = int(15 + (val_pot / 65535) * 20)

    now = utime.ticks_ms()
    if utime.ticks_diff(now, last_dht_read) > 1000:
        try:
            capteur.measure()
            temp_mesuree = capteur.temperature()
        except:
            pass
        last_dht_read = now

    lcd_set_cursor(0, 0)
    lcd_write("Set: " + str(temp_consigne) + "C   ")

    lcd_set_cursor(0, 1)
    lcd_write("Ambient: " + str(temp_mesuree) + "C ")

    if temp_mesuree >= temp_consigne + 3:
        buzzer.duty_u16(15000)
        led_pwm.duty_u16(65535)
        utime.sleep(0.1)
        led_pwm.duty_u16(0)
        utime.sleep(0.1)

        alarm_blink += 1
        if alarm_blink % 2 == 0:
            lcd_set_cursor(alarm_col, 0)
            lcd_write(" ALARM ")
        else:
            lcd_set_cursor(alarm_col, 0)
            lcd_write("       ")
        
        alarm_col = (alarm_col + 1) % 9

    elif temp_mesuree > temp_consigne:
        buzzer.duty_u16(0)
        for brillance in range(0, 65535, 6500):
            led_pwm.duty_u16(brillance)
            utime.sleep(0.1)
        for brillance in range(65535, 0, -6500):
            led_pwm.duty_u16(brillance)
            utime.sleep(0.1)

    else:
        buzzer.duty_u16(0)
        led_pwm.duty_u16(0)
        utime.sleep(0.2)