import pyodbc
import customtkinter as ctk
from tkinter import messagebox

# Connect to your MS SQL Server database
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=LAPTOP-LR7GMOE9\SQLEXPRESS;DATABASE=HandGesture;UID=sa;PWD=12345678')

def insert_user(name, email, username, password, mobile):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (Name, Email, Username, Password, mobile) VALUES (?, ?, ?, ?, ?)", (name, email, username, password, mobile))
    conn.commit()
    messagebox.showinfo("Registered successfully !")
    cursor.close()

window = ctk.CTk()
window.title('Customtkinter app')
window.geometry('800x500')

label = ctk.CTkLabel(window, text='SignUp', font=("Arial", 20, "bold"), text_color="red")
label.pack()

label = ctk.CTkLabel(window, text='Enter your name:', font=("Arial", 14, "bold"))
label.place(x=100, y=50)

label = ctk.CTkLabel(window, text='Enter your Email:', font=("Arial", 14, "bold"))
label.place(x=100, y=100)

label = ctk.CTkLabel(window, text='Enter Mobile No:', font=("Arial", 14, "bold"))
label.place(x=100, y=150)

label = ctk.CTkLabel(window, text='Create a UserName:', font=("Arial", 14, "bold"))
label.place(x=100, y=200)

label = ctk.CTkLabel(window, text='Create a new Password:', font=("Arial", 14, "bold"))
label.place(x=100, y=250)

label = ctk.CTkLabel(window, text='Confirm Password:', font=("Arial", 14, "bold"))
label.place(x=100, y=300)

name_entry = ctk.CTkEntry(window)
name_entry.place(x=300, y=50)

email_entry = ctk.CTkEntry(window)
email_entry.place(x=300, y=100)

mobile_entry = ctk.CTkEntry(window)
mobile_entry.place(x=300, y=150)

username_entry = ctk.CTkEntry(window)
username_entry.place(x=300, y=200)

password_entry = ctk.CTkEntry(window, show="*")  # Show * for password entry
password_entry.place(x=300, y=250)

confirm_password_entry = ctk.CTkEntry(window, show="*")  # Show * for password entry
confirm_password_entry.place(x=300, y=300)

def submit():
    name = name_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    mobile = mobile_entry.get()

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    insert_user(name, email, username, password, mobile)
    window.quit()
    # ctk.messagebox.showinfo("Success", "Registration successful!")

button = ctk.CTkButton(window, text="Submit", command=submit)
button.place(x=200, y=360)

window.mainloop()
