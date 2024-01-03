from abc import ABC, abstractmethod
from datetime import datetime

class HealthcareOperation(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Patient(HealthcareOperation):
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.medical_history = []

    def schedule_appointment(self, doctor, appointment_type, appointment_time, *args):
        appointment = appointment_type(self, doctor, appointment_time, *args)
        doctor.schedule_appointment(appointment)
        return appointment

    def add_medical_record(self, record):
        self.medical_history.append(record)

    def view_medical_history(self):
        print(f"\nMedical History for {self.name}:")
        for record in self.medical_history:
            print(record)

    def display_info(self):
        return f"Patient: {self.name}, Contact: {self.contact_info}"

class Doctor(HealthcareOperation):
    def __init__(self, name, contact_info, specialty):
        self.name = name
        self.contact_info = contact_info
        self.specialty = specialty
        self.schedule = []

    def schedule_appointment(self, appointment):
        self.schedule.append(appointment)

    def view_schedule(self):
        print(f"\nSchedule for Dr. {self.name} ({self.specialty}):")
        for appointment in self.schedule:
            print(appointment.display_info())

    def view_patient_history(self, patient):
        print(f"\nPatient History for {patient.name} seen by Dr. {self.name} ({self.specialty}):")
        for record in patient.medical_history:
            print(record)

    def display_info(self):
        return f"Doctor: Dr. {self.name}, Contact: {self.contact_info}, Specialty: {self.specialty}"

class Appointment(HealthcareOperation):
    def __init__(self, patient, doctor, appointment_time, *args):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time

    def display_info(self):
        return f"Appointment with Dr. {self.doctor.name} ({self.doctor.specialty}) at {self.appointment_time}"

class InPersonAppointment(Appointment):
    def __init__(self, patient, doctor, appointment_time, location):
        super().__init__(patient, doctor, appointment_time)
        self.location = location

    def display_info(self):
        return f"In-Person {super().display_info()}, Location: {self.location}"

class VirtualAppointment(Appointment):
    def __init__(self, patient, doctor, appointment_time, platform):
        super().__init__(patient, doctor, appointment_time)
        self.platform = platform

    def display_info(self):
        return f"Virtual {super().display_info()}, Platform: {self.platform}"

class MedicalRecord:
    def __init__(self, patient, doctor, timestamp, diagnosis, prescription):
        self.patient = patient
        self.doctor = doctor
        self.timestamp = timestamp
        self.diagnosis = diagnosis
        self.prescription = prescription

    def __str__(self):
        return f"At {self.timestamp}: Dr. {self.doctor.name} diagnosed {self.patient.name} with {self.diagnosis} and prescribed {self.prescription}"

if __name__ == "__main__":
    patient1 = Patient("Maria Klark", "maria.klark@mail.ru")
    patient2 = Patient("Papa Rimskiy", "papa.rimskiy@gamil.com")

    doctor1 = Doctor("Davit", "davit@yandex.com", "Cardiology")
    doctor2 = Doctor("Lloyd", "lloyd@yandex.com", "Dermatology")

    appointment1 = patient1.schedule_appointment(doctor1, InPersonAppointment, datetime(2022, 2, 1, 10, 0), "Hospital A")
    appointment2 = patient2.schedule_appointment(doctor2, VirtualAppointment, datetime(2022, 2, 2, 11, 0), "TeleHealth Platform")

    record1 = MedicalRecord(patient1, doctor1, datetime(2022, 2, 1, 11, 0), "Heart condition", "Aspirin")
    record2 = MedicalRecord(patient2, doctor2, datetime(2022, 2, 2, 12, 0), "Skin allergy", "Antihistamines")

    patient1.add_medical_record(record1)
    patient2.add_medical_record(record2)

    doctor1.view_schedule()
    doctor2.view_schedule()

    doctor1.view_patient_history(patient1)
    doctor2.view_patient_history(patient2)

    patient1.view_medical_history()
    patient2.view_medical_history()
