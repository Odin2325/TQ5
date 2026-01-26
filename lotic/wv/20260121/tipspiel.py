import random

def ratespiel():
    zufallszahl = random.randint(1, 100)
    geraten = 0
    leben = 10
    versuche = 0

    while zufallszahl != geraten:
        print(f'Du hast noch {leben-versuche} Leben übrig')
        geraten = int(input('Bitte gib eine Zahl von 1-100 ein: '))
        versuche += 1
        if geraten < zufallszahl:
            print('Deine Zahl ist zu klein')
        if geraten > zufallszahl:
            print('Deine Zahl ist zu groß')
        if versuche > 9:
            break

    if zufallszahl != geraten:
        print('Du hast keine Leben mehr übrig. GAME OVER!')
    else:
        print(f'Richtig geraten! Du hast {versuche} Versuche gebraucht und noch {leben-versuche} Leben übrig.')


while True:
    ratespiel()
    nochmal = input('Möchtest du nochmal spielen? (y)')
    if nochmal != 'y':
        break

