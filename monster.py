# Code mit KI für besseres Code Verständnis auskommentiert.
# Importiere die nötigen Funktionen: 'random' für Zufallszahlen (z.B. für Würfelwürfe) und 'time' zum Pausieren des Spiels.
import random
import time

# --- SPIELSTART UND EINLEITUNG ---

print("~" * 50)
print("DIE LETZTE HOFFNUNG") # Der Titel des Spiels
print("~" * 50)

# Geschichte
time.sleep(1) # Kurze Pause, um den Text langsam erscheinen zu lassen
print("\nDie Nacht war dunkel, als die Schreie aus dem Dorf drangen.")
print("Sie kamen wieder. Die Schatten der alten Welt.")
time.sleep(2) # Längere Pause

# Frage nach dem Namen des Spielers. Wenn nichts eingegeben wird, wird "Elias" als Standardname verwendet.
name = input("\nWie heißt du, Kind dieser Erde? ") or "Elias"

print(f"\n{name}...")
time.sleep(1)
print("Dein Vater gab mir dies, bevor er fiel.")
time.sleep(1)
print("'Wenn mein Kind groß ist', sagte er, 'gib ihm diese Klinge.'")
time.sleep(2)

# --- CHARAKTER-WERTE FESTLEGEN ---

print("\n" + "-" * 40)
print("⚔️  Das Erbe deines Vaters ⚔️")
print("-" * 40)
time.sleep(1)

leben = 100 # Der aktuelle Gesundheitswert des Spielers (Startwert)
angriff = 18 # Die Stärke des Schwertes und damit der verursachte Grundschaden
trank = 1 # Die Anzahl der Heiltränke, die der Spieler besitzt

print(f"Leben: {leben}")
print(f"Schwert des Vaters: {angriff} Stärke")
print(f"Letzter Trank deiner Mutter: {trank}")
time.sleep(2)

# --- MONSTER-DEFINITION ---

# Eine Liste von Gegnern (Monstern). Jedes Monster ist ein "Wörterbuch" mit Name, Leben, Angriff und einer kleinen Geschichte.
monster = [
    {"name": "Der verfluchte Wächter", "leben": 40, "angriff": 10, 
     "geschichte": "Einst ein Dorfältester, jetzt nur noch leerer Blick"},
    {"name": "Die weinende Mutter", "leben": 60, "angriff": 8,
     "geschichte": "Ihr Kind wurde genommen. Ihr Schmerz macht sie wild."},
    {"name": "Der gebrochene Schmied", "leben": 80, "angriff": 15,
     "geschichte": "Er schmiedete einst dein Schwert. Jetzt schmiedet er nur noch Tod."}
]

print(f"\nVor dir stehen {len(monster)} Gestalten...") # Zeigt an, wie viele Monster es gibt.
print("Sie waren alle einmal Menschen !.")
time.sleep(2)

# --- SPIEL-STATUS-VARIABLEN ---

runde = 1 # Zählt die aktuelle Spielrunde
besiegt = 0 # Zählt, wie viele Monster bereits besiegt wurden

# --- HAUPTSPIELSCHLEIFE ---

