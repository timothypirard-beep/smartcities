# Labo Thermostat — Système de Contrôle de Température (Raspberry Pi Pico W)

Ce laboratoire a pour objectif de concevoir un système de régulation de température avec consigne réglable, affichage dynamique sur écran LCD et alertes sonores et visuelles.

---

## 📸 Matériel & Raccordement

### Composants
* Microcontrôleur Raspberry Pi Pico W
* Shield d'extension Grove
* Module Capteur de température/humidité (DHT11)
* Module Potentiomètre (Consigne)
* Module Écran LCD 1602 (I2C)
* Module Buzzer
* Module LED

### Tableau de câblage
| Composant | Port Shield | Broche Pico | Rôle |
|---|:---:|:---:|---|
| **Potentiomètre** | `A0` | `GP26` | Réglage de la température de consigne (15-35 °C) |
| **Buzzer** | `D16` | `GP16` | Alarme sonore en cas de surchauffe (PWM) |
| **LED** | `D18` | `GP18` | Battement lumineux et clignotement d'alarme (PWM) |
| **Capteur Température** | `D22` | `GP22` | Mesure de la température ambiante (DHT11) |
| **Écran LCD** | `I2C` | `GP8 (SDA) / GP9 (SCL)` | Affichage des températures et de l'alarme |

---
 Consignes
 
1. **Température de consigne :** Le potentiomètre est lu avec l'ADC (`read_u16`) et converti proportionnellement entre **15 °C** et **35 °C**.
2. **Mesure ambiante :** La température mesurée par le capteur est actualisée toutes les secondes environ.
3. **Affichage standard :**
   * Ligne 1 : `Set: XXC`
   * Ligne 2 : `Ambient: XXC`
4. **Comportement selon les seuils :**
   * **Température ambiante <= Consigne :** Tout est au repos (LED éteinte, buzzer muet).
   * **Température ambiante > Consigne :** La LED bat doucement à une fréquence de 0,5 Hz.
   * **Température ambiante >= Consigne + 3°C :** Le buzzer retentit, la LED clignote rapidement et le message `ALARM` apparaît à l'écran.

### 🌟 Bonus intégrés
* **Battement progressif (Dimmer) :** Utilisation de la PWM sur la LED pour créer un effet de respiration lumineuse fluide au lieu d'un clignotement sec.
* **Alarme animée :** Le mot `ALARM` clignote et se déplace sur la première ligne de l'écran LCD pour attirer l'attention lors du dépassement critique.

---

## ⚙️ Explication du fonctionnement

* **Conversion de consigne :**  
  La formule `15 + (val_pot / 65535) * 20` permet d'étaler les 65536 valeurs de l'ADC sur les 20 degrés de plage demandés.

* **Non-blocage du capteur :**  
  `utime.ticks_diff()` est utilisé pour n'interroger le DHT11 qu'une fois par seconde, évitant ainsi de surcharger la communication du capteur tout en gardant l'écran réactif.

* **Effet de gradation (PWM) :**  
  En faisant monter puis descendre `duty_u16()` par paliers de 100 ms, la LED produit un battement continu à environ 0,5 Hz (1 s de montée, 1 s de descente).

---

## 🚀 Utilisation

1. Brancher les modules sur leurs ports respectifs sur le shield.
2. Ouvrir le dossier dans VS Code.
3. Téléverser le fichier `main.py` sur la carte Pico.
4. Tourner le potentiomètre pour faire varier la consigne sous la température de la pièce pour déclencher le battement LED, puis chauffer le capteur avec le doigt pour déclencher l'alarme et le buzzer.
