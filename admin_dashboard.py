from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time



class AdminDashboard(tk.Toplevel):
    def __init__(self, master, username):
        self.username = username
        super().__init__(master)
        self.title("Admin Dashboard")
        self.geometry("1366x768")
        self.resizable(0, 0)
        self.state('zoomed')
        self.config(background='#eff5f6')
        
        #header
        self.header = tk.Frame(self, bg='#009df4')
        self.header.place(x=300, y=0, width=1070, height=60)

        self.heading = tk.Label(self.header, text='Admin Dashboard', font=("", 15, "bold"),bg='#009df4')
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

        # Dashboard
        image = Image.open('images/dashboard.png')
        # Resize the image to 25x25 pixels without cropping
        resized_image = image.resize((25, 25), resample=Image.LANCZOS)

        self.dashboardImage = ImageTk.PhotoImage(resized_image)
        self.dashboard = tk.Label(self.sidebar, image=self.dashboardImage, bg='#ffffff')
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = tk.Button(self.sidebar, text="Dashboard", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff')
        self.dashboard_text.place(x=80, y=287)

        # Manage
        self.manageImage = ImageTk.PhotoImage(file='images/manage-icon.png')
        self.manage = tk.Label(self.sidebar, image=self.manageImage, bg='#ffffff')
        self.manage.place(x=35, y=340)

        self.manage_text = tk.Button(self.sidebar, text="Management Report", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff')
        self.manage_text.place(x=80, y=345)

        #doctor panel
        self.doctorheading = tk.Label(self, text='Doctor(Register, view, Update, delete)', font=("", 15, "bold"), bg="#eff5f6")
        self.doctorheading.place(x=325, y=80)

        # Create a canvas with a scrollbar for the doctor
        self.doctor_panel_canvas = tk.Canvas(self, bg='#ffffff', highlightthickness=0)
        self.doctor_panel_canvas.place(x=325, y=120, width=1010, height=150)
        self.doctor_panel_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.doctor_panel_canvas.yview)
        self.doctor_panel_scrollbar.place(x=1335, y=120, height=150)
        self.doctor_panel_canvas.configure(yscrollcommand=self.doctor_panel_scrollbar.set)

        # Create a frame to hold the content of the control panel
        self.doctor_panel_frame = tk.Frame(self.doctor_panel_canvas, bg='#ffffff')
        self.doctor_panel_canvas.create_window((0, 0), window=self.doctor_panel_frame, anchor='nw')

        # Add your content to the doctor panel frame
        with open("doctor.txt", "r") as file:
            data = file.readlines()

        # Loop through the data and display it in the doctor panel frame
        for i in range(len(data)):
            row_data = data[i].strip().split()
            for j in range(len(row_data)):
                label = tk.Label(self.doctor_panel_frame, text=row_data[j],bg='#fff')
                label.grid(row=i+2, column=j+1, padx=10, pady=10)

        # Update the scroll region of the canvas after displaying the data
        self.doctor_panel_canvas.configure(scrollregion=self.doctor_panel_canvas.bbox("all"))
        
        label = tk.Label(self.doctor_panel_frame, text=f"username", bg='#fff')
        label.grid(row=1,column=1,padx=10,pady=10)
        labe2 = tk.Label(self.doctor_panel_frame, text=f"Password", bg='#fff')
        labe2.grid(row=1,column=2,padx=10,pady=10)
        labe3 = tk.Label(self.doctor_panel_frame, text=f"firstname",bg='#fff')
        labe3.grid(row=1,column=3,padx=10,pady=10)
        labe4 = tk.Label(self.doctor_panel_frame, text=f"surname",bg='#fff')
        labe4.grid(row=1,column=4,padx=10,pady=10)
        labe5 = tk.Label(self.doctor_panel_frame, text=f"Speciality",bg='#fff')
        labe5.grid(row=1,column=5,padx=10,pady=10)
        labe6 = tk.Label(self.doctor_panel_frame, text=f"Patient Assigned",bg='#fff')
        labe6.grid(row=1,column=6,padx=10,pady=10)
        labe7 = tk.Label(self.doctor_panel_frame, text=f"Appointments Requests",bg='#fff')
        labe7.grid(row=1,column=7,padx=10,pady=10)



        # Update the scroll region of the canvas when the doctor panel frame changes size
        self.doctor_panel_frame.bind("<Configure>", lambda event: self.doctor_panel_canvas.configure(scrollregion=self.doctor_panel_canvas.bbox("all")))

   
        #Patient panel
        self.patientheading = tk.Label(self, text='Patient(Register, view, Update, delete)', font=("", 15, "bold"), bg="#eff5f6")
        self.patientheading.place(x=325, y=320)

        # Create a canvas with a scrollbar for the patient
        self.patient_panel_canvas = tk.Canvas(self, bg='#ffffff', highlightthickness=0)
        self.patient_panel_canvas.place(x=325, y=350, width=1010, height=150)
        self.patient_panel_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.patient_panel_canvas.yview)
        self.patient_panel_scrollbar.place(x=1335, y=350, height=150)
        self.patient_panel_canvas.configure(yscrollcommand=self.patient_panel_scrollbar.set)

        # Create a frame to hold the content of the patient panel
        self.patient_panel_frame = tk.Frame(self.patient_panel_canvas, bg='#ffffff')
        self.patient_panel_canvas.create_window((0, 0), window=self.patient_panel_frame, anchor='nw')

         # Add your content to the patient panel frame
        with open("patient.txt", "r") as file:
            data = file.readlines()

        for i in range(len(data)):
            row_data = data[i].strip().split()
            for j in range(len(row_data)):
                label = tk.Label(self.patient_panel_frame, text=row_data[j],bg='#fff')
                label.grid(row=i+2, column=j+1, padx=10, pady=10)

        # Update the scroll region of the canvas after displaying the data
        self.patient_panel_canvas.configure(scrollregion=self.patient_panel_canvas.bbox("all"))
        
        label = tk.Label(self.patient_panel_frame, text=f"username")
        label.grid(row=1,column=1,padx=10,pady=10)
        labe2 = tk.Label(self.patient_panel_frame, text=f"Password")
        labe2.grid(row=1,column=2,padx=10,pady=10)
        labe3 = tk.Label(self.patient_panel_frame, text=f"First Name")
        labe3.grid(row=1,column=3,padx=10,pady=10)
        labe4 = tk.Label(self.patient_panel_frame, text=f"Surname")
        labe4.grid(row=1,column=4,padx=10,pady=10)
        labe5 = tk.Label(self.patient_panel_frame, text=f"Doctor Assigned")
        labe5.grid(row=1,column=5,padx=10,pady=10)
        labe6 = tk.Label(self.patient_panel_frame, text=f"Age")
        labe6.grid(row=1,column=6,padx=10,pady=10)
        labe7 = tk.Label(self.patient_panel_frame, text=f"Postcode")
        labe7.grid(row=1,column=7,padx=10,pady=10)
        

        # Update the scroll region of the canvas when the patient panel frame changes size
        self.patient_panel_frame.bind("<Configure>", lambda event: self.patient_panel_canvas.configure(scrollregion=self.patient_panel_canvas.bbox("all")))

   

      

        # self.add_doctor_button = Button(self, text="Add Doctor", command=self.add_doctor)
        # self.add_doctor_button.grid(row=3,column=1)

        # self.add_patient_button = Button(self, text="Add Patient", command=self.add_patient)
        # self.add_patient_button.grid(row=3,colum=2)

        

    def logout(self):
        # Add logout functionality here
        self.destroy()

    def add_doctor(self):
        # Add doctor functionality here
        pass

    def add_patient(self):
        # Add patient functionality here
        pass

