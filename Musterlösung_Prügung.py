# FISI
'''
Funktion1:
Summiert alle Elemente der übergebenen Liste auf und gibt die Summe zurück.

Funktion2:
Findet in der übergebenen Liste das kleinste Element und gibt dieses zurück.

Funktion3:
Berechnet den Durchschnitt der Elemente der Liste, indem zuerst die Summe der Elemente berechnet wird und durch die Anzahl der Elemente dividiert wird.

Erläutern Sie die sogenannte 3-2-1-Backup-Regel.

3: Es gibt drei Kopien: Original + Zwei Backups
2: Es gibt zwei unterschiedliche Speichermedien, z.B. SSD + Festplatte
1: Es gibt mindestens ein Backup an einem anderen Standort

Erklären Sie den Unterschied zwischen Vollsicherung, differenzieller Sicherung und inkrementeller Sicherung

Vollsicherung: alle Daten werden vollständig gesichert, unabhängig davon welche sich seit der letzten Sicherung geändert haben
Differenzielle Sicherung: sichert die Änderungen seit der letzten Vollsicherung
Inkrementelle Sicherung: sichert die Änderungen ab der letzten Vollsicherung inkrementell, d.h. es werden immer nur die Daten gesichert, die sich seit der letzten (inkrementellen) Sicherung geändert haben.
'''

# Anwendungsentwicklung

'''
class Patient:
    def __init__(self, patient_id, name, required_department : str):
        self.patient_id = patient_id
        self.name = name
        self.required_department = required_department

    # Dient nur zur Ausgabe eines Patienten auf die Kommandozeile
    def __repr__(self):
        return f"Patient {self.patient_id}, Name: {self.name}"


class TreatmentRoom:
    def __init__(self, room_id, department, assigned_patients):
        self.room_id = room_id
        self.department = department
        self.assigned_patients = assigned_patients

    def assign_patient(self, patient):
        self.assigned_patients.append(patient)

    def __repr__(self):
        return f"Raum {self.room_id}, Department {self.department}, Patienten: {self.assigned_patients}"


class MediCareAssignmentSystem:
    def __init__(self, treatment_rooms):
        self.treatment_rooms : list[TreatmentRoom] = treatment_rooms

    def assign_patient_to_room(self, patient : Patient) -> bool:
        for room in self.treatment_rooms:
            if room.department == patient.required_department:
                room.assign_patient(patient)
                return True
        return False


# Beispielverwendung:

kardiologie = TreatmentRoom(1, "Kardiologie", [])
neurologie = TreatmentRoom(2, "Neurologie", [])
radiologie = TreatmentRoom(3, "Radiologie", [])

treatment_rooms = [kardiologie, neurologie, radiologie]

assignment_system = MediCareAssignmentSystem(treatment_rooms)

patient1 = Patient(1, "Max Müller", "Radiologie")

success = assignment_system.assign_patient_to_room(patient1)

# Erwartete Ausgabe: True
print(success)

# Erwartete Ausgabe: "Patient 1, Name: Max Müller"
print(radiologie.assigned_patients[0])
'''
'''
Was ist eine Klasse in der OOP (objektorientierten Programmierung)?
 
Eine Klasse ist ein Bauplan für Objekte. Sie definiert welche Eigenschaften (Attribute) und Fähigkeiten (Methoden) die daraus erstellten Objekte besitzen werden.
 
 
Was ist ein Objekt in der OOP (objektorientierten Programmierung)?
 
Ein Objekt ist eine konkretes Exemplar (Instanz) einer Klasse. Die in der Klasse definierten Attribute besitzen in diesem Exemplar konkrete Werte, die sich von Objekt zu Objekt unterscheiden können.
'''