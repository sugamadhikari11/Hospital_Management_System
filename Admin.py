from Doctor import Doctor
from Patient import Patient
from tkinter import *
from login import LoginSystem


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """
        self.__username = username
        self.__password = password
        self.__address =  address


       

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self):
        while True:
            username = input('Enter the username: ')
            password = input('Enter the password: ')
            
            if self.authenticate('admin.txt', username, password):
                return "admin"
            elif self.authenticate('doctor.txt', username, password):
                return "doctor"
            elif self.authenticate('patient.txt', username, password):
                return "patient"
            else:
                print('Login Failed')
            
    def authenticate(self, filename, username, password):
        with open(filename) as file:
            for line in file:
                fields = line.strip().split()
                if len(fields) >= 2 and fields[0] == username and fields[1] == password:
                    return True
        return False

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        print("-----Get Doctor Details-----")
        print('User Name: ', end='')
        username = input()
        print('Password: ', end='')
        password = input()
        print('First Name: ', end='')
        first_name = input()
        print('Surname: ', end='')
        surname = input()
        print('Speciality: ', end='')
        speciality = input()
        return username, password, first_name, surname, speciality
        
        

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input("Enter the operation: ")

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            username, password, first_name, surname, speciality = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if(first_name == doctor.get_first_name() and surname == doctor.get_surname()):
                    print('Name already exists.')
                    #ToDo5
                    name_exists = True
                    break
                # save time and end the loop

            #ToDo6
            # add the doctor ...
            if not name_exists:
                doctors.append(Doctor(first_name, surname, speciality))
                with open("doctor.txt",'a') as file:
                    file.write(f"\n{username} {password} {first_name} {surname} {speciality} patients() doctor_appointment()")
                    file.close()
           
                                                         # ... to the list of doctors
                print('Doctor registered.')
                self.view(doctors)


        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            print('ID |          Full name           |  Speciality           |  Patient           |  Appointment')
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality           |  Patient           |  Appointment')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')

            op = int(input('Input: '))# make the user input lowercase

            #ToDo8
            # if the user chose the first name
            if op == 1:
                new_firstname = input("Enter the new first name : ")
                doctors[index].update(doctors[index].get_first_name(), new_firstname)
                doctors[index].set_first_name(new_firstname)
                print("Your first name is updated.")
                self.view(doctors)
                # if the user chose the surname
            elif op == 2:
                new_surname = input("Enter the new surname : ")
                doctors[index].update(doctors[index].get_surname(), new_surname)
                doctors[index].set_surname(new_surname)
                print("Your surname is updated.")
                self.view(doctors)
                # if the user chose the speciality
            elif op == 3:
                new_spec = input("Enter the new speciality : ")
                doctors[index].update(doctors[index].get_speciality(), new_spec)
                doctors[index].set_speciality(new_spec)
                print("Your speciality is updated.")
                self.view(doctors)
            else:
                print("The id entered is incorrect")

        



        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            index =  int(input('Enter the ID of the doctor to be deleted: '))-1
            doctor_index = self.find_index(index,doctors)

            if doctor_index != False:
                doctors[index].delete_line(index)  
                doctors.pop(index)
                print("Doctor deleted")
            else:
                print('The id entered is incorrect')

            # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def get_new_patient_details(self):
        # Prompt the user to enter details of a new patient
        first_name = input("Enter the first name of the patient: ")
        surname = input("Enter the surname of the patient: ")
        symptoms = input("Enter the symptoms of the patient: ")
        age = int(input("Enter the age of the patient: "))
        phone_number = input("Enter the phone number of the patient: ")
        postcode = input("Enter the postcode of the patient: ")
        username = input("Create a username for the patient: ")
        password = input("Create a password for the patient: ")
        confirm_password = input("Confirm password: ")
        if password == confirm_password:
            return username, password, first_name, surname, age, phone_number, postcode, symptoms
        else:
            print("Passwords do not match.")

    def register_new_patient(self):
        patient_details = self.get_new_patient_details()
        self.patients.append(patient_details)
        with open("patient.txt", "a") as file:
            file.write(" ".join(patient_details) + "\n")
        print("Patient registered successfully.")

    def patient_Mangement(self, patients, doctors):
        print("=== Patient Management System ===")
        print("1. Register new patient")
        print("2. List all patients")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.register_new_patient()
        elif choice == "2":
            self.view_patient()
        elif choice == "3":
            print("Goodbye!")
        else:
            print("Invalid input. Please try again.")   

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        self.view(patients)

        

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode | Symptoms')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures
        

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].full_name()) 
                self.view(patients)
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                print('The patient is now assign to the doctor.')
                print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |           Symptoms           |  Appointments   ')

                self.view(patients)

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
    
        self.view(patients)
        patient_index = input('Please enter the patient ID: ')

        #ToDo12
        patient_index = int(patient_index) -1
        # check if the id is in the list of patients
        if self.find_index(patient_index,patients)!=False:
            discharged_patients.append(patients[patient_index])
            patients.pop(patient_index)
            # patients[patient_index].delete_line(patient_index)
            print('The patient is now discharged.')
            return # stop the procedures
        # if the id is not in the list of doctors
        else:
            print('The id entered was not found.')
 

        

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        self.view(discharged_patients)

        # for patient in discharged_patients:
        #     print(f'{patient.id} | {patient.full_name} | {patient.doctor.full_name} | {patient.age} | {patient.mobile} | {patient.postcode}')
    



    def update_details(self):
       
        """Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        with open("admin.txt", "r") as file:
            admin_data = file.read().strip().split()
        
        if op == 1:
            username1 = input('Enter the new username: ')
            # validate the username
            username2 = input('Enter the new username again: ')
            if(username1 == username2):
                print("Username matched.")
                self.__username = username2
                admin_data[0] = username2
                print("------------------------------")
                print("-----------Username updated--------------")
            else:
                print("Username not matched")   

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                admin_data[1] = password
                print("----------------Password updated---------------")

        elif op == 3:
            print('Please enter the new address: ')
            new_address = input()
            self.address = new_address
            admin_data[2] = new_address

        else:
            print('Invalid input')

        with open("admin.txt", "w") as file:
            file.write(" ".join(admin_data))


    def management_report(self):
        master=Tk()
        win_obj= LoginSystem(master)
        win_obj.run_report(master)
