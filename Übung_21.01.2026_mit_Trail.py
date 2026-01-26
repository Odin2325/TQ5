'''
entscheidung = input('Nächste Kunde? (ja/nein): ')

while True:
    alter = int(input('Bitte gib dein Alter ein: '))

    if alter < 18:
        print('Kein Zutritt')
    elif alter <= 65:
        print('Willkommen!')
    else:
        print('Eintritt Frei!')
    if entscheidung == 'nein':
        print('Schönen Feierabend!')
        break
    print('Nächste Kunde bitte!\n')
'''
'''
while True:
    alter = int(input('Alter bitte: '))
    if alter < 18:
        print('Unter 18! "Kein Zutritt!"')
    elif alter <= 65:
        print("Willkommen!")
    else:
        print('"Eintritt frei!"')
 
    # Hier kommt die Logik für den nächsten Kunden:
    print('\n--- Der nächste bitte! ---')
    antwort = input('Soll der nächste Kunde eintreten? (ja/nein): ').lower()
    if antwort == 'nein':
        print("Türsteher macht Feierabend.")
        break  # Beendet die while-Schleife
    # Wenn die Antwort nicht 'nein' ist, springt Python automatisch 
    # wieder an den Anfang der while-Schleife.
    '''
'''
while True:
    # 1. Alter abfragen
    alter_input = input('Alter Bitte! ')
    alter = int(alter_input)

    # 2. Entscheidung treffen
    if alter < 18:
        print('Unter 18! "Kein Zutritt!"')
    elif alter <= 65:
        print("Willkommen!")
    else:
        print('"Eintritt frei!"')

    # 3. Die Sperre: Hier geht es erst weiter, wenn "nächster" getippt wird
    print('\n--- Der Kunde wird bearbeitet... ---')

    bereit_fuer_naechsten = False
    while not bereit_fuer_naechsten:
        kommando = input('Gib "weiter" ein, um den nächsten Kunden zu rufen: ').lower()

        if kommando == "weiter":
            print("Okay, der nächste bitte!\n")
            bereit_fuer_naechsten = True  # Bricht die innere Schleife ab
        elif kommando == "feierabend":
            print("Club geschlossen.")
            exit() # Beendet das komplette Programm
        else:
            print(f'Du hast "{kommando}" gesagt, aber ich warte auf "weiter"!')
'''

