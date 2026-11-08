# 🕒 Horloge Connectée avec Servomoteur (Raspberry Pi Pico W)

Ce projet permet de fabriquer une horloge connectée en MicroPython avec un **Raspberry Pi Pico W** et un **servomoteur standard (0° à 180°)**[cite: 1]. L'heure est synchronisée via internet avec le protocole NTP[cite: 1], puis le servomoteur se positionne automatiquement sur le cadran[cite: 1, 3].

---

## 📸 Matériel & Câblage

### Composants
* Raspberry Pi Pico W[cite: 1]
* Shield Grove pour Pico (ou platine d'essais)
* Servomoteur 9g (SG90 ou Grove Servo)[cite: 1]
* Connexion Wi-Fi 2.4 GHz[cite: 1]

### Tableau de raccordement
| Composant | Fil / Port | Broche Pico | Rôle |
|---|:---:|:---:|---|
| **Servo (Signal)** | Jaune / Blanc | `GP16` (D16) | Signal PWM (50 Hz) |
| **Servo (VCC)** | Rouge | `VBUS` (Pin 40) ou `5V` | Alimentation moteur |
| **Servo (GND)** | Marron / Noir | `GND` | Masse commune |

---

## 🎯 Consignes & Logique du Cadran

Le servomoteur a une course mécanique limitée entre **0° et 180°**[cite: 1]. Le cadran de 12 heures est adapté à cette plage[cite: 1] :
* **12h00** $\rightarrow$ **0°**[cite: 1]
* **6h00** $\rightarrow$ **90°**[cite: 1]
* Chaque heure correspond à un écart de **15°** ($90° / 6 = 15°$).
* Les minutes ajoutent une progression fluide de **0,25° par minute** ($15° / 60$).

---

## ⚙️ Fonctionnement du programme

1. **Connexion Wi-Fi :** La carte se connecte au réseau local via la bibliothèque `network`[cite: 1].
2. **Synchronisation NTP :** L'heure UTC actuelle est récupérée depuis les serveurs de temps grâce à `ntptime.settime()`[cite: 1].
3. **Calcul de l'angle :** Le script prend l'heure actuelle modulo 12 et calcule l'angle correspondant sur 180°[cite: 1, 3].
4. **Commande PWM :** L'angle est transformé en rapport cyclique (`duty_u16`) sous une fréquence de 50 Hz pour piloter le moteur[cite: 3].
5. **Mise à jour :** L'aiguille réactualise sa position toutes les 30 secondes[cite: 2].

---
