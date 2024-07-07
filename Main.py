# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient



def main():
    """
    the main function to be ran when the program runs
    """

    # # Initialising the actors
    # admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    # doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    # patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    # discharged_patients = []
    
    admins=[]
    doctors=[]
    patients=[]
    discharged_patients=[]
 

    with open("admin.txt", 'r') as file:
        line=file.readline()
        while line!='':
            data = line.split()
            admin=Admin(data[0], data[1], data[2])
            admins.append(admin)
            line=file.readline()
       

    
    with open("doctor.txt",'r') as file:
        line=file.readline()
        while line!='':
            data = line.split()
            doctors.append(Doctor(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
            line=file.readline()

    with open("patient.txt",'r') as file:
        line=file.readline()
        while line!='':
            data = line.split()
            patients.append(Patient(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
            line=file.readline()
    with open("discharged_patient.txt", "r") as file:
        line = file.readline()
        while line!='':
            data = line.split()
            discharged_patients.append(Patient(data[0],data[1],data[2],data[3],data[4],data[5]))
            line=file.readline()
    # keep trying to login tell the login details are correct
    
    
    type_user=admin.login()
    
    
        

    if type_user=="admin":
        while True:
            print("Welcome to the admin panel")
            # print the menu
            print('Choose the operation:')
            print(' 1- Register/view/update/delete doctor')
            print(' 2- Register/view patients')
            print(' 3- Assign doctor to a patient')
            print(' 4- Discharge patients')
            print(' 5- View discharged patient')
            print(' 6- Update admin details')
            print(' 7- View management report')
            print(' 8- Quit')

            # get the option
            op = input('Option: ')

            if op == '1':
                # 1- Register/view/update/delete doctor
            #ToDo1
                admin.doctor_management(doctors)

            elif op == '2':
                admin.patient_Mangement(patients, doctors)

            elif op == '3':
                admin.assign_doctor_to_patient(patients, doctors)
            

            elif op == '4':
                while True:
                    op = input('Do you want to discharge a patient(Y/N):').lower()

                    if op == 'yes' or op == 'y':
                        #ToDo3
                        admin.discharge(patients, discharged_patients)
                        break


                    elif op == 'no' or op == 'n':
                        break

                    # unexpected entry
                    else:
                        print('Please answer by yes or no.')
            
            elif op == '5':
                admin.view_discharge(discharged_patients)

            

            elif op == '6':
                admin.update_details()

            elif op == '7':
                admin.management_report()
            
            elif op == '8':
            
                #ToDo5
                break
            


            else:
                # the user did not enter an option that exists in the menu
                print('Invalid option. Try again')
        
    elif type_user=="doctor":
        while True:
            print("Welcome to Doctor Panel")
            doctorname=type_user
            for doctor in doctors:
                if doctor.get_username()==doctorname:
                    now_change=doctor
            #menu
            print('Choose the operation:')
            print(' 1- Change username/password')
            print(' 2- view details')
            print(' 3- Accept patient')
            print(' 4- View patients')
            print(' 5- Quit')
            op= input("Enter your Option: ")
            if op=="1":
                print("Select which one you wanto change?")
                print("1- password")
                print("2- username")
                select =input("input your option: ")
                if select =="1":
                    username=input('Enter the new username: ')
                    if username==input('Confirmed username again: '):
                        print("Confirmed!")
                        now_change.update(now_change.get_username(), username)
                    else:
                        print("Sorry! couldn't be confirmed")
                elif select=="2":
                    password=input("Enter the new password:")
                    if password==input("Confirm password:"):
                        print("Confirmed")
                        now_change.update(now_change.get_password(), password)
                else:
                    print()
            
            elif op==2:
                print("------Your Details----")
                print("   |      Full name             |  Speciality   |           Patients           |         Appoinments        ")
                print(f"{'':3}|{now_change}")
            
            
            elif op=="3":
                
                print("------Your Details----")
                print("   |      Full name             |  Speciality   |           Patients           |         Appoinments        ")
                print(f"{'':3}|{now_change}")

                admin.view(patients)
                patient_index=input("Please enter the patient ID: ")
                try:
                    patient_index=int(patient_index)-1
                    if patient_index not in range(len(patients)):
                        print('The id entered was not found.')
                        break
                except ValueError:
                    print("The id entered is not correct")
                    break
                now_change.add_patient(patients[patient_index].full_name())
                patients[patient_index].link(now_change.full_name())

            elif op=="4":
                print("-------Patient Details------")
                admin.view(patients)
            elif op=="5":
                break
            else:
                print("Invalid Entry")


    elif type_user=="patient":
         while True:
            print("Welcome to Patient Panel")
            patientname=type_user
            for patient in patients:
                if patient.get_username()==patientname:
                    now_change=patient
            #menu
            print('Choose the operation:')
            print(' 1- Change username/password')
            print(' 2- view details')
            print(' 3- Apply appointment')
            print(' 4- Quit')
            op= input("Enter your Option: ")
            if op=="1":
                print("Choose which one to change?")
                print("1- username")
                print("2- password")
                op_s=input("input: ")
                if op_s=="1":
                    username=input('Enter the new username: ')
                    if username==input('Confirmed username again: '):
                        print("Confirmed!")
                        now_change.update(now_change.get_username(), username)
                    else:
                        print("Sorry! couldn't be confirmed")
                elif op_s=="2":
                    password=input("Enter the new password:")
                    if password==input("Confirm password:"):
                        print("Confirmed")
                        now_change.update(now_change.get_password(), password)
                else:
                    print("Field not available")

            elif op=="2":
                print("----Your Details----")
                print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |           Symptoms           |  Appointments   ')
                print(f"{now_change}")
            elif op=="3":
                print("ID |      Full name               |  Speciality   |           Patients           |         Appoinments        ")
                admin.view(doctors)
                doctor_index=input("Please enter the doctor ID: ")
                try:
                    doctor_index=int(doctor_index)-1
                    if admin.find_index(doctor_index, doctors)!=False:
                        doctors[doctor_index].add_patient(now_change.full_name())
                        appointment=input("Enter date and time for appointment:")
                        print("Appointment is now set!")
                        now_change.set_appointment(appointment)
                    else:
                        print("The entered id is not found")
                except ValueError:
                    print("The id entered is incorrect")
            elif op=="5":
                break
            else:
                print("Invalid Option! Please try again.")

 

if __name__ == '__main__':
    main()
