# 💡 Labo GPIO — Contrôle de LED & Interruptions (Raspberry Pi Pico W)

Ce projet présente la mise en œuvre des entrées/sorties numériques (GPIO) et des interruptions matérielles (`IRQ`) sur une carte **Raspberry Pi Pico W** programmée en MicroPython, à l'aide d'un shield d'extension Grove.

---

## 📸 Matériel & Montage

<div align="center">
  <img src="https://github.com/user-attachments/assets/3d80e159-2c27-47de-91f8-b9ac7969ab4d" width="600" alt="Shield d'extension pour Raspberry Pi Pico" />
  <p><em>Shield d'extension avec connecteurs rapides pour Raspberry Pi Pico</em></p>
</div>

### Composants utilisés
* **Microcontrôleur :** Raspberry Pi Pico W (MicroPython)
* **Extension :** Shield d'extension pour Pico (connecteurs standardisés / Grove)
* **Actionneur :** Module LED
* **Capteur :** Module Bouton-poussoir
* **Connectique :** Câbles de liaison 4 broches pour shield

### Tableau de raccordement
| Périphérique | Port Shield | Broche GPIO (MicroPython) | Rôle |
| :--- | :---: | :---: | :--- |
| **Module LED** | `D16` | `GP16` | Sortie numérique (`Pin.OUT`) |
| **Module Bouton** | `D18` | `GP18` | Entrée numérique (`Pin.IN, Pin.PULL_DOWN`) |

---

## 🎯 Objectifs & Consignes

L'objectif est de contrôler l'état et la fréquence de clignotement d'une LED via des appuis successifs sur un bouton-poussoir :

1. **1ᵉʳ appui :** Clignotement lent à une fréquence de **0,5 Hz** (période de 2 s : 1 s allumée, 1 s éteinte).
2. **2ᵉ appui :** Clignotement accéléré (fréquence plus élevée).
3. **3ᵉ appui :** Extinction complète de la LED.
4. **Appui suivant :** Réinitialisation du cycle vers l'état 1.

### 🌟 Bonus implémentés
* **Effet de transition visuel :** Déclenchement d'une brève animation lumineuse (stroboscope rapide) lors du basculement d'un mode à un autre.
* **Seuil d'appuis paramétrable :** Possibilité de configurer le nombre d'appuis nécessaires pour changer d'état.

---

## ⚙️ Architecture & Fonctionnement

### 1. Interruption matérielle (`IRQ`) & Anti-rebond
Au lieu de sonder en continu l'état de la broche dans la boucle principale (*polling*), le bouton est géré par une interruption matérielle :
* Déclenchement configuré sur front montant (`machine.Pin.IRQ_RISING`).
* Filtrage logiciel des rebonds mécaniques (*debouncing*) à l'aide de calculs d'intervalles de temps (`utime.ticks_diff()`).

### 2. Machine à états
Le programme gère une transition d'états cyclique :
* **État 1 :** Mode 0,5 Hz
* **État 2 :** Mode rapide
* **État 0 / 3 :** Arrêt complet

### 3. Effet visuel (`effect`)
Dès qu'une différence entre l'état courant et le nouvel état est détectée, une routine dédiée produit une impulsion visuelle distinctive avant d'appliquer la nouvelle cadence de clignotement.

---

## 📁 Arborescence du dépôt

```text
├── README.md          # Documentation du projet
├── main.py            # Code source principal MicroPython
└── docs/
    └── wiring.png     # Schéma ou photo du montage réel
