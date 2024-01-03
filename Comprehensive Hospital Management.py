from abc import ABC, abstractmethod
from datetime import datetime

class Person:
    def __init__(self,name):
        self.name = name


class Patients(Person):
    def __init__(self, name, age, medical_history = None):
        super().__init__(name)
        self.age = age
        self.medical_history = medical_history or []
        
    def add_medical_history(self,entry):
        self.medical_history.append(entry)
        
    

class Doctors(Person):
    def __init__(self, name,contact_info):
        super().__init__(name)
        self.contact_info = contact_info
    
    def manage_appointment(self,patient,date):
        print(f"Appointment scheduled with {patient.name} on {date}.")
            
    

class MedicalStaff(Person):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position
        
    def manage_hospital_operations(self,operation):
        print(f"{self.name} is managing operation.")

        
class MedicalProcedure(ABC):
    
    @abstractmethod
    def perform(self):
        pass
    
class Surgery(MedicalProcedure):
    def __init__(self,name,surgeon,date):
        self.name = name
        self.surgeon = surgeon
        self.date = date
        
    def perform(self):
        print(f"Surgery {self.name} performed by Dr. {self.surgeon} on {self.date}.")
        
class CheckUp(MedicalProcedure):
    def __init__(self,name,doctor,date):
        self.name = name
        self.doctor = doctor
        self.date = date
        
    def perform(self):
        print(f"Chek-Up {self.name} conducted by Dr. {self.doctor} on {self.date}.")


patient = Patients('Davit',20,["Pneumonia"])
doctor = Doctors("Dr.Albert",'444-555-1234')
staff = MedicalStaff('Nurse Grigoryan', 'Registered Nurse')

patient.add_medical_history('Broken arm in 2018')
doctor.manage_appointment(patient,datetime.now())
staff.manage_hospital_operations('Admissions')

surgery = Surgery('Appendectomy','Dr. Voskanyan', datetime.now())
surgery.perform()

checkup = CheckUp('Annual Physical', 'Dr. Gasparyan',datetime.now())
checkup.perform()


