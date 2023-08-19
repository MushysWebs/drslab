#Group 3
#Project: Classes
#August 18, 2023
#Description: Alberta Hospital (AH) is a new healthcare provider in Alberta. To complement the existing large-scale hospitals located in urban settings, AH is building a network of smaller scale mini-hospitals which target underserved rural populations. AH has hired your company to create a management system which is customized to meet their unique operational needs. This program works with two data files to retrieve and edit doctor and patient information.

#Class #1: Doctor
#Doctor constructor class
class Doctor:
    def __init__(self, doctor_id=None, name=None, specialization=None, working_time=None, qualification=None, room_number=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
    
    #getter functions
    def get_doctor_id(self):
        return self.doctor_id
    def get_name(self):
        return self.name
    def get_specialization(self):
        return self.specialization
    def get_working_time(self):
        return self.working_time
    def get_qualification(self):
        return self.qualification
    def get_room_number(self):
        return self.room_number
  
    #setter functions
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id
    def set_name(self, new_name):
        self.name = new_name
    def set_specialization(self, new_specialization):
        self.specialization = new_specialization
    def set_working_time(self, new_time):
        self.working_time = new_time
    def set_qualification(self, new_qualification):
        self.qualification = new_qualification
    def set_room_number(self, new_room_number):
        self.room_number = new_room_number
        
    #string to return representaion of dr object
    def __str__(self):
        return (f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}")






# Class #2: Doctor Manager
class DoctorManager:
    def __init__(self):
        # Creates an empty list of files and calls read_doctor_files
        self.doctors = self.read_doctors_file()
    
    # Gathers doctor information and formats according to the txt file
    def format_dr_info(self, doctor):
        return str(doctor)
    
    # Asks the user to enter doctor details and returns a new Doctor object
    def enter_dr_info(self):
        doctor_id = input("Enter ID: ")
        name = input("Enter Name: ")
        specialization = input("Enter Specialization: ")
        working_time = input("Enter Working Time: ")
        qualification = input("Enter Qualification: ")
        room_number = input("Enter Room Number: ")
        
        return Doctor(doctor_id=doctor_id, name=name, specialization=specialization, working_time=working_time, qualification=qualification, room_number=room_number)
    
    # Reads text in the file and turns it into a list of Doctor objects
    def read_doctors_file(self):
        doctor_list = []
        with open("Final group project\doctors.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split("_")  # Clears white space and adds _ between properties to format how the doctors.txt file is
                if len(parts) == 6:
                    # Variable parts; id, name, specialization, working time, qualification, room number
                    doctor_object = Doctor(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                    doctor_list.append(doctor_object)  # Appends the doctor object to the list
        return doctor_list

    # Searches for a doctor using their ID
    def search_doctor_id(self):
        doctor_id = input("Enter Doctor ID to search: ")
        for identified_doctor in self.doctors:  # identified_doctor is different variable than doctor to avoid loop 
            if identified_doctor.get_doctor_id() == doctor_id:
                self.display_doctor_info(identified_doctor)
                return
        print("Can't find the doctor with the same ID on the system")

    # Searches for a doctor using their name
    def search_doctor_name(self):
        get_name = input("Enter doctor name to search: ")
        for identified_doctor in self.doctors:
            if identified_doctor.get_name() == get_name:
                self.display_doctor_info(identified_doctor)
                return
        print("Can't find the doctor with the same name on the system")

    # Displays doctor information in a structured format
    def display_doctor_info(self, doctor):
        print("Doctor Information:")
        print(f"Doctor ID: {doctor.get_doctor_id()}") 
        print(f"Name: {doctor.get_name()}")
        print(f"Speciality: {doctor.get_specialization()}")
        print(f"Timing: {doctor.get_working_time()}")
        print(f"Qualification: {doctor.get_qualification()}")
        print(f"Room Number: {doctor.get_room_number()}")

    # Asks the user to enter the doctor id which the user wants to edit, searches the list and updates the relevant fields
    def edit_doctor_info(self):
        enter_id = input("Enter doctor ID to edit: ")
        for identified_doctor in self.doctors:
            if identified_doctor.get_doctor_id() == enter_id:
                identified_doctor.name = input("Enter new name: ")
                identified_doctor.specialization = input("Enter new specialization: ")
                identified_doctor.working_time = input("Enter new working time: ")
                identified_doctor.qualification = input("Enter new qualification: ")
                identified_doctor.room_number = input("Enter new room number: ")
                print("Doctor information has been edited.")
                return 
        print("Can't find the doctor...") 


#Class #3: patient
class Patient:
    #Constructor
    def __init__(self, patient_id=None, name=None, disease=None, gender=None, age=None):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    #getters
    def get_patient_ID(self):
        return self.patient_id
    def get_name(self):
        return self.name
    def get_disease(self):
        return self.disease
    def get_gender(self):
        return self.gender
    def get_age(self): 
        return self.age
    #setters
    def set_patient_ID(self, new_id):
        self.patient_id = new_id
    def set_name(self, new_name):
        self.name = new_name
    def set_disease(self, new_disease):
        self.disease = new_disease
    def set_gender(self, new_gender):
        self.gender = new_gender
    def set_age(self, new_age): 
        self.age = new_age

    #string to return representaion of dr object
    def __str__(self):
        return (f"{self.patient_id}_{self.name}_{self.disease}_{self.gender}_{self.age}")


#Class #4: patient Manager
#constructor
class PatientManager:
    def __init__(self):
        self.patients = []
        self.Read_patient_file()

    def format_patient_info_for_file(self, patient):
        return f"{patient.patient_id}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}"

    #enter_patient_Info
    def Enter_patient_info(self):
        patient_id = input("Enter Patient Name ID: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient Disease: ")
        gender = input("Enter Patient Gender: ")
        age = input("Enter Patient Age: ")

        return Patient(patient_id, name, disease, gender, age)

    #read_patients_file
    def Read_patient_file(self):
        try:
            with open('Final group project\patients.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    id, name, disease, gender, age = line.strip().split('_')
                    self.patients.append(Patient(id, name, disease, gender, age))
        except FileNotFoundError:
            pass

    #search_patient_by_Id
    def search_patient_by_Id(self):
        patient_id = input("Enter the patient ID to search: ")
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.display_patient_info(patient)
                return
        print("Can’t find the patient....")

    #display_patient_info
    def display_patient_info(self, patient):
        print(f"ID: {patient.patient_id}\nName: {patient.name}\nDisease: {patient.disease}\nGender: {patient.gender}\nAge: {patient.age}")

    #edit_patient_info_by_id
    def edit_patient_info_by_id(self):
        patient_id = input("Enter the patient ID to edit: ")
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)
        if patient:
            patient.name = input("Enter new name: ")
            patient.disease = input("Enter new disease: ")
            patient.gender = input("Enter new gender: ")
            patient.age = input("Enter new age: ")

            self.write_list_of_patients_to_file()
            print("Patient info has been edited!")
        else:
            print("Cannot find the patient ....")

    #display_patients_list
    def display_patients_list(self):
        for patient in self.patients:
            self.display_patient_info(patient)

    #write_list_of_patients_to_file
    def write_list_of_patients_to_file(self):
        with open('Final group project\patients.txt', 'w') as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient) + '\n')

    #add_patient_to_file
    def add_patient_to_file(self):
        new_patient = self.Enter_patient_info()
        self.patients.append(new_patient)
        with open('Final group project\patients.txt', 'a') as file:
            file.write(self.format_patient_info_for_file(new_patient) + '\n')
        print("A new patient has been added!")



#Class #5: Management
class Management:
    # Constructor
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patientManager = PatientManager()
    
    # display_menu to direct users
    def display_menu(self):
        while True:  # prints main menu
            print("Welcome to Alberta Hospital (AH) Managment system \nSelect from the following options, or select 0 to stop:")
            print("1-   Doctors")
            print("2-   Patients")
            print("3-   Exit")
            choice = input(">>> ")
            
            if choice == "1":
                self.display_doctors_menu()
            elif choice == "2":
                self.display_patients_menu()
            elif choice == "3":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    
    # Display doctors submenu
    def display_doctors_menu(self):
        while True:
            print("\nDoctors Menu: ")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")
            choice = input(">>> ")

            if choice == "1":  # Displays all doctors
                for doctor in self.doctor_manager.doctors:
                    self.doctor_manager.display_doctor_info(doctor)

            elif choice == "2":  # Searches for doctor by Id
                self.doctor_manager.search_doctor_id()

            elif choice == "3":  # Searches for doctor by name
                self.doctor_manager.search_doctor_name()

            elif choice == "4":  # Adds a new doctor
                new_doctor = self.doctor_manager.enter_dr_info()
                self.doctor_manager.doctors.append(new_doctor)
                with open("Final group project\doctors.txt", "a") as file:
                    file.write(str(new_doctor) + "\n")
                print("A new doctor has been added!")

            elif choice == "5":  # Edit the info of a doctor
                self.doctor_manager.edit_doctor_info()

            elif choice == "6":  # Takes user back to the main menu
                return
            else:
                print("Enter a valid option.")
    
    # Display patient submenu
    def display_patients_menu(self):
        while True:  # Prints the menu and stays until 5 has been chosen
            print("Patients Menu: ")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")
            choice = input(">>>")
            
            if choice == "1":  # displays the list of patients
                self.patientManager.display_patients_list()
            
            elif choice == "2":  # searching for a patient by Id
                self.patientManager.search_patient_by_Id()
            
            elif choice == "3":  # adding a new patient
                self.patientManager.add_patient_to_file()
                
            elif choice == "4":  # edit the info of a patient
                self.patientManager.edit_patient_info_by_id()
            
            elif choice == "5":  # takes user back to main menu
                return
            else: 
                print("Enter a valid option.")

def main():
    system = Management()  
    system.display_menu()  # Starting the program

if __name__ == '__main__':
    main()