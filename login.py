from tkinter import *
import tkinter.messagebox
from admin_dashboard import AdminDashboard
from person_dashboard import DoctorDashboard, PatientDashboard

class LoginSystem:
    def __init__(self, master):
        self.master = master
        self.master.title('Login')
        self.master.geometry('925x500+250+100')
        self.master.configure(bg="#E1D9D1")
        self.master.resizable(False, False)


        self.frame = Frame(self.master, width=350, height=350, bg="#fff")
        self.frame.place(x=300, y=70)

        heading = Label(self.frame, text='LOGIN', fg="#57a1f8", bg='#fff', font=('Microsft YaHei UI Light', 23))
        heading.place(x=130, y=20)

        self.username_entry = Entry(self.frame, width=35, fg='black', border=0, bg='#fff', font=('Microsft YaHei UI Light', 11))
        self.username_entry.place(x=30, y=105)
        self.username_entry.insert(0, 'Username')
        self.username_entry.bind('<FocusIn>', self.on_enter)
        self.username_entry.bind('<FocusOut>', self.on_leave)
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=125)
        self.password_entry = Entry(self.frame, width=35, fg='black', border=0, bg='#fff', font=('Microsft YaHei UI Light', 11))
        self.password_entry.place(x=30, y=190)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind('<FocusIn>', self.on_enter)
        self.password_entry.bind('<FocusOut>', self.on_leave)
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=210)

        Button(self.frame, width=20, pady=7, text='Login', bg="#57a1f8", border=0, command=self.login).place(x=100, y=275)

    

    def on_enter(self, e):
        widget = e.widget
        widget.delete(0, 'end')

    def on_leave(self, e):
        widget = e.widget
        name = widget.get()
        if name == "":
            widget.insert(0, "Password" if widget == self.password_entry else "Username")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if self.authenticate('admin.txt', username, password):
            self.open_dashboard("Admin Dashboard",username)
        elif self.authenticate('doctor.txt', username, password):
            self.open_dashboard("Doctor Dashboard",username)
        elif self.authenticate('patient.txt', username, password):
            self.open_dashboard("Patient Dashboard", username)
        else:
            tkinter.messagebox.showerror('Error', 'Invalid username, password combination')

    def authenticate(self, filename, username, password):
        with open(filename) as file:
            for line in file:
                fields = line.strip().split()
                if len(fields) >= 2 and fields[0] == username and fields[1] == password:
                    return True
        return False
           
    
    def open_dashboard(self, title, username):
        if title == "Admin Dashboard":
            # Open the admin dashboard
            admin_dashboard = AdminDashboard(self.master, username)
        elif title == "Doctor Dashboard":
            # Show a message box with the dashboard title
            person_dashboard = DoctorDashboard(self.master, username)
        elif title == "Patient Dashboard":
             # Open the patient dashboard
            person_dashboard = PatientDashboard(self.master, username)
        else:
            tkinter.messagebox.showinfo('Dashboard', f'Welcome to {title}!')

       
    


       
    
    def run_report(self,master):
        master.mainloop()
