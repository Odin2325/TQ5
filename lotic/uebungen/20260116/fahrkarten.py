# Gibt Grundpreis abhängig vom Alter zurück
# wirft ValueError wenn Alter negativ
# wirft ValueError wenn Alter < 6 (Kinder unter 6 Jahren brauchen kein Ticket)
# Kinder und Jugendliche zwischen 6 und 17 Jahren: Grundpreis 1.5
# Erwachsene: Grundpreis 3.0
def grundpreis(alter: int) -> float:
    if not isinstance(alter, int):
        raise ValueError('Ungültiges Alter')
    if alter < 6:
        raise ValueError('Ungültiges Alter')
    if alter < 17:
        return 1.5
    return 3.0

# Gibt den Zuschlag für die Zonen zurück
# Es gibt nur drei Zonen: 1, 2 und 3
# Wirft ValueError bei ungültiger Zone
# Bei Zone 1 gibt es keinen Zuschlag, bei Zone 2 Zuschlag 1.0, Zone 3 Zuschlag 2.0
def zonen_zuschlag(zone: int) -> float:
    if not isinstance(zone, int):
        raise ValueError('Ungültige Zone')
    if zone < 1 or zone > 3:
        raise ValueError('Ungültige Zone')
    zuschlag = {
        1: 0.0,
        2: 1.0,
        3: 2.0
    }
    return zuschlag[zone]

# Berechnet den rabattierten Preis
# Wirft ValueError wenn Ticketzahl < 0
# Bei 4 oder mehr Tickets gibt es 10 % Rabatt
def rabatt(ticket_anzahl: int, preis: float) -> float:
    if ticket_anzahl < 0:
        raise ValueError('Ungültige Anzahl')
    if ticket_anzahl < 4:
        return preis * ticket_anzahl
    return preis * 0.9 * ticket_anzahl

# Berechnet Gesamtpreis für die Fahrkarten anhand Alter, Zone und Ticketanzahl
def gesamtpreis(alter: int, zone: int, ticket_anzahl: int = 1) -> float:
    preis = grundpreis(alter) + zonen_zuschlag(zone)
    return rabatt(ticket_anzahl, preis)
