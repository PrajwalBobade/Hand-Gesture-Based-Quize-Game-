from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pyodbc
import os
import customtkinter as ctk


def call_other_script():
    # Add code to call another script (if needed)
    login_window.destroy()
    os.system('python HomePage.py')

def signup_page():
    os.system('python DatabaseRegestration.py')


#functionality part


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0,END)
    passwordEntry.configure(show='*')

def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    os.environ['user'] = usernameEntry.get()


    # Establish a connection to the database
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server Native Client 11.0};SERVER=LAPTOP-LR7GMOE9\SQLEXPRESS;DATABASE=HandGesture;UID=sa;PWD=12345678')
        cursor = connection.cursor()

        # Execute a query to check if the username and password exist in the users table
        cursor.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?", (username, password))
        row = cursor.fetchone()

        if row:
            # messagebox.showinfo("Login Successful", "Welcome!")
            call_other_script()  # Call another script upon successful login
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

        connection.close()
    except pyodbc.Error as e:
        messagebox.showerror("Database Error", f"Error: {str(e)}")



# GUI Part
login_window = Tk()
login_window.geometry('890x500+50+50')
login_window.resizable(0,0)
login_window.title('Login page')
login_window.configure(bg="white")

bgImage = ImageTk.PhotoImage(file='login.png')

bgLabel = Label(login_window, image=bgImage, bd=0)
bgLabel.place(x=50, y=90)

bgImage2 = ImageTk.PhotoImage(file='LoginHeading.JPG')

bgLabel2 = Label(login_window, image=bgImage2, bd=0)
bgLabel2.place(x=5, y=10)

bgImage3 = ImageTk.PhotoImage(file='LoginBtn.JPG')



new_frame = ctk.CTkFrame(login_window, width=340, height=400, fg_color='white', corner_radius=20)
new_frame.place(x=490,y=80)




# Title = Label(login_window, text='Virtual Quiz Platform', font=('Helvetica',28,'bold'),
#               bg='#FFEEDC', fg='black')
# Title.place(x=130, y=50)

heading = Label(new_frame, text='Sign In', font=('Arial Black',20,'bold'), bg='white', fg='black')
heading.place(x=110, y=35)

usernameEntry = Entry(new_frame, width=25, font=('Microsoft Yahei UI Light',11,'bold'), bd=0, fg='black', bg="white")
usernameEntry.place(x=50, y=120)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(new_frame, width=250, height=2, bg='#06639E')
frame1.place(x=50, y=142)

passwordEntry = Entry(new_frame, width=25, font=('Microsoft Yahei UI Light',11,'bold'), bd=0, fg='black', bg="white")
passwordEntry.place(x=50, y=185)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(new_frame, width=250, height=2, bg='#06639E')
frame2.place(x=50, y=207)

# openeye = PhotoImage(file='openeye.png')
# eyeButton = Button(new_frame, image=openeye, bd=0, bg="white", activebackground='white', cursor='hand2', command=hide )
# eyeButton.place(x=269, y=181)

# forgetButton = Button(new_frame, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2',
#                       font=('Microsoft Yahei UI Light',9,'bold'), fg='firebrick1', activeforeground='firebrick1')
# forgetButton.place(x=190, y=220)

loginButton = Button(new_frame, image=bgImage3, font=('Open Sans',16,'bold'),
                     fg='white', bg='#06639E', activebackground='#06639E',
                     activeforeground='white', cursor='hand2', bd=0, width=245, command=login)
loginButton.place(x=50, y=260)

signupLabel = Label(new_frame, text='Don\'t have an account?',font=('Open Sans',9,'bold'), fg='firebrick1', bg='white')
signupLabel.place(x=70, y=330)

newaccountButton = Button(new_frame, text='SignUp', font=('Open Sans',9,'bold underline'),
                     fg='blue', bg='white', activebackground='white',
                          cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=210, y=328)


login_window.mainloop()