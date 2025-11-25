#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Farmingspiel.py
Ein komplexes, terminal-basiertes Farmspiel, das mit echtem Python-Code gesteuert wird.
Features:
- 20x20 Acker mit ASCII-Darstellung und Farmhaus rechts
- Mehrzeilige Eingaben für echten Python-Code (Schleifen, Funktionen)
- Hilfesystem, Status, ausführliche Feedback-Ausgaben
- Mehrere Saatarten, Wachstum, Wetter, Schädlingsbefall
- Inventar, Lager, Lieferungen, Händler
- Aufgaben/Quests, Tutorial
- Speichern/Laden, Logbuch
- Hindernisse, Wegfindung (einfach), Checkpoints
- Konfigurierbare Optionen
"""

import sys
import json
import time
import random
from collections import deque
from typing import List, Dict, Tuple, Optional

# ------------------------------
# Globale Konfiguration
# ------------------------------

FIELD_W, FIELD_H = 20, 20  # Größe des Ackers

# Feldzustände: 0=leer, 1=gepflügt, 2=gesät, 3=reif, 4=geerntet, 5=Hindernis, 6=Unkraut, 7=krank
STATE_CH = {
    0: '.',   # leer
    1: '=',   # gepflügt
    2: '+',   # gesät
    3: '#',   # reif
    4: '*',   # geerntet / Stoppel
    5: 'X',   # Hindernis (Stein)
    6: 'u',   # Unkraut
    7: 'k',   # Krankheit / Schädlingsbefall
}

# ASCII-Farmhaus rechts neben dem Feld
HOUSE_ART = [
    "    HHHHHHHH    ",
    "   H        H   ",
    "   H        H   ",
    "   H   __   H   ",
    "   H  |DF|  H   ",
    "   H  |  |  H   ",
] + ["   H        H   "] * 13 + ["    HHHHHHHH    "]

DOOR_ROW = 4
DELIVERY_X = FIELD_W - 1
DELIVERY_Y = DOOR_ROW

# Wettertypen
WEATHER_TYPES = ["klar", "bewölkt", "regen", "sturm", "heiß"]

# Saatarten mit Eigenschaften
SEED_TYPES = {
    "weizen": {"grow_steps": 3, "yield": 1, "resistance": 0.2, "price": 2},
    "mais": {"grow_steps": 4, "yield": 2, "resistance": 0.3, "price": 3},
    "kartoffel": {"grow_steps": 5, "yield": 3, "resistance": 0.4, "price": 4},
    "roggen": {"grow_steps": 3, "yield": 1, "resistance": 0.25, "price": 2},
    "gerste": {"grow_steps": 3, "yield": 1, "resistance": 0.25, "price": 2},
}

# Händlerpreise (Verkauf)
SELL_PRICES = {
    "weizen": 5,
    "mais": 7,
    "kartoffel": 8,
    "roggen": 5,
    "gerste": 5,
}

# Optionen
OPTIONS = {
    "show_grid": True,
    "animate_wait": False,
    "max_log_entries": 200,
    "auto_render": True,
    "weather_variability": 0.5,
    "pest_base_chance": 0.03,
    "weed_base_chance": 0.05,
    "disease_spread_chance": 0.05,
    "pathfinding_max_steps": 200,
}

# ------------------------------
# Hilfsfunktionen
# ------------------------------

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def manhattan(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# ------------------------------
# Inventar, Lager, Log
# ------------------------------

class Inventory:
    def __init__(self):
        self.items: Dict[str, int] = {}  # {"weizen_saat": 12, "kartoffel": 3, ...}

    def add(self, name: str, qty: int):
        if qty <= 0:
            return
        self.items[name] = self.items.get(name, 0) + qty

    def remove(self, name: str, qty: int) -> bool:
        if self.items.get(name, 0) >= qty and qty > 0:
            self.items[name] -= qty
            if self.items[name] == 0:
                del self.items[name]
            return True
        return False

    def has(self, name: str, qty: int = 1) -> bool:
        return self.items.get(name, 0) >= qty

    def list(self) -> List[Tuple[str, int]]:
        return sorted(self.items.items())

class Logbook:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.entries: deque = deque(maxlen=capacity)

    def add(self, message: str):
        ts = time.strftime("%H:%M:%S")
        self.entries.append(f"[{ts}] {message}")

    def dump(self) -> str:
        return "\n".join(self.entries)

# ------------------------------
# Robot
# ------------------------------

class Robot:
    def __init__(self):
        self.x, self.y = 0, 0
        self.bag = 0
        self.total_harvest = 0
        self.energy = 100
        self.level = 1
        self.exp = 0
        self.tool_quality = 1.0  # beeinflusst Erfolgsraten

    def add_exp(self, amount: int):
        self.exp += amount
        while self.exp >= 100:
            self.exp -= 100
            self.level += 1
            self.tool_quality += 0.1

# ------------------------------
# Feldzelle
# ------------------------------

class Cell:
    def __init__(self):
        self.state = 0  # siehe STATE_CH
        self.growth = 0
        self.seed_type: Optional[str] = None
        self.moisture = 0.5
        self.pest = False
        self.weed = False
        self.diseased = False

    def reset(self):
        self.state = 0
        self.growth = 0
        self.seed_type = None
        self.moisture = 0.5
        self.pest = False
        self.weed = False
        self.diseased = False

# ------------------------------
# Quests
# ------------------------------

class Quest:
    def __init__(self, name: str, description: str, goals: Dict[str, int], reward_money: int, reward_exp: int):
        self.name = name
        self.description = description
        self.goals = goals  # z.B. {"deliver_weizen": 5}
        self.progress: Dict[str, int] = {k: 0 for k in goals.keys()}
        self.completed = False
        self.reward_money = reward_money
        self.reward_exp = reward_exp

    def update_progress(self, key: str, amount: int):
        if key in self.progress:
            self.progress[key] += amount
            if self.progress[key] >= self.goals[key]:
                self.progress[key] = self.goals[key]
        self.completed = all(self.progress[k] >= self.goals[k] for k in self.goals)

    def summary(self) -> str:
        lines = [f"Quest: {self.name}", self.description, "Ziele:"]
        for k in self.goals:
            lines.append(f"  - {k}: {self.progress[k]}/{self.goals[k]}")
        lines.append(f"Belohnung: {self.reward_money} Geld, {self.reward_exp} EXP")
        lines.append(f"Status: {'abgeschlossen' if self.completed else 'aktiv'}")
        return "\n".join(lines)

# ------------------------------
# Spielzustand speichern/laden
# ------------------------------

class SaveData:
    def __init__(self):
        self.money = 50
        self.day = 1
        self.weather = "klar"

    def to_dict(self) -> Dict:
        return {"money": self.money, "day": self.day, "weather": self.weather}

    @staticmethod
    def from_dict(d: Dict) -> 'SaveData':
        s = SaveData()
        s.money = d.get("money", 50)
        s.day = d.get("day", 1)
        s.weather = d.get("weather", "klar")
        return s

# ------------------------------
# FarmGame
# ------------------------------

class FarmGame:
    def __init__(self):
        self.w, self.h = FIELD_W, FIELD_H
        self.field: List[List[Cell]] = [[Cell() for _ in range(self.w)] for _ in range(self.h)]
        self.robot = Robot()
        self.message = "Willkommen! Tippe game.help() für Befehle. Leerzeile beendet Eingabeblock."
        self.inventory = Inventory()
        self.storage = Inventory()
        self.log = Logbook(OPTIONS["max_log_entries"])
        self.save = SaveData()
        self.weather = "klar"
        self.weather_history: deque = deque(maxlen=5)
        self.quests: List[Quest] = []
        self.last_help_text = ""
        self.started = False

        # Setup: Hindernisse, Startinventar, Beispiel-Quests
        self._place_obstacles()
        self._seed_start_inventory()
        self._setup_quests()

    # --------------------------
    # Setup
    # --------------------------
    def _place_obstacles(self):
        random.seed(42)
        for _ in range(40):
            x = random.randint(0, self.w - 2)  # nicht ganz rechter Rand
            y = random.randint(0, self.h - 1)
            if (x, y) != (0, 0) and y != DELIVERY_Y:
                self.field[y][x].state = 5  # Hindernis

    def _seed_start_inventory(self):
        self.inventory.add("weizen_saat", 10)
        self.inventory.add("mais_saat", 6)
        self.inventory.add("kartoffel_saat", 4)
        self.storage.add("dünger", 5)
        self.storage.add("pestizid", 2)

    def _setup_quests(self):
        q1 = Quest(
            "Erste Lieferung",
            "Liefere 5 Einheiten Weizen an die Tür.",
            {"deliver_weizen": 5},
            reward_money=30,
            reward_exp=50
        )
        q2 = Quest(
            "Kartoffel-König",
            "Ernte 6 Einheiten Kartoffeln.",
            {"harvest_kartoffel": 6},
            reward_money=40,
            reward_exp=60
        )
        self.quests = [q1, q2]

    # --------------------------
    # Hilfesystem
    # --------------------------
    def help(self):
        text = """
