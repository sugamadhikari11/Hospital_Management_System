from person import Person

class Doctor(Person):
    """A class that deals with the Doctor operations"""

    def __init__(self, username, password, first_name, surname, speciality, patient=[], appointment=[]):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """
        super().__init__(username, password, first_name, surname, 'doctor.txt')
        self.__speciality = speciality
        self.__patients=patient
        self.appoinments=appointment


    
    # def full_name(self) :
    #     #ToDo1
    #     """Returns the doctor's full name"""
    #     return f"{self.__first_name} {self.__surname}"
        
        

    # def get_first_name(self) :
    #     #ToDo2
    #     """Returns the doctor's first name"""
    #     return self.__first_name
        

    # def set_first_name(self, new_first_name):
    #     #ToDo3
    #     """Sets the doctor's first name"""
    #     self.__first_name = new_first_name
       
        

    # def get_surname(self) :
    #     #ToDo4
    #     """Returns the doctor's surname"""
    #     return self.__surname

    # def set_surname(self, new_surname):
    #     #ToDo5
    #     """Sets the doctor's surname"""
    #     self.__surname = new_surname
        

    def get_speciality(self) :
        """Returns the doctor's speciality"""
        #ToDo6
        return self.__speciality
        
        

    def set_speciality(self, new_speciality):
        #ToDo7
        """Sets the doctor's speciality"""
        self.__speciality = new_speciality
        
    def add_patient(self, patient_name):
            """Adds a patient to the doctor's list of patients"""
            self.__patients.append(patient_name)

            # update the doctor's file to reflect the change
            with open(self.filename, "r") as file:
                lines = file.readlines()

            for i, line in enumerate(lines):
                if self.username in line:
                    parts = line.strip().split()
                    if len(parts) < 5:
                        print("Error: file format is incorrect")
                        return
                    parts[4] = " ".join([patient.full_name() for patient in self.__patients])
                    lines[i] = " ".join(parts) + "\n"
                    break

            with open(self.filename, "w") as file:
                file.writelines(lines)
        


    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
