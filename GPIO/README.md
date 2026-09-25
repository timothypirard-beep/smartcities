import machine
import utime

# ==========================================
# 1. Configuration du matériel (Hardware)
# ==========================================
# LED externe sur GP16 (ou LED interne Pico W : 'LED')
PIN_LED = 16
PIN_BP = 18

led = machine.Pin(PIN_LED, machine.Pin.OUT)
bp = machine.Pin(PIN_BP, machine.Pin.IN, machine.Pin.PULL_DOWN)

# ==========================================
# 2. Variables de gestion des états
# ==========================================
# Bonus 2 : nombre d'appuis requis pour passer à l'état suivant
PRESSES_PER_STAGE = 2

raw_press_count = 0      # Compteur brut d'appuis valides
current_state = 0        # 0: Éteint, 1: Clignotement lent, 2: Clignotement rapide
previous_state = 0       # Détection de changement d'état

last_irq_time = 0        # Anti-rebond (debounce)
last_blink_time = 0      # Chronomètre pour le clignotement non bloquant
led_status = False

# ==========================================
# 3. Routine d'interruption (IRQ)
# ==========================================
def bp_handler(pin):
    """
    Gestionnaire d'interruption pour le bouton poussoir.
    Incrémente les appuis avec filtrage anti-rebond matériel/logiciel.
    """
    global raw_press_count, last_irq_time
    now = utime.ticks_ms()
    
    # Filtre anti-rebond : 200 ms minimum entre deux appuis
    if utime.ticks_diff(now, last_irq_time) > 200:
        last_irq_time = now
        raw_press_count += 1

# Déclenchement sur front montant (appui du bouton)
bp.irq(trigger=machine.Pin.IRQ_RISING, handler=bp_handler)

# ==========================================
# 4. Fonctions d'animation (Bonus 1)
# ==========================================
def trigger_transition_effect():
    """
    Bonus 1 : Effet visuel lors du changement de vitesse/mode.
    Produit 4 impulsions très rapides pour signaler la bascule.
    """
    for _ in range(4):
        led.value(1)
        utime.sleep_ms(40)
        led.value(0)
        utime.sleep_ms(40)

# ==========================================
# 5. Boucle principale
# ==========================================
while True:
    # Calcul de l'état actuel selon le seuil d'appuis configuré
    # 0 = repos / éteint, 1 = lent (0.5 Hz), 2 = rapide (3 Hz)
    stage_calculated = (raw_press_count // PRESSES_PER_STAGE) % 3
    current_state = stage_calculated

    # Détection de transition -> déclenchement de l'effet bonus
    if current_state != previous_state:
        trigger_transition_effect()
        previous_state = current_state
        last_blink_time = utime.ticks_ms()

    current_time = utime.ticks_ms()

    # --- Mode 1 : Clignotement 0,5 Hz (1s allumée / 1s éteinte) ---
    if current_state == 1:
        if utime.ticks_diff(current_time, last_blink_time) >= 1000:
            last_blink_time = current_time
            led_status = not led_status
            led.value(led_status)

    # --- Mode 2 : Clignotement rapide (~3 Hz, 160 ms alterné) ---
    elif current_state == 2:
        if utime.ticks_diff(current_time, last_blink_time) >= 160:
            last_blink_time = current_time
            led_status = not led_status
            led.value(led_status)

    # --- Mode 0 (3e phase) : Extinction totale ---
    else:
        led.value(0)
        led_status = False

    utime.sleep_ms(10)