================== HILFE ==================
Echte Python-Befehle (mehrzeilig, mit Leerzeile abschließen):

Bewegung:
    game.move('N'|'S'|'E'|'W')
    game.go_to(x, y)                   -> einfache Wegfindung

Feldarbeit:
    game.plow()                        -> Pflügen (=)
    game.sow('weizen'|'mais'|'kartoffel'|'roggen'|'gerste') -> Säen (+)
    game.water()                       -> Bewässern (erhöht Feuchte)
    game.fertilize()                   -> Düngen (schnelleres Wachstum)
    game.weed()                        -> Unkraut entfernen
    game.spray()                       -> Pestizide (reduziert Schädlingsbefall)
    game.wait(steps=1)                 -> Zeit vergeht & wächst (#)
    game.harvest()                     -> Ernten (# -> *)
    game.reclaim()                     -> Feld zurücksetzen (leer)

Lieferung & Handel:
    game.deliver()                     -> Abgabe am Haus (x=19, y=4)
    game.sell('weizen', qty)           -> Verkauf beim Händler
    game.buy('weizen_saat', qty)       -> Einkauf von Saat

Info:
    game.status()                      -> Position, Beutel, Ertrag, Geld, Wetter
    game.map_info()                    -> Kartenstatistik
    game.inventory()                   -> Inventar anzeigen
    game.storage_info()                -> Lager anzeigen
    game.weather_info()                -> Wetterhistorie
    game.log_show()                    -> Logbuch anzeigen
    game.list_quests()                 -> Quests anzeigen
    game.quest_detail(index)           -> Questdetails

System:
    game.save_game('save.json')        -> Speichern
    game.load_game('save.json')        -> Laden
    game.reset_message()               -> Meldung leeren
    sys.exit()                         -> Beenden

Beispiele:
    # Drei Felder pflügen und säen
    for _ in range(3):
        game.move('E')
        game.plow()
        game.sow('weizen')

    # Wachsen lassen und ernten
    for _ in range(3):
        game.wait()
    game.harvest()

Wichtig:
- Eingaben werden als Python-Block ausgeführt, Leerzeile beendet den Block.
- Fehler in einer Zeile stoppen den gesamten Block.
===========================================
"""
        print(text)
        self.last_help_text = text
        self.message = "Hilfe angezeigt."
        self.log.add("Hilfe geöffnet.")

    def reset_message(self):
        self.message = ""

    # --------------------------
    # Wetter & Wachstum
    # --------------------------
    def _roll_weather(self):
        # Zufällige Wetteränderung mit Varianz
        if random.random() < OPTIONS["weather_variability"]:
            self.weather = random.choice(WEATHER_TYPES)
            self.weather_history.append(self.weather)

    def _apply_weather_effects(self):
        # Feuchte beeinflusst Wachstum
        for y in range(self.h):
            for x in range(self.w):
                c = self.field[y][x]
                if c.state in (2, 3):  # gesät/reif
                    if self.weather == "regen":
                        c.moisture = clamp(c.moisture + 0.2, 0.0, 1.0)
                    elif self.weather == "heiß":
                        c.moisture = clamp(c.moisture - 0.2, 0.0, 1.0)
                    elif self.weather == "sturm":
                        # Sturm erhöht die Chance auf Krankheit
                        if random.random() < 0.06:
                            c.diseased = True

    def _spread_weeds_and_pests(self):
        for y in range(self.h):
            for x in range(self.w):
                c = self.field[y][x]
                if c.state in (0, 1, 2):
                    if random.random() < OPTIONS["weed_base_chance"]:
                        c.weed = True
                        c.state = 6
                if c.state in (2, 3):
                    base = OPTIONS["pest_base_chance"]
                    resistance = SEED_TYPES.get(c.seed_type, {}).get("resistance", 0.2)
                    chance = max(0.01, base * (1.0 - resistance))
                    if random.random() < chance:
                        c.pest = True
                        c.diseased = True
                        c.state = 7

    def _growth_step(self):
        matured_count = 0
        for y in range(self.h):
            for x in range(self.w):
                c = self.field[y][x]
                if c.state == 2 and c.seed_type:
                    seed_info = SEED_TYPES.get(c.seed_type)
                    if seed_info:
                        # Feuchte-Schwelle
                        if c.moisture >= 0.3 and not c.diseased:
                            c.growth += 1
                        else:
                            # bei niedriger Feuchte langsamer
                            if random.random() < 0.4:
                                c.growth += 1
                        # Dünger-Effekt: simuliert durch Toolqualität (vereinfachend)
                        steps_needed = max(1, int(seed_info("grow_steps") / self.robot.tool_quality))
                        if c.growth >= steps_needed:
                            c.state = 3
                            matured_count += 1
        return matured_count

    def _disease_spread(self):
        # Krankheiten können sich auf Nachbarn ausbreiten
        for y in range(self.h):
            for x in range(self.w):
                c = self.field[y][x]
                if c.diseased and c.state in (2, 3):
                    for nx, ny in self._neighbors(x, y):
                        nc = self.field[ny][nx]
                        if nc.state in (2, 3) and not nc.diseased:
                            if random.random() < OPTIONS["disease_spread_chance"]:
                                nc.diseased = True
                                if nc.state == 2:
                                    nc.state = 7

    def _neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        res = []
        if x > 0: res.append((x - 1, y))
        if x < self.w - 1: res.append((x + 1, y))
        if y > 0: res.append((x, y - 1))
        if y < self.h - 1: res.append((x, y + 1))
        return res

    # --------------------------
    # Aktionen
    # --------------------------
    def move(self, d: str):
        d = d.upper().strip()
        delta = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
        if d not in delta:
            print("Roboter: Richtung muss N, S, E oder W sein.")
            self.message = "Ungültige Richtung."
            return
        dx, dy = delta[d]
        self.robot.x = clamp(self.robot.x + dx, 0, self.w - 1)
        self.robot.y = clamp(self.robot.y + dy, 0, self.h - 1)
        self.robot.energy = clamp(self.robot.energy - 1, 0, 100)
        print(f"Roboter: Position ({self.robot.x},{self.robot.y}).")
        self.message = f"Bewegt nach {d}."
        self.log.add(f"Bewegung: {d}")

    def go_to(self, x: int, y: int):
        # einfache BFS-Pfadfindung, meidet Hindernisse
        target = (clamp(x, 0, self.w - 1), clamp(y, 0, self.h - 1))
        start = (self.robot.x, self.robot.y)
        if start == target:
            print("Roboter: Ziel bereits erreicht.")
            return
        path = self._bfs_path(start, target)
        if not path:
            print("Roboter: Kein Pfad gefunden.")
            self.log.add("Pfadfindung fehlgeschlagen.")
            return
        steps = 0
        for px, py in path[1:]:  # ersten Punkt (Start) überspringen
            if steps >= OPTIONS["pathfinding_max_steps"]:
                break
            self.robot.x, self.robot.y = px, py
            steps += 1
            print(f"Roboter: Gehe zu ({px},{py}).")
        self.message = f"Ziel erreicht ({self.robot.x},{self.robot.y})."
        self.log.add(f"Wegfindung: {start} -> {target} in {steps} Schritten.")

    def _bfs_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        q = deque([start])
        came_from: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}
        while q:
            cx, cy = q.popleft()
            if (cx, cy) == goal:
                break
            for nx, ny in self._neighbors(cx, cy):
                if (nx, ny) not in came_from:
                    if self.field[ny][nx].state != 5:  # kein Hindernis
                        came_from[(nx, ny)] = (cx, cy)
                        q.append((nx, ny))
        if goal not in came_from:
            return []
        # Pfad rekonstruieren
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = came_from[cur]
        path.reverse()
        return path

    def plow(self):
        x, y = self.robot.x, self.robot.y
        c = self.field[y][x]
        if c.state in (0, 4, 6, 7):  # auch Unkraut/Krankheit räumt der Pflug weg
            c.state = 1
            c.growth = 0
            c.seed_type = None
            c.weed = False
            c.pest = False
            c.diseased = False
            print("Roboter: Feld gepflügt (=).")
            self.message = "Pflügen erledigt."
            self.robot.add_exp(5)
            self.log.add(f"Pflügen bei ({x},{y}).")
        else:
            print("Roboter: Pflügen hier nicht möglich.")
            self.message = "Pflügen fehlgeschlagen."
            self.log.add(f"Pflügen fehlgeschlagen bei ({x},{y}).")

    def sow(self, seed: str = "weizen"):
        seed = seed.lower().strip()
        if seed not in SEED_TYPES:
            print(f"Roboter: Unbekannte Saat '{seed}'. Verfügbar: {', '.join(SEED_TYPES.keys())}")
            self.message = "Säen fehlgeschlagen."
            return
        inv_name = f"{seed}_saat"
        if not self.inventory.has(inv_name, 1):
            print(f"Roboter: Keine {inv_name} im Inventar.")
            self.message = "Säen fehlgeschlagen."
            return
        x, y = self.robot.x, self.robot.y
        c = self.field[y][x]
        if c.state == 1:
            c.state = 2
            c.seed_type = seed
            c.growth = 0
            self.inventory.remove(inv_name, 1)
            print(f"Roboter: Saat '{seed}' ausgebracht (+).")
            self.message = f"Säen: {seed}."
            self.robot.add_exp(5)
            self.log.add(f"Säen {seed} bei ({x},{y}).")
        else:
            print("Roboter: Erst pflügen (=), dann säen (+).")
            self.message = "Säen fehlgeschlagen."

    def water(self):
        x, y = self.robot.x, self.robot.y
        c = self.field[y][x]
        c.moisture = clamp(c.moisture + 0.25, 0.0, 1.0)
        print(f"Roboter: Bewässert. Feuchte={c.moisture:.2f}")
        self.message = "Bewässerung durchgeführt."
        self.log.add(f"Wasser bei ({x},{y}).")

    def fertilize(self):
        if not self.storage.has("dünger", 1):
            print("Roboter: Kein Dünger im Lager.")
            self.message = "Düngen fehlgeschlagen."
            return
        self.storage.remove("dünger", 1)
        self.robot.tool_quality = clamp(self.robot.tool_quality + 0.1, 1.0, 2.0)
        print(f"Roboter: Gedüngt. Werkzeugqualität={self.robot.tool_quality:.2f}")
        self.message = "Düngung durchgeführt."
        self.log.add("Düngung global.")

    def weed(self):
        x, y = self.robot.x, self.robot.y
        c = self.field[y][x]
        if c.weed or c.state == 6:
            c.weed = False
            if c.state == 6:
                c.state = 0
            print("Roboter: Unkraut entfernt.")
            self.message = "Unkraut entfernt."
            self.log.add(f"Unkraut entfernt bei ({x},{y}).")
        else:
            print("Roboter: Kein Unkraut hier.")
            self.message = "Kein Unkraut."

    def spray(self):
        if not self.storage.has("pestizid", 1):
            print("Roboter: Kein Pestizid im Lager.")
            self.message = "Spritzen fehlgeschlagen."
            return
        x, y = self.robot.x, self.robot.y
        c = self.field[y][x]
        self.storage.remove("pestizid", 1)
        c.pest = False
        c.diseased = False
        if c.state == 7 and c.seed_type:
            c.state = 2  # zurück zu gesät
        print("Roboter: Schädlingsbekämpfung durchgeführt.")
        self.message = "Pestizid eingesetzt."
        self.log.add(f"Pestizid bei ({x},{y}).")

    def wait(self, steps: int = 1):
        steps = max(1, int(steps))
        matured_total = 0
        for _ in range(steps):
            self._roll_weather()
            self._apply_weather_effects()
            matured_total += self._growth_step()
            self._spread_weeds_and_pests()
            self._disease_spread()
            if OPTIONS["animate_wait"]:
                time.sleep(0.2)
        print(f"Roboter: Zeit vergeht ({steps}). Reif geworden: {matured_total} Felder.")
        self.message = f"Warten beendet. {matured_total} Felder reif."
        self.log.add(f"Warten: {steps} Schritte, {matured_total} gereift.")

    def harvest(self):
        x, y = self.robot.x, self.robot.y
        c = self.field[y][x]
        if c.state == 3 and c.seed_type:
            yield_amount = SEED_TYPES[c.seed_type]["yield"]
            self.robot.bag += yield_amount
            self.robot.total_harvest += yield_amount
            # Quest-Update
            key_h = f"harvest_{c.seed_type}"
            for q in self.quests:
                q.update_progress(key_h, yield_amount)
            print(f"Roboter: {yield_amount}x {c.seed_type} geerntet (# -> *). Beutel={self.robot.bag}")
            c.state = 4
            c.growth = 0
            self.robot.add_exp(10)
            self.message = "Ernten erfolgreich."
            self.log.add(f"Ernte {yield_amount}x {c.seed_type} bei ({x},{y}).")
        else:
            print("Roboter: Hier ist nichts reif.")
            self.message = "Ernten fehlgeschlagen."

    def reclaim(self):
        x, y = self.robot.x, self.robot.y
        self.field[y][x].reset()
        print("Roboter: Feld zurückgesetzt (leer).")
        self.message = "Feld zurückgesetzt."
        self.log.add(f"Reset Feld bei ({x},{y}).")

    def deliver(self):
        if self.robot.x == DELIVERY_X and self.robot.y == DELIVERY_Y:
            if self.robot.bag > 0:
                delivered = self.robot.bag
                print(f"Roboter: Lieferung {delivered} Einheiten am Farmhaus. Farmer bedankt sich.")
                self.save.money += delivered * 3  # Lieferbonus
                # Quest: Lieferung von Weizen
                for q in self.quests:
                    q.update_progress("deliver_weizen", delivered)
                self.robot.bag = 0
                self.message = "Lieferung erfolgreich!"
                self.log.add(f"Lieferung {delivered}. Geld={self.save.money}")
            else:
                print("Roboter: Beutel ist leer.")
                self.message = "Nichts zu liefern."
        else:
            print("Roboter: Zur Tür (x=19, y=4) gehen.")
            self.message = "Zum Liefern zur Tür."

    def sell(self, crop: str, qty: int):
        crop = crop.lower().strip()
        if crop not in SELL_PRICES:
            print(f"Roboter: Unbekannte Ware '{crop}'.")
            self.message = "Verkauf fehlgeschlagen."
            return
        # Verkauf erfolgt aus Beutel anteilig
        if self.robot.bag < qty:
            print("Roboter: Nicht genug im Beutel.")
            self.message = "Verkauf fehlgeschlagen."
            return
        self.robot.bag -= qty
        money = SELL_PRICES[crop] * qty
        self.save.money += money
        print(f"Roboter: Verkauf {qty}x {crop}. Erlös={money}. Geld={self.save.money}")
        self.message = "Verkauf erfolgreich."
        self.log.add(f"Verkauf {qty}x {crop}.")

    def buy(self, item: str, qty: int):
        item = item.lower().strip()
        if not item.endswith("_saat"):
            print("Roboter: Nur Saat wird hier verkauft (z.B. 'weizen_saat').")
            self.message = "Einkauf fehlgeschlagen."
            return
        base = item.replace("_saat", "")
        if base not in SEED_TYPES:
            print(f"Roboter: Unbekannte Saat '{item}'.")
            self.message = "Einkauf fehlgeschlagen."
            return
        price = SEED_TYPES[base]["price"] * qty
        if self.save.money < price:
            print(f"Roboter: Zu wenig Geld ({self.save.money} < {price}).")
            self.message = "Einkauf fehlgeschlagen."
            return
        self.save.money -= price
        self.inventory.add(item, qty)
        print(f"Roboter: Gekauft {qty}x {item} für {price}. Geld={self.save.money}")
        self.message = "Einkauf erfolgreich."
        self.log.add(f"Einkauf {qty}x {item}.")

    # --------------------------
    # Info & Status
    # --------------------------
    def status(self):
        print(f"Status: Pos=({self.robot.x},{self.robot.y}) | Beutel={self.robot.bag} | Ertrag={self.robot.total_harvest} | "
              f"Energie={self.robot.energy} | Level={self.robot.level} | Geld={self.save.money} | Wetter={self.weather}")
        self.message = "Status ausgegeben."
        self.log.add("Status abgerufen.")

    def map_info(self):
        stats = {"leer": 0, "gepflügt": 0, "gesät": 0, "reif": 0, "geerntet": 0, "hindernis": 0, "unkraut": 0, "krank": 0}
        for y in range(self.h):
            for x in range(self.w):
                s = self.field[y][x].state
                if s == 0: stats["leer"] += 1
                elif s == 1: stats["gepflügt"] += 1
                elif s == 2: stats["gesät"] += 1
                elif s == 3: stats["reif"] += 1
                elif s == 4: stats["geerntet"] += 1
                elif s == 5: stats["hindernis"] += 1
                elif s == 6: stats["unkraut"] += 1
                elif s == 7: stats["krank"] += 1
        print("Karteninfo:", stats)
        self.message = "Karteninfo angezeigt."
        self.log.add("Karteninfo.")

    def inventory(self):
        items = self.inventory.list()
        if items:
            print("Inventar:")
            for name, qty in items:
                print(f"  - {name}: {qty}")
        else:
            print("Inventar: leer")
        self.message = "Inventar angezeigt."
        self.log.add("Inventar angezeigt.")

    def storage_info(self):
        items = self.storage.list()
        if items:
            print("Lager:")
            for name, qty in items:
                print(f"  - {name}: {qty}")
        else:
            print("Lager: leer")
        self.message = "Lager angezeigt."
        self.log.add("Lager angezeigt.")

    def weather_info(self):
        print(f"Aktuelles Wetter: {self.weather}")
        if self.weather_history:
            print("Letzte Wetter:", list(self.weather_history))
        self.message = "Wetterinfo angezeigt."
        self.log.add("Wetterinfo.")

    def list_quests(self):
        if not self.quests:
            print("Keine aktiven Quests.")
        else:
            for i, q in enumerate(self.quests):
                status = "✓" if q.completed else "…"
                print(f"[{i}] {q.name} ({status})")
        self.message = "Quests aufgelistet."
        self.log.add("Quests aufgelistet.")

    def quest_detail(self, index: int):
        if index < 0 or index >= len(self.quests):
            print("Ungültiger Quest-Index.")
            self.message = "Questdetail fehlgeschlagen."
            return
        print(self.quests[index].summary())
        self.message = "Questdetail angezeigt."
        self.log.add(f"Questdetail {index}.")

    def log_show(self):
        print("Logbuch:")
        print(self.log.dump())
        self.message = "Logbuch angezeigt."

    # --------------------------
    # Speichern/Laden
    # --------------------------
    def save_game(self, filename: str):
        data = {
            "save": self.save.to_dict(),
            "robot": {
                "x": self.robot.x, "y": self.robot.y, "bag": self.robot.bag,
                "total_harvest": self.robot.total_harvest, "energy": self.robot.energy,
                "level": self.robot.level, "exp": self.robot.exp, "tool_quality": self.robot.tool_quality
            },
            "inventory": self.inventory.items,
            "storage": self.storage.items,
            "weather": self.weather,
            "weather_history": list(self.weather_history),
            "field": [[self._cell_to_dict(self.field[y][x]) for x in range(self.w)] for y in range(self.h)],
            "quests": [self._quest_to_dict(q) for q in self.quests]
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Spiel gespeichert in '{filename}'.")
        self.message = "Spiel gespeichert."
        self.log.add(f"Speichern: {filename}")

    def load_game(self, filename: str):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"Laden fehlgeschlagen: {e}")
            self.message = "Laden fehlgeschlagen."
            return
        self.save = SaveData.from_dict(data.get("save", {}))
        rob = data.get("robot", {})
        self.robot.x = rob.get("x", 0)
        self.robot.y = rob.get("y", 0)
        self.robot.bag = rob.get("bag", 0)
        self.robot.total_harvest = rob.get("total_harvest", 0)
        self.robot.energy = rob.get("energy", 100)
        self.robot.level = rob.get("level", 1)
        self.robot.exp = rob.get("exp", 0)
        self.robot.tool_quality = rob.get("tool_quality", 1.0)
        self.inventory.items = data.get("inventory", {})
        self.storage.items = data.get("storage", {})
        self.weather = data.get("weather", "klar")
        self.weather_history = deque(data.get("weather_history", []), maxlen=5)
        field_data = data.get("field", [])
        for y in range(self.h):
            for x in range(self.w):
                try:
                    cd = field_data[y][x]
                except Exception:
                    cd = {}
                self._dict_to_cell(self.field[y][x], cd)
        self.quests = [self._dict_to_quest(qd) for qd in data.get("quests", [])]
        print(f"Spiel geladen aus '{filename}'.")
        self.message = "Spiel geladen."
        self.log.add(f"Laden: {filename}")

    def _cell_to_dict(self, c: Cell) -> Dict:
        return {
            "state": c.state, "growth": c.growth, "seed_type": c.seed_type,
            "moisture": c.moisture, "pest": c.pest, "weed": c.weed, "diseased": c.diseased
        }

    def _dict_to_cell(self, c: Cell, d: Dict):
        c.state = d.get("state", 0)
        c.growth = d.get("growth", 0)
        c.seed_type = d.get("seed_type", None)
        c.moisture = d.get("moisture", 0.5)
        c.pest = d.get("pest", False)
        c.weed = d.get("weed", False)
        c.diseased = d.get("diseased", False)

    def _quest_to_dict(self, q: Quest) -> Dict:
        return {
            "name": q.name, "description": q.description,
            "goals": q.goals, "progress": q.progress,
            "completed": q.completed, "reward_money": q.reward_money,
            "reward_exp": q.reward_exp
        }

    def _dict_to_quest(self, d: Dict) -> Quest:
        q = Quest(d.get("name", "Unbekannt"), d.get("description", ""), d.get("goals", {}), d.get("reward_money", 0), d.get("reward_exp", 0))
        q.progress = d.get("progress", {k: 0 for k in q.goals.keys()})
        q.completed = d.get("completed", False)
        return q

    # --------------------------
    # Darstellung
    # --------------------------
    def render(self):
        # Bildschirm leeren
        print("\x1b[2J\x1b[H", end="")
        title = f"Acker ({self.w}x{self.h})  |  Farmhaus   | Beutel: {self.robot.bag} | Gesamt-Ertrag: {self.robot.total_harvest} | Geld: {self.save.money} | Wetter: {self.weather}"
        print(title)
        print("-" * max(60, len(title)))
        # Karte
        for row in range(self.h):
            line = "".join(
                'R' if (self.robot.x == x and self.robot.y == row)
                else STATE_CH.get(self.field[row][x].state, '?')
                for x in range(self.w)
            )
            house = HOUSE_ART[row] if row < len(HOUSE_ART) else ""
            if OPTIONS["show_grid"]:
                print(f"{line}   {house}")
            else:
                print(line)
        print("-" * max(60, len(title)))
        if self.message:
            print(self.message)
        else:
            print("")

        if not self.started:
            print("Tipps: game.help() • game.tutorial() • sys.exit()")
        # keine automatische Ausgaben nach render, damit Hilfe oben sichtbar bleibt

    # --------------------------
    # Tutorial
    # --------------------------
    def tutorial(self):
        print("Tutorial: Pflügen, Säen, Warten, Ernten, Liefern (Weizen).")
        # einfache Routine, weicht Hindernissen mit go_to aus
        steps = [(2, 0), (3, 0), (4, 0)]
        for tx, ty in steps:
            self.go_to(tx, ty)
            self.plow()
            self.sow("weizen")
        self.wait(3)
        for tx, ty in steps:
            self.go_to(tx, ty)
            self.harvest()
        self.go_to(DELIVERY_X, DELIVERY_Y)
        self.deliver()
        self.message = "Tutorial beendet. Nutze game.help() für mehr."
        self.log.add("Tutorial abgeschlossen.")

    # --------------------------
    # Spielschleife
    # --------------------------
    def run(self):
        allowed = {
            'game': self,
            'sys': sys,
            # einige sichere Funktionen erlauben
            'range': range, 'len': len, 'min': min, 'max': max, 'abs': abs
        }
        self.render()
        self.started = True
        while True:
            try:
                print(">>> Mehrzeiligen Python-Code eingeben (Leerzeile beendet den Block)")
                lines = []
                while True:
                    line = input("... ")
                    if not line.strip():
                        break
                    lines.append(line)
                cmd = "\n".join(lines)
                if not cmd.strip():
                    continue
                exec(cmd, {'__builtins__': {}}, allowed)
                if OPTIONS["auto_render"]:
                    self.render()
            except SystemExit:
                print("Spiel beendet. Danke fürs Spielen!")
                return
            except Exception as e:
                self.message = f"Fehler: {e}"
                print(f"Fehler: {e}")
                self.log.add(f"Fehler: {e}")
                self.render()

# ------------------------------
# Hauptprogramm
# ------------------------------

def main():
    game = FarmGame()
    # Optional: Startroutine ins Log
    game.log.add("Spiel gestartet.")
    game.run()

if __name__ == "__main__":
    main()