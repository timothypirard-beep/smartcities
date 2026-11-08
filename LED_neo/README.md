# 🎵 Contrôle d'une LED RGB (WS2812B) au rythme de la musique

Ce projet consiste à programmer un microcontrôleur **Raspberry Pi Pico W** en MicroPython pour synchroniser les changements de couleur d'une LED RGB adressable (WS2812B / NeoPixel) avec les battements de la musique captés par un microphone.

---

## 📸 Matériel & Câblage

### Composants utilisés
* Raspberry Pi Pico W
* Shield Grove pour Pico
* Module Microphone analogique Grove
* Module LED RGB WS2812B (NeoPixel)
* Câbles Grove

### Tableau des connexions
| Composant | Port Shield | Broche Pico | Rôle |
|---|:---:|:---:|---|
| **Microphone** | `A0` | `GP26` (ADC0) | Lecture du niveau sonore |
| **LED WS2812B** | `D16` | `GP16` | Contrôle numérique de la LED (Signal DIN) |

---

## 🎯 Consignes & Fonctionnement

1. **Échantillonnage audio :** Le microphone capte le signal sonore ambiant sur l'entrée analogique `GP26`.
2. **Détection des battements :** Le script calcule l'écart d'amplitude (crête à crête) sur une série d'échantillons rapides pour identifier les pics d'énergie correspondant aux coups de basse ou aux temps forts.
3. **Changement de couleur :** Dès qu'un pic dépasse le seuil défini, la LED WS2812B prend une couleur aléatoire (rouge, vert, bleu générés entre 0 et 255).
4. **Filtre anti-rebond :** Un délai minimal de 250 ms entre deux déclenchements évite les faux positifs et stabilise la synchronisation sur le rythme musical.

---

## 🚀 Utilisation

1. Brancher le microphone sur le connecteur `A0` et la LED sur `D16`.
2. Ouvrir le dossier du projet dans VS Code.
3. Téléverser le fichier `main.py` sur la carte Raspberry Pi Pico W.
4. Lancer une musique : la LED change de couleur instantanément à chaque temps fort.
