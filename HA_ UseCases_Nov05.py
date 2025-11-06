# 🍽️ Use Case: Essensbestellungs-App für ein Restaurant
#
# Use Case Name:
# Bestellung von Speisen über die App
#
# Akteure:
# - Kunde (Hauptakteur)
# - Bezahlsystem (z. B. PayPal, Kreditkarte)
# - Küchensystem (zur Entgegennahme der Bestellung)
#
# Ziel:
# Der Kunde möchte Speisen über die App bestellen und bezahlen, 
# um das Essen im Restaurant abzuholen oder liefern zu lassen.
#
# Vorbedingungen:
# - Der Kunde hat die App installiert und ist eingeloggt.
# - Das Restaurant ist geöffnet und Bestellungen werden akzeptiert.
#
# Nachbedingungen:
# - Die Bestellung ist erfolgreich im System gespeichert.
# - Der Kunde hat eine Bestellbestätigung erhalten.
# - Die Küche hat die Bestellung zur Zubereitung erhalten.
#
# Hauptablauf:
# 1. Der Kunde öffnet die App und wählt das Restaurant aus.
# 2. Das System zeigt die verfügbare Speisekarte an.
# 3. Der Kunde wählt die gewünschten Gerichte aus und legt sie in den Warenkorb.
# 4. Der Kunde überprüft die Bestellung und wählt „Zur Kasse“.
# 5. Der Kunde gibt Lieferadresse oder Abholoption an.
# 6. Der Kunde wählt die Zahlungsart (z. B. Kreditkarte, PayPal).
# 7. Das System überprüft die Zahlungsdaten und verarbeitet die Zahlung.
# 8. Nach erfolgreicher Zahlung bestätigt das System die Bestellung.
# 9. Das System sendet die Bestelldetails an das Küchensystem.
# 10. Der Kunde erhält eine Bestellbestätigung mit voraussichtlicher Lieferzeit.
#
# Alternativabläufe:
# A1: Kunde wählt „Abholung“ statt Lieferung:
#     - Schritte 5–6 bleiben gleich, aber keine Lieferadresse wird benötigt.
#     - Bestätigung enthält Abholzeit statt Lieferzeit.
#
# A2: Kunde ändert Bestellung vor der Zahlung:
#     - Kunde kann Gerichte entfernen oder hinzufügen, bevor er „Zur Kasse“ wählt.
#
# A3: Zahlung mit Gutschein:
#     - Kunde gibt Gutscheincode ein.
#     - System überprüft Gültigkeit und reduziert den Gesamtbetrag.
#
# Ausnahmen:
# E1: Zahlung fehlgeschlagen:
#     - System zeigt Fehlermeldung an.
#     - Kunde kann andere Zahlungsart wählen oder Bestellung abbrechen.
#
# E2: Gericht nicht mehr verfügbar:
#     - System informiert den Kunden, dass das Gericht ausverkauft ist.
#     - Kunde kann ein alternatives Gericht auswählen.
#
# E3: Netzwerkfehler:
#     - Bestellung wird nicht übertragen.
#     - System zeigt Fehlermeldung und bietet Wiederholung an.

