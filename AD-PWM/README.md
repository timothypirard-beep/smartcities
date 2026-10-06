Labo PWM & ADC — Buzzer, Potentiomètre et LED (Raspberry Pi Pico W)

Ce laboratoire a pour but d'apprendre à utiliser un potentiomètre (entrée analogique ADC), un buzzer passif (sortie PWM), une LED et un bouton-poussoir sur un **Raspberry Pi Pico W** avec le shield Grove.

---

## 📸 Matériel & Câblage

### Composants
* Raspberry Pi Pico W
* Shield d'extension Grove
* Module Potentiomètre
* Module Buzzer
* Module LED
* Module Bouton-poussoir

### Tableau de raccordement
| Composant | Port Shield | Broche Pico | Rôle |
|---|:---:|:---:|---|
| **Potentiomètre** | `A0` | `GP26` | Contrôle du volume (ADC) |
| **Buzzer** | `D16` | `GP16` | Sortie du bip sonore (PWM) |
| **LED** | `D18` | `GP18` | Clignote au rythme du son |
| **Bouton-poussoir** | `D20` | `GP20` | Change de son via interruption (`IRQ`) |

---

## 🎯 Consignes & Fonctionnalités

### Consignes de base
1. Le buzzer produit un bip en boucle régulière.
2. La rotation du potentiomètre ajuste directement le volume sonore.
3. À fond vers la gauche, le son est complètement coupé.

### Bonus intégrés
* **Bouton-poussoir (Changement de son) :** Un appui sur le bouton modifie la fréquence et la vitesse du bip (Mode 1 : son grave et lent / Mode 2 : son aigu et rapide).
* **LED synchronisée :** La LED s'allume au moment exact où le buzzer sonne et s'éteint pendant les silences.

---

## ⚙️ Explication simple du fonctionnement

* **Volume (Potentiomètre) :**  
  On lit la valeur de l'entrée analogique avec `pot.read_u16()` (de 0 à 65535). On divise cette valeur par deux pour l'envoyer dans `buzzer.duty_u16()`. Plus le rapport cyclique est haut, plus le son est fort. En dessous d'un seuil minimum, le volume est mis à 0 pour couper le bruit résiduel.

* **Interruption (Bouton) :**  
  Le bouton utilise `bp.irq(...)` sur front montant pour basculer la variable `sound_mode` entre 1 et 2, avec un petit délai anti-rebond pour éviter les faux déclenchements.

* **Rythme & LED :**  
  Le signal sonore et la LED sont activés en même temps pendant le délai `t_on`, puis éteints tous les deux pendant le délai `t_off`.

---

## 🚀 Utilisation

1. Brancher les 4 modules sur leurs ports respectifs sur le shield.
2. Ouvrir le projet dans **Thonny**.
3. Lancer le script `main.py`.
4. Tourner le potentiomètre pour tester le volume et appuyer sur le bouton pour changer le son.
