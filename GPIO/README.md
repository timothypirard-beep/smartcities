Labo GPIO — Contrôle de LED et Interruptions (Raspberry Pi Pico W)
Introduction
Ce laboratoire a pour objectif d'apprendre à manipuler les ports GPIO d'un Raspberry Pi Pico W à l'aide de MicroPython.

Matériel requis
Microcontrôleur compatible MicroPython (Raspberry Pi Pico W)

Module LED

Module bouton-poussoir

Câbles de liaison (jumpers)

Consignes de base
Brancher la LED et le bouton-poussoir sur les broches GPIO du microcontrôleur.

Développer un script MicroPython répondant aux critères suivants :

1ᵉʳ appui : La LED clignote à une fréquence de 0,5 Hz (période de 2 s).

2ᵉ appui : La LED clignote à une cadence plus rapide.

3ᵉ appui : La LED s'éteint complètement.

Tester et valider le bon fonctionnement du montage.

Fonctionnalités bonus
Effet de transition : Ajout d'un effet visuel intermédiaire lors du passage d'une vitesse de clignotement à une autre.

Seuil d'appuis paramétrable : Modification du nombre d'appuis requis pour déclencher un changement d'état.

Explication de l'implémentation
Détection des appuis (Interruption / IRQ) :

Pour éviter le blocage du programme, la détection du bouton repose sur une interruption matérielle (IRQ). À chaque front montant valide, une fonction de rappel incrémente un compteur d'appuis tout en appliquant un filtrage anti-rebond (debouncing). Le compteur gère le cycle des modes et revient à zéro une fois le cycle terminé.

Gestion des états :

Le programme associe chaque valeur du compteur aux différents états demandés :

État 1 : Clignotement lent (0,5 Hz).

État 2 : Clignotement rapide.

État 3 : Arrêt complet de la LED.

Effet visuel (Bonus) :

Une fonction dédiée (effect) s'exécute dès qu'un changement d'état est détecté, produisant une brève séquence lumineuse avant d'enchaîner sur le mode sélectionné.
