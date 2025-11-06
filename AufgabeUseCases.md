# Aufgabe: Kinoticket-Buchungssystem

## Beschreibung:
Ein Kino möchte ein Online-System einführen, über das Kunden Kinotickets kaufen können.


## Rahmenbedingungen:

### Das System soll Folgendes ermöglichen:

Kunden können aktuelle Filme und Vorführzeiten ansehen.

Kunden können Sitzplätze auswählen und Tickets buchen.

Kunden können ihre Buchung stornieren.

Ein Administrator kann neue Filme und Vorführzeiten hinzufügen oder löschen.


## Unsere Aufgabe:

Identifiziere die Akteure:
(z. B. Kunde, Administrator, Bezahlsystem)

Erstelle 1 Use Case:

   * Filmübersicht anzeigen

   * Ticket buchen

   * Buchung stornieren

 *  Film hinzufügen (Admin)


# Use Case: Ticket buchen
# 
# 1. Name:
#    Ticket buchen
#
# 2. Ziel:
#    Der Kunde möchte ein oder mehrere Kinotickets für eine bestimmte Vorstellung buchen
#    und erhält am Ende eine Buchungsbestätigung.
#
# 3. Akteure:
#    - Primärer Akteur: Kunde
#    - Sekundäre Akteure:
#        * Bezahlsystem (z. B. PayPal, Kreditkarte)
#        * Kinosystem (zur Verwaltung von Sitzplätzen und Vorstellungen)
#
# 4. Auslöser:
#    Der Kunde entscheidet sich, ein Ticket für einen Film zu kaufen,
#    nachdem er die Filmübersicht und Vorführzeiten angesehen hat.
#
# 5. Vorbedingungen:
#    - Der Kunde registriert sich 
#    - Der Kunde hat Zugriff auf das Online-Kinoticket-System.
#    - Der Film und die gewünschte Vorstellung sind im System vorhanden.
#    - Es sind noch freie Sitzplätze verfügbar.
#    
#
# 6. Nachbedingungen:
#    - Die Buchung ist erfolgreich im System gespeichert.
#    - Der Kunde erhält eine Buchungsbestätigung (z. B. per E-Mail oder QR-Code).
#    - Die gebuchten Sitzplätze werden als "belegt" markiert.
#
# 7. Hauptablauf :
#    1. Der Kunde öffnet das Kinoticket-System.
#    2. Der Kunde wählt einen Film aus der Filmübersicht.
#    3. Das System zeigt verfügbare Vorführzeiten an.
#    4. Der Kunde wählt eine Vorstellung (Datum, Uhrzeit, Saal).
#    5. Das System zeigt eine Sitzplatzübersicht.
#    6. Der Kunde wählt einen oder mehrere freie Sitzplätze.
#    7. Der Kunde gibt ggf. persönliche Daten (Name, E-Mail-Adresse) ein.
#    8. Der Kunde wählt eine Zahlungsmethode und gibt Zahlungsdaten ein.
#    9. Das Bezahlsystem überprüft die Zahlung.
#   10. Nach erfolgreicher Zahlung speichert das System die Buchung.
#   11. Das System sendet eine Buchungsbestätigung an den Kunden.
#   12. Der Use Case endet erfolgreich.
#
# 8. Alternativabläufe:
#     Zahlung fehlgeschlagen
#        - Das Bezahlsystem meldet einen Fehler (z. B. unzureichendes Guthaben).
#        - Das System informiert den Kunden, dass die Buchung nicht abgeschlossen wurde.
#        - Der Kunde kann eine andere Zahlungsmethode wählen oder abbrechen.
#
#     Sitzplatz inzwischen belegt
#        - Ein anderer Kunde hat den gleichen Sitzplatz kurz zuvor gebucht.
#        - Das System zeigt eine Fehlermeldung und bittet um erneute Auswahl.
#
#     Abbruch durch den Kunden
#        - Der Kunde verlässt den Buchungsvorgang vor Abschluss der Zahlung.
#        - Keine Buchung wird gespeichert.
#
# 9. Sonderfälle / Erweiterungen:
#     Registrierter Kunde → gespeicherte Zahlungs-/Kontodaten werden vorgeschlagen.
#     Gruppenbuchung → Mehrere Sitzplätze können gemeinsam gebucht werden.

# Abbruch durch den Kunden
#        - Der Kunde verlässt den Buchungsvorgang vor Abschluss der Zahlung.
#        - Keine Buchung wird gespeichert.

# 10. Beteiligte Systemkomponenten:
#     - Benutzeroberfläche (Frontend)
#     - Buchungsverwaltungssystem
#     - Sitzplatzverwaltung
#     - Bezahlschnittstelle (API)
#     - E-Mail-/Benachrichtigungssystem
#
# ============================================================
