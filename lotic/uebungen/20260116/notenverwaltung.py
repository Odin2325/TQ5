# prüft ob eine Note gültig ist (zw. 1 und 6)
# gibt in dem fall True zurück, ansonsten (0, -10, "foo") False
def ist_gueltige_note(note: int) -> bool:
    if not isinstance(note, int):
        return False
    if note < 1 or note > 6:
        return False
    return True

# berechnet den Durchschnitt einer Liste von Noten
# wirft ValueError wenn die Liste leer ist
# wirft Value Error wenn eine Note für ist_gueltige_note() false zurückgibt
def durchschnitt(noten: list[int]) -> float:
    if len(noten) < 1:
        raise ValueError('Leere Liste')
    sum = 0
    for note in noten:
        if not ist_gueltige_note(note):
            raise ValueError('Ungültige Note')
        sum += note
    return sum / len(noten)

# gibt die beste Note zurück
# wirft ValueError wenn die Liste leer ist
def beste_note(noten: list[int]) -> int:
    if len(noten) < 1:
        raise ValueError('Leere Liste')
    noten.sort()
    return noten[0]

# wandelt Note in Text um (1 -> "sehr gut" usw)
# wirft ValueError wenn ist_gueltige_note() false zurückgibt
def note_zu_text(note: int) -> str:
    if not ist_gueltige_note(note):
        raise ValueError('Ungültige Note')
    textGrades = {
        1: 'sehr gut',
        2: 'gut',
        3: 'befriedigend',
        4: 'ausreichend',
        5: 'mangelhaft',
        6: 'ungenügend',
    }
    return textGrades[note]
