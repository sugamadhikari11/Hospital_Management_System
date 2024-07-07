class Person:
    def __init__(self, username, password, first_name, surname, filename):
        self.first_name = first_name
        self.surname = surname
        self.username = username
        self.password = password
        self.filename = filename
    
    def full_name(self) :
        #ToDo1
        """Returns the doctor's full name"""
        return f"{self.first_name} {self.surname}"
    
    def get_first_name(self) :
        #ToDo2
        """Returns the doctor's first name"""
        return self.first_name
        
    def set_first_name(self, new_first_name):
        #ToDo3
        """Sets the doctor's first name"""
        self.first_name = new_first_name
       
    def get_surname(self) :
        #ToDo4
        """Returns the doctor's surname"""
        return self.surname

    def set_surname(self, new_surname):
        #ToDo5
        """Sets the doctor's surname"""
        self.surname = new_surname
    
    def update(self, old_value, new_value):
        """Updates the details of the person in a file of the specified type"""
        with open(self.filename, "r") as file:
            lines = file.readlines()
        
        for i, line in enumerate(lines):
            if self.username in line:
                parts = line.strip().split(":")
                if len(parts) < 4:
                    print("Error: file format is incorrect")
                    return
                if parts[2] == old_value:
                    parts[2] = new_value
                    lines[i] = ":".join(parts) + "\n"
                    break
        
        with open(self.filename, "w") as file:
            file.writelines(lines)
    
    def delete_line(self, line_number):
        """Deletes the specified line from the file"""
        with open(self.filename, "r") as file:
            lines = file.readlines()
            
        with open(self.filename, "w") as file:
            for i, line in enumerate(lines):
                if i != line_number:
                    file.write(line)


    def appointments(self):
        # View or manage the appointments of the person
        pass