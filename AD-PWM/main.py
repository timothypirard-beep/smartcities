import machine
import utime

led = machine.Pin(18, machine.Pin.OUT)
buzzer = machine.PWM(machine.Pin(16))
buzzer.freq(1000)

print("--- DEMARRAGE DU TEST ---")

while True:
    print("BIP ON")
    led.value(1)
    buzzer.duty_u16(15000)  # Volume moyen forcé
    utime.sleep(0.5)

    print("BIP OFF")
    led.value(0)
    buzzer.duty_u16(0)
    utime.sleep(0.5)