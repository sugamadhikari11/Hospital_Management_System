import tkinter as tk

from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time

class DoctorDashboard(tk.Toplevel):
    def __init__(self, master, username):
        self.username = username
        super().__init__(master)
        self.title("Doctor Dashboard")
        self.geometry("1366x768")
        self.resizable(0, 0)
        self.state('zoomed')
        self.config(background='#eff5f6')

        #header
        self.header = tk.Frame(self, bg='#009df4')
        self.header.place(x=300, y=0, width=1070, height=60)

        self.heading = tk.Label(self.header, text='Doctor Dashboard', font=("", 15, "bold"),bg='#009df4')
        self.heading.place(x=10, y=15)

        self.logout_text = tk.Button(self.header, text="Logout", bg='#32cf8e', font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#32cf8e', command=self.logout)
        self.logout_text.place(x=950, y=15)

        #sidebar
        self.sidebar = tk.Frame(self, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        #sidebar content
        
        # logo
        logoimage = Image.open('images/profile.png')
        # Resize the image to 25x25 pixels without cropping
        resized_image = logoimage.resize((100, 100), resample=Image.LANCZOS)
        
        self.logoImage = ImageTk.PhotoImage(resized_image)
        self.logo = tk.Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        self.logo.place(x=90, y=80)

        # Name of brand/person
        self.userName = tk.Label(self.sidebar, text=f'{self.username}', bg='#ffffff', font=("", 15, "bold"))
        self.userName.place(x=90, y=200)

    def logout(self):
        # Add logout functionality here
        self.destroy()
        
    def add_patient(self):
        # Add patient functionality here
        pass

class PatientDashboard(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Patient Dashboard")

        self.message_label = tk.Label(self, text="Welcome to the Patient Dashboard!")
        self.message_label.pack()

        self.view_appointments_button = tk.Button(self, text="View Appointments", command=self.view_appointments)
        self.view_appointments_button.pack()

    def view_appointments(self):
        # View appointments functionality here
        pass