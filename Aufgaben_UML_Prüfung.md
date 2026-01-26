### Aufgabe 1: Erweiterte Online-Bestellung

Erstellen Sie ein UML-Aktivitätsdiagramm mit zwei Swimlanes (Kunde und Online-Shop), das folgenden Ablauf darstellt:

    Der Kunde wählt ein Produkt aus.

    Der Kunde legt das Produkt in den Warenkorb.

    Der Kunde gibt seine Bestelldaten ein.

    Der Online-Shop prüft, ob das Produkt auf Lager ist.

    Falls nein:
        Der Online-Shop informiert den Kunden über die Nichtverfügbarkeit.
        Der Vorgang endet.

    Falls ja:
        Der Online-Shop prüft die Zahlungsart.

    Ist die Zahlung erfolgreich?

    Falls ja:
        Der Online-Shop bestätigt die Bestellung.
        Der Kunde erhält eine Bestellbestätigung.

    Falls nein:
        Der Online-Shop informiert den Kunden über die fehlgeschlagene Zahlung.

    Der Vorgang endet.

### Aufgabe 2: Erweiterte Kursanmeldung

Erstellen Sie ein UML-Aktivitätsdiagramm mit zwei Swimlanes (Teilnehmer und Kursverwaltung), das folgenden Ablauf beschreibt:

    Der Teilnehmer wählt einen Kurs aus.

    Der Teilnehmer meldet sich für den Kurs an.

    Die Kursverwaltung prüft, ob noch freie Plätze verfügbar sind.

    Falls nein:
        Die Kursverwaltung informiert den Teilnehmer, dass der Kurs ausgebucht ist.
        Der Vorgang endet.

    Falls ja:
        Die Kursverwaltung prüft, ob die Teilnahmevoraussetzungen erfüllt sind.

    Sind die Voraussetzungen erfüllt?

    Falls ja:
        Die Kursverwaltung bestätigt die Anmeldung.
        Der Teilnehmer erhält eine Anmeldebestätigung.

    Falls nein:
        Die Kursverwaltung informiert den Teilnehmer über fehlende Voraussetzungen.

    Der Vorgang endet.

### Aufgabe 3: 

Für die Entwicklung einer Verwaltungssoftware für eine Bibliothek soll der Ausleih- und Rückgabeprozess modelliert werden.
Dazu soll der Ablauf dieses Prozesses in einem UML-Aktivitätsdiagramm dargestellt werden.

Um den Ablauf vollständig zu erfassen, sind Gespräche mit den beteiligten Stellen erfolgt und Sie haben jeweils folgende Informationen erhalten.

Ausleihtheke:
Ein Benutzer wählt aus dem Bestand der Bibliothek ein Medium aus und geht mit diesem zur Ausleihtheke.
Dort muss er zunächst seinen Benutzerausweis vorlegen. Wenn er noch keinen besitzt, muss er sich zuerst registrieren und erhält einen Benutzerausweis.
Anschließend wird das Medium ausgeliehen. Dazu wird vorher geprüft, ob offene Mahngebühren vorhanden sind. Sind sie vorhanden, müssen sie vor der Ausleihe bezahlt werden. Abschließend wird das Medium im System als ausgeliehen markiert und der Benutzer kann mit dem Medium die Bibliothek verlassen.

Rückgabestelle:
Bei der Rückgabe wird jedes Medium gescannt. Das System prüft dann automatisch, ob die Rückgabe innerhalb der Rückgabefrist erfolgt ist. Bei verspäteter Rückgabe werden Mahngebühren erhoben und dem Benutzerkonto hinzugefügt. Anschließend wird das Medium im System wieder als verfügbar markiert.

Zeichnen Sie mit https://draw.io ein UML-Aktivitätsdiagramm, welches die oben beschriebenen Schritte abbildet.
Exportieren Sie anschließend das Diagramm als URL und fügen Sie diese in das Eingabefeld ein.