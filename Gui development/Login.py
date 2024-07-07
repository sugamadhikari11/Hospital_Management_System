from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Admin-Login')
root.geometry('925x500+250+100')
root.configure(bg="#E1D9D1")
root.resizable(False,False)

frame = Frame(root,width=350,height=350,bg="#fff")
frame.place(x=300,y=70)

heading = Label(frame, text='LOGIN', fg="#57a1f8", bg='#fff', font=('Microsft YaHei UI Light',23))
heading.place(x=130,y=20)

##############
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,"Username")
       
                    
user =Entry (frame, width=35, fg='black', border=0, bg='#fff', font=('Microsft YaHei UI Light',11))
user.place(x=30,y=105)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg='black').place(x=25, y=125)
###############
def on_enter(e):
    passw.delete(0,'end')
def on_leave(e):
    name=passw.get()
    if name=="":
        passw.insert(0,"Password")

passw =Entry (frame, width=35, fg='black', border=0, bg='#fff', font=('Microsft YaHei UI Light',11))
passw.place(x=30,y=190)
passw.insert(0,'Password')
passw.bind('<FocusIn>', on_enter)
passw.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=210)
###############
def login():
    name=user.get()
    password=passw.get()
    if name=="" or passw=="":
        messagebox.showerror("Error", "Please Enter Username and Password")
    elif name=="admin" and password=="admin":
        screen=Toplevel(root)
        screen.title("Hospital Management System")
        screen.geometry('800x600')
        screen.config(bg="white")
        Label(screen,text="Dashboard", bg='#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)
        screen.mainloop()
    else:
        messagebox.showerror("Error", "Username and Password Doesn't Match")
  
Button(frame,width=20, pady=7, text='Login', bg="#57a1f8", border=0,command=login).place(x=100,y=255)

root.mainloop()