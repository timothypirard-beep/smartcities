import machine
import neopixel
import utime
import urandom


mic = machine.ADC(26)

led1 = neopixel.NeoPixel(machine.Pin(16), 1)
led1[0] = (0, 0, 0)
led1.write()

#Calcul BPM
last_beat_time = utime.ticks_ms()
minute_timer = utime.ticks_ms()
bpm_records = []
beat_count = 0

while True:
    average = 0
    for i in range(1000):
        noise = mic.read_u16()/256
        average += noise
        noise = average/1000
    #print("Noise level:", noise)

    if noise > 100:
        beat_count += 1
        now = utime.ticks_ms()
        deltat = utime.ticks_diff(now, last_beat_time)

        if deltat >= 50:
            r = urandom.randint(0, 255)
            g = urandom.randint(0, 255)
            b = urandom.randint(0, 255)
            led1[0] = (r, g, b)
            led1.write()

            # Calcul du BPM
            if utime.ticks_diff(now, minute_timer) >= 60000:
                bpm = beat_count
                bpm_records.append(bpm)
                print("BPM:", bpm)
                beat_count = 0
                minute_timer = now

    utime.sleep_ms(10)