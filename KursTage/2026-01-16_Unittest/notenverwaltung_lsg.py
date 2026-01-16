def ist_gueltige_note(note: int) -> bool:
    """
    Prüft, ob eine Note gültig ist (1 bis 6).
    """
    return isinstance(note, int) and 1 <= note <= 6


def durchschnitt(noten: list[int]) -> float:
    """
    Berechnet den Durchschnitt einer Liste von Noten.
    """
    if not noten:
        raise ValueError("Notenliste darf nicht leer sein")

    for note in noten:
        if not ist_gueltige_note(note):
            raise ValueError(f"Ungültige Note: {note}")

    return sum(noten) / len(noten)


def beste_note(noten: list[int]) -> int:
    """
    Gibt die beste (kleinste) Note zurück.
    """
    if not noten:
        raise ValueError("Notenliste darf nicht leer sein")

    return min(noten)


def note_zu_text(note: int) -> str:
    """
    Wandelt eine Note in Text um.
    """
    if not ist_gueltige_note(note):
        raise ValueError("Ungültige Note")

    texte = {
        1: "sehr gut",
        2: "gut",
        3: "befriedigend",
        4: "ausreichend",
        5: "mangelhaft",
        6: "ungenügend",
    }

    return texte[note]