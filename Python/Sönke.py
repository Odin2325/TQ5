import time
import threading
import random

class Ted:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.zufrieden = True
        self.unglücklich = False
        self.vitalwert = 50
        self.punkte = 0
        self.running = True

    def tick(self):
        while self.running:
            time.sleep(60)
            self.hunger += 1
            self.random_behavior()
            self.evaluate_state()
            self.status()

    def random_behavior(self):
        verhalten = random.choice(["schnurren", "aggressiv", "sabbern", "warten"])
        if verhalten == "schnurren":
            self.schnurren()
        elif verhalten == "aggressiv":
            self.aggressiv()
        elif verhalten == "sabbern":
            self.sabber()
        else:
            print(f"{self.name} steht ratlos herum und wartet auf Aufmerksamkeit... 😿")

    def evaluate_state(self):
        if self.hunger > 7:
            self.zufrieden = False
            self.unglücklich = True
        elif self.hunger > 4:
            self.zufrieden = False
            self.unglücklich = False
        else:
            self.zufrieden = True
            self.unglücklich = False

    def essen(self, menge=2):
        print(f"{self.name} isst {menge} Portion(en)...")
        self.hunger = max(0, self.hunger - menge)
        self.zufrieden = True
        self.unglücklich = False
        self.sabber()

    def ruhe(self):
        print(f"{self.name} legt sich hin und ruht sich aus...")
        self.zufrieden = True
        self.unglücklich = False
        self.schnurren()

    def streicheln(self):
        print(f"Du klopfst {self.name} freundlich auf die Schulter. 🥰")
        self.zufrieden = True
        self.unglücklich = False
        self.schnurren()

    def treten(self):
        print(f"Du gibst {self.name} einen Tritt... 😡")
        self.zufrieden = False
        self.unglücklich = True
        print(f"{self.name} macht ein brrr-bähh-Geräusch und humpelt beleidigt davon! 😾")

    def deutsch_sprechen(self):
        print(f"Du versuchst, mit {self.name} korrektes Deutsch zu sprechen...")
        print(f"{self.name} schaut dich verwirrt an und sagt: „hähh?“ 🤨")
        print(f"{self.name} läuft verwirrt mit seinen Füßen im Kreis, schnüffelt an der Wand und stolpert über einen Hocker... 🌀🦶")

    def sabber(self):
        print(f"{self.name} sabbert glücklich. 💧")

    def schnurren(self):
        print(f"{self.name} macht ein schnurr-Geräusch. 😸")

    def aggressiv(self):
        print(f"{self.name} wird laut und fuchtelt wild mit den Armen! 😾")

    def status(self):
        zustand = "schnurr 😸" if self.zufrieden else "brrr-bähh 😾" if self.unglücklich else "murr 😐"
        print(f"\nStatus: Hunger {self.hunger}/10 | Zufrieden: {'Ja' if self.zufrieden else 'Nein'} | Unglücklich: {'Ja' if self.unglücklich else 'Nein'} | Geräusch: {zustand}")
        print(f"Vitalwert: {self.vitalwert}/100 | Trainierte Teds: {self.punkte}")

        if self.vitalwert == 100 and self.zufrieden and not self.unglücklich and self.hunger == 0:
            print(f"\n🎉 {self.name} ist in einem perfekten Zustand! Er wird verschachert... 💸")
            self.punkte += 1
            print(f"🏅 Du hast jetzt {self.punkte} trainierte Ted(s) gesammelt!")
            self._neuer_ted()

    def _neuer_ted(self):
        print("Ein neuer Ted wird geboren... 🐣")
        self.name = f"TED #{self.punkte + 1}"
        self.hunger = 5
        self.zufrieden = True
        self.unglücklich = False
        self.vitalwert = 50

    def stop(self):
        self.running = False

    def drogen_blackjack(self):
        print(f"\n{self.name} betritt den dunklen Nebenraum in dem Du bereit stehst ... 🕶️")
        deck = self._generate_drogen_deck()
        hand = []
        total = 0

        def karte_ziehen():
            karte = deck.pop()
            hand.append(karte)
            wert = self._kartenwert(karte)
            bezeichnung = karte.replace("Ass", "Smart").replace("Bube", "Coolness").replace("Dame", "Sextraum").replace("König", "Geldrausch")
            if any(x in bezeichnung for x in ["Smart", "Coolness", "Sextraum", "Geldrausch"]):
                print(f"{self.name} bekommt: {bezeichnung} ({wert} Drugpoints)")
            else:
                print(f"{self.name} bekommt: {bezeichnung.replace(' ', ' Stärke ', 1)} ({wert} Drugpoints)")
            return wert

        total += karte_ziehen()
        total += karte_ziehen()

        while True:
            print(f"Aktueller Drogenwert: {total}")
            if total >= 23:
                print(f"\n{self.name} bölkt! 💥 Er liegt bewusstlos beim Barbierpfuscher auf der Intensivstation... 🏥")
                for i in range(60, 0, -10):
                    print(f"Reanimation läuft... ({i} Sekunden verbleiben)")
                    time.sleep(10)
                print("Ted wurde reanimiert. Bitte geh pfleglicher mit ihm um. 😿")
                self.vitalwert = 1
                self.zufrieden = False
                self.unglücklich = True
                break
            elif total > 20:
                print(f"\n{self.name} tanzt fröhlich herum! 🕺 Seine Vitalwerte steigen! 💓")
                self.vitalwert = min(100, self.vitalwert + 20)
                self.zufrieden = True
                self.unglücklich = False
                break
            else:
                antwort = input("Noch eine Dosis dazu? (j/n): ").strip().lower()
                if antwort == "j":
                    total += karte_ziehen()
                elif antwort == "n":
                    print(f"\n{self.name} bleibt bei {total} Punkten. Er ist stone und will mehr... 😵‍💫")
                    self.zufrieden = False
                    self.unglücklich = False
                    break
                else:
                    print("Ungültige Eingabe.")

    def _generate_drogen_deck(self):
        farben = {
            "Herz": "Amphetaminchen",
            "Karo": "Kokain",
            "Pik": "Ekstatik",
            "Kreuz": "MaryJane"
        }
        werte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]
        deck = [f"{farben[f]} {w}" for f in farben for w in werte]
        random.shuffle(deck)
        return deck

    def _kartenwert(self, karte):
        if "Ass" in karte:
            return random.choice([1, 11])
        elif "Bube" in karte:
            return 10
        elif "Dame" in karte:
            return 10
        elif "König" in karte:
            return 10
        else:
            return int(karte.split()[-1])

# Hauptprogramm
ted = Ted("TED #1")

thread = threading.Thread(target=ted.tick)
thread.daemon = True
thread.start()

try:
    while True:
        ted.status()
        print("Aktionen: [1] Füttern  [2] Ruhe  [3] Streicheln  [4] Treten  [5] Deutsch reden  [6] Drogen geben  [q] Beenden  [Enter] nichts tun")
        aktion = input("Aktion wählen: ").strip()

        if aktion == "1":
            ted.essen()
        elif aktion == "2":
            ted.ruhe()
        elif aktion == "3":
            ted.streicheln()
        elif aktion == "4":
            ted.treten()
        elif aktion == "5":
            ted.deutsch_sprechen()
        elif aktion == "6":
            ted.drogen_blackjack()
        elif aktion.lower() == "q":
            ted.stop()
            print("Simulation beendet.")
            break
        elif aktion == "":
            print(f"{ted.name} schaut dich erwartungsvoll an... 🐾")
            ted.random_behavior()
        else:
            print("Ungültige Eingabe.")
except KeyboardInterrupt:
    ted.stop()
    print("\nSimulation durch Tastendruck beendet.")