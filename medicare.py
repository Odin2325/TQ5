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
        pass # TO DO


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