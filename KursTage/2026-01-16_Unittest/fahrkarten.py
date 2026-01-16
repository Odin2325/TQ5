# Gibt Grundpreis abhängig vom Alter zurück
# wirft ValueError wenn Alter negativ
# wirft ValueError wenn Alter < 6 (Kinder unter 6 Jahren brauchen kein Ticket)
# Kinder und Jugendliche zwischen 6 und 17 Jahren: Grundpreis 1.5
# Erwachsene: Grundpreis 3.0
def grundpreis(alter: int) -> float:
    pass

# Gibt den Zuschlag für die Zonen zurück
# Es gibt nur drei Zonen: 1, 2 und 3
# Wirft ValueError bei ungültiger Zone
# Bei Zone 1 gibt es keinen Zuschlag, bei Zone 2 Zuschlag 1.0, Zone 3 Zuschlag 2.0
def zonen_zuschlag(zone: int) -> float:
    pass


# Berechnet den rabattierten Preis
# Wirft ValueError wenn Ticketzahl < 0
# Bei 4 oder mehr Tickets gibt es 10 % Rabatt
def rabatt(ticket_anzahl: int, preis: float) -> float:
    pass

# Berechnet Gesamtpreis für die Fahrkarten anhand Alter, Zone und Ticketanzahl
def gesamtpreis(alter: int, zone: int, ticket_anzahl: int = 1) -> float:
    pass
