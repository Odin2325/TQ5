def grundpreis(alter: int) -> float:
    """
    Gibt den Grundpreis abhängig vom Alter zurück.
    """
    if alter < 0:
        raise ValueError("Alter darf nicht negativ sein")
    if alter < 6:
        raise ValueError("Kinder unter 6 Jahren brauchen kein Ticket")
    if alter <= 17:
        return 1.5
    return 3.0


def zonen_zuschlag(zone: int) -> float:
    """
    Gibt den Zuschlag für die Zone zurück.
    """
    # if zone not in (1, 2, 3):
    #     raise ValueError("Ungültige Zone")

    # if zone == 1:
    #     return 0.0
    # elif zone == 2:
    #     return 1.0
    # else:
    #     return 2.0

    match zone:
        case 1:
            return 0.0
        case 2:
            return 1.0
        case 3:
            return 2.0
        case _:
            raise ValueError("Ungültige Zone")


def rabatt(ticket_anzahl: int, preis: float) -> float:
    """
    Berechnet den Rabatt.
    """
    if ticket_anzahl < 0:
        raise ValueError("Ticketanzahl darf nicht negativ sein")

    if ticket_anzahl >= 4:
        return preis * 0.9
    return preis


def gesamtpreis(alter: int, zone: int, ticket_anzahl: int = 1) -> float:
    """
    Berechnet den Gesamtpreis für die Fahrkarten.
    """
    grund = grundpreis(alter)
    zuschlag = zonen_zuschlag(zone)

    preis_pro_ticket = grund + zuschlag
    gesamt = preis_pro_ticket * ticket_anzahl

    return rabatt(ticket_anzahl, gesamt)
