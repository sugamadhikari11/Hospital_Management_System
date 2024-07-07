from person import Person
class Patient(Person):
    """Patient class"""

    def __init__(self, username, password, first_name, surname, age, mobile, postcode, symptoms,doctor="not set", appointment="not set"):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        super().__init__(username, password, first_name, surname,  "patient.txt")
        self.__age=age
        self.__mobile=mobile
        self.__postcode=postcode
        self.symptoms=symptoms


        #ToDo1 done!
        self.__doctor = doctor
        self.appointment=appointment
       
       

    
    # def full_name(self) :
    #     """full name is first_name and surname"""
    #     return self.first_name + " " + self.surname
    #     #ToDo2
    


    # def get_doctor(self) :
    #     """return the doctor name"""
    #     return self.__doctor
    
    #     #ToDo3
        

    def link(self, doctor):
        """Links the patient to a doctor"""
        self.__doctor = doctor

        # update the patients file to reflect the change
        with open(self.filename, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if self.username in line:
                parts = line.strip().split("")
                if len(parts) < 5:
                    print("Error: file format is incorrect")
                    return
                parts[4] = self.__doctor
                lines[i] = "".join(parts) + "\n"
                break

        with open(self.filename, "w") as file:
            file.writelines(lines)

    def print_symptoms(self):
        """prints all the symptom"""
        print(self.first_name, self.surname, self.__age, self.__mobile, self.__postcode, self.__doctor)
        

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