# Die Schleife läuft, solange der Spieler noch am Leben ist (leben > 0) UND noch nicht alle Monster besiegt wurden.
while leben > 0 and besiegt < len(monster):
    print(f"\n{'°' * 30}")
    print(f"Begegnung {runde}")
    print(f"{'°' * 30}")
    
    # Zeige die aktuellen Werte des Spielers an
    print(f"\n{name}: ❤️  {leben}/100")
    if trank > 0:
        print(f"⚗️  Mutters Trank: {trank}")
    
    # Zeige die verfügbaren Monster zur Auswahl
    print(f"\nWer steht vor dir?")
    for i, m in enumerate(monster): # Geht durch die Monster-Liste
        if m["leben"] > 0: # Zeigt nur Monster, die noch nicht besiegt sind
            print(f"{i+1}. {m['name']} ({m['leben']} ❤️)")
    
    try:
        # Der Spieler wählt ein Monster aus (Zahl eingeben)
        wahl = int(input("\nDeine Wahl: ")) - 1 # -1, weil die Liste bei 0 anfängt
        m = monster[wahl] # Das ausgewählte Monster
        
        # Überprüfung, ob das Monster bereits tot ist
        if m["leben"] <= 0:
            print("Dieser Geist fand bereits Frieden.")
            continue # Springe zum Anfang der Schleife
        
        # Details zum Kampfgegner
        print(f"\nDu siehst {m['name']}...")
        print(m["geschichte"])
        time.sleep(2)
        
        # --- ANGRIFF DES SPIELERS ---
        
        print("\n🎲 Du würfelst deinen Mut...")
        time.sleep(1)
        würfel = random.randint(1, 20) # Simuliert einen W20-Würfelwurf
        
        # Berechnet den Schaden basierend auf dem Würfelwurf
        if würfel == 20:
            schaden = angriff * 3 # Dreifacher Schaden bei einer 20 (kritischer Treffer)
            print("✨ VOLLTREFFER! Vaters Geist führt deine Hand!")
        elif würfel >= 15:
            schaden = angriff * 2 # Doppelter Schaden
            print("⭐ Stark! Du erinnerst dich an Vaters Lehren.")
        elif würfel >= 5:
            schaden = angriff # Normaler Schaden
            print("✓ Ein klarer Schlag.")
        else:
            schaden = angriff // 2 # Halber Schaden (schwacher Schlag)
            print("✗ Deine Hand zittert...")
        
        # Schaden wird vom Leben des Monsters abgezogen
        m["leben"] -= schaden
        print(f"Du fügst {schaden} Schaden zu.")
        time.sleep(1)
        
        # --- MONSTER BESIEGT? ---
        
        if m["leben"] <= 0:
            m["leben"] = 0 # Sorgt dafür, dass Leben nicht negativ wird
            besiegt += 1 # Zähler für besiegte Monster erhöhen
            print(f"\n☮️  {m['name']} wird ruhig...")
            print("Ein letztes Lächeln, dann löst er sich in Licht auf.")
            
            # 40% Chance, einen Trank als Belohnung zu finden
            if random.random() < 0.4:
                trank += 1
                print("💧 Eine Träne der Erlösung fällt. Du fängst sie in Vaters Flasche.")
            time.sleep(2)
            
            # Prüfen, ob dies das letzte Monster war
            if besiegt == len(monster):
                break
        else:
            # --- MONSTER GREIFT AN ---
            
            print(f"\n{m['name']} wehrt sich...")
            time.sleep(1)
            
            # Spezielle Regel für die "Weinende Mutter" (sie macht weniger Schaden)
            if m["name"] == "Die weinende Mutter":
                schaden = m["angriff"] // 2
                print("Ihr Schlag ist voller Trauer, nicht Zorn.")
            else:
                schaden = m["angriff"] # Normaler Schaden des Monsters
                print("Ein wilder Angriff!")
            
            # Schaden wird vom Leben des Spielers abgezogen
            leben -= schaden
            print(f"Du verlierst {schaden} Leben.")
            
            # Hinweis, wenn der Spieler im kritischen Bereich ist und Tränke hat
            if leben <= 30 and trank > 0:
                print("\n💭 Du spürst Mutters Stimme: 'Trink, mein Kind...'")
    
        # --- TRANK VERWENDEN? ---
        
        # Der Spieler wird gefragt, ob er einen Trank benutzen will, wenn das Leben unter 50 fällt
        if leben < 50 and trank > 0:
            benutzen = input("\nMutters Trank benutzen? (j/n): ").lower()
            if benutzen == 'j':
                trank -= 1 # Trank verbrauchen
                heilung = random.randint(30, 50) # Zufällige Heilung zwischen 30 und 50
                leben = min(leben + heilung, 100) # Leben heilen, aber maximal 100
                print(f"💖 Du trinkst... Die Erinnerung wärmt dich. (+{heilung} Leben)")
                print(f"Du hörst ihre Stimme: 'Ich bin immer bei dir, {name}.'")
                time.sleep(2)
        
        runde += 1 # Runde erhöhen
        
    except:
        # Fehlerbehandlung, falls der Spieler z.B. Text statt einer Zahl eingibt
        print("Deine Gedanken sind wirr...")

# --- ENDE DES SPIELS ---

print(f"\n{'=' * 40}")

if leben <= 0:
    # Niederlage
    print("💀 Du sinkst zu Boden...")
    print("Vaters Stimme: 'Du hast getan, was du konntest.'")
    print("Mutter: 'Komm nach Hause, mein Kind...'")
else:
    # Sieg (alle Monster besiegt)
    print("🌈 Das letzte Licht verschwindet.")
    print("Die Gestalten sind frei.")
    print(f"\n{name} steht allein in der Stille.")
    print("Vaters Stimme: 'Ich bin stolz auf dich.'")
    print("Mutter: 'Unser Kind ist erwachsen geworden.'")
    print(f"\nDu bewahrst die Flasche mit {trank} Tränen der Erlösung.")
    print("Für alle, die noch kommen mögen...")

print(f"\nDeine Reise endet hier.")

# --- ENDE DES CODES ---