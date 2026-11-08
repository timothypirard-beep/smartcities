import network
import ntptime
import utime
import machine

SSID = "S24 Ultra de Timothy"
PASSWORD = "12345678"

servo = machine.PWM(machine.Pin(16))
servo.freq(50)

def set_angle(angle):
    duty = int(1638 + (angle / 180) * (8192 - 1638))
    servo.duty_u16(duty)

for a in range(0, 181, 2):
    set_angle(a)
    utime.sleep_ms(15)

for a in range(180, -1, -2):
    set_angle(a)
    utime.sleep_ms(15)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    utime.sleep(0.5)

ntptime.settime()

while True:
    try:
        ntptime.settime()
    except:
        pass

    t = utime.localtime()
    hour = t[3]
    minute = t[4]

    hour_12 = hour % 12
    angle = (hour_12 * 15) + (minute * 0.25)

    if angle > 180:
        angle = 180

    set_angle(angle)
    utime.sleep(30)