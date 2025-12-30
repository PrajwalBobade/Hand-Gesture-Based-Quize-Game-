from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import pyodbc
import os


def call_Cloud_script():
    os.system("python HandCode.py Que_CloudComputing.csv")


def call_CG_script():
    os.system("python HandCode.py Que_ComputerGraphics.csv")


def call_android_script():
    os.system("python HandCode.py Que_Android.csv")



value = os.environ['user']

class Dashboard:

    def __init__(self, window):
        self.window = window
        self.window.title('Home Page')
        self.window.geometry('1366x768')
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')

        # Initialize page frames
        self.page_1 = Frame(self.window, bg='green')
        self.page_2 = Frame(self.window, bg='yellow')

        # List of page frames
        self.pages = [self.page_1, self.page_2]


        #************* HEADER ***************

        # self.header = Frame(self.window, bg='#3cb371')
        # self.header.place(x=200, y=0, width=1070, height=60)
        #
        # self.logout_text = Button(self.window, text='Logout', bg='#32cf8e', font=("Open Sans",13,"bold"),
        #                           bd=0, fg='white', cursor='hand2', activebackground='#32cf8e', activeforeground='white')
        # self.logout_text.place(x=1150, y=15)


        #***************** SIDEBAR *********************

        self.sidebar = Frame(self.window, bg='#06639E')
        self.sidebar.place(x=0, y=0, width=250, height=850)


        #************* Main Frame *********************

        self.main_frame = Frame(self.window, bg='#e2e8fe')
        self.main_frame.place(x=250, y=0, width=1280, height=800)

        # self.Home_lb = Label(self.main_frame, text='Home Page', font=("bold",18))
        # self.Home_lb.place(x=100, y=100)



        # self.page_1 = Frame(self.main_frame, bg='green')
        # # self.page_1.place(x=0,y=0, width=1000, height=500)
        # self.page_1_lb = Label(self.page_1, text='Home Page', font=('Bold', 20))
        # self.page_1_lb.place(x=50, y=50)
        #
        #
        # self.page_2 = Frame(self.main_frame, bg='yellow')
        # self.page_2_lb = Label(self.page_2, text='Profile', font=('Bold', 20))
        # self.page_2_lb.place(x=50, y=50)

        # #********************** CARD1 ********************

        card_frame = Frame(self.main_frame, bg='white', width=260, height=340)
        card_frame.place(x=160, y=40)

        image = Image.open("cloudComputing.jpg")  # Replace "example_image.jpg" with your image file
        photo = ImageTk.PhotoImage(image)

        label = Label(card_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.place(x=0, y=0)

        python_label = Label(card_frame, text="Subject : Cloud Computing",
                             font=("Open Sans", 10, "bold"), bg='white')
        python_label.place(x=40, y=230)

        python_label2 = Label(card_frame, text="Total no. of questions : 5",
                              font=("Open Sans", 10, "bold"), bg='white')
        python_label2.place(x=40, y=250)

        button = ctk.CTkButton(card_frame, text='Start Quiz', text_color='white', command=call_Cloud_script, fg_color="#06639E", font=('Microsoft Yahei UI Light',14,'bold'), height=35, width=200 )
        button.place(x=35, y=285)


        #********************** CARD2 ********************

        card_frame = Frame(self.main_frame, bg='white', width=260, height=340)
        card_frame.place(x=510, y=40)

        image = Image.open("computerGraphics.jpg")  # Replace "example_image.jpg" with your image file
        photo = ImageTk.PhotoImage(image)

        label = Label(card_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.place(x=0, y=0)

        python_label = Label(card_frame, text="Subject : Computer Graphics",
                             font=("Open Sans", 10, "bold"), bg='white')
        python_label.place(x=40, y=230)

        python_label2 = Label(card_frame, text="Total no. of questions : 5",
                              font=("Open Sans", 10, "bold"), bg='white')
        python_label2.place(x=40, y=250)

        button = ctk.CTkButton(card_frame, text='Start Quiz', fg_color="#06639E", command=call_CG_script, font=('Microsoft Yahei UI Light',14,'bold'), height=35, width=200)
        button.place(x=35, y=285)

        #********************** CARD3 ********************

        card_frame = Frame(self.main_frame, bg='white', width=260, height=340)
        card_frame.place(x=860, y=40)

        image = Image.open("Android.jpg")  # Replace "example_image.jpg" with your image file
        photo = ImageTk.PhotoImage(image)

        label = Label(card_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.place(x=0, y=0)

        python_label = Label(card_frame, text="Subject : Android Programming",
                             font=("Open Sans", 10, "bold"), bg='white')
        python_label.place(x=40, y=230)

        python_label2 = Label(card_frame, text="Total no. of questions : 5",
                              font=("Open Sans", 10, "bold"), bg='white')
        python_label2.place(x=40, y=250)

        button = ctk.CTkButton(card_frame, text='Start Quiz', fg_color="#06639E", command=call_android_script, font=('Microsoft Yahei UI Light',14,'bold'), height=35, width=200)
        button.place(x=35, y=285)


        #********************** CARD4 ********************

        card_frame = Frame(self.main_frame, bg='white', width=260, height=340)
        card_frame.place(x=280, y=450)

        image = Image.open("cyberForensic.jpg")  # Replace "example_image.jpg" with your image file
        photo = ImageTk.PhotoImage(image)

        label = Label(card_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.place(x=0, y=0)

        python_label = Label(card_frame, text="Subject : Cyber Forensic",
                             font=("Open Sans", 10, "bold"), bg='white')
        python_label.place(x=40, y=230)

        python_label2 = Label(card_frame, text="Total no. of questions : 5",
                              font=("Open Sans", 10, "bold"), bg='white')
        python_label2.place(x=40, y=250)

        button = ctk.CTkButton(card_frame, text='Start Quiz', fg_color="#06639E", font=('Microsoft Yahei UI Light',14,'bold'), height=35, width=200)
        button.place(x=35, y=285)

        #********************** CARD5 ********************

        card_frame = Frame(self.main_frame, bg='white', width=260, height=340)
        card_frame.place(x=665, y=450)

        image = Image.open("Asp.jpg")  # Replace "example_image.jpg" with your image file
        photo = ImageTk.PhotoImage(image)

        label = Label(card_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.place(x=0, y=0)

        python_label = Label(card_frame, text="Subject : ASP.NET & C#",
                             font=("Open Sans", 10, "bold"), bg='white')
        python_label.place(x=40, y=230)

        python_label2 = Label(card_frame, text="Total no. of questions : 5",
                              font=("Open Sans", 10, "bold"), bg='white')
        python_label2.place(x=40, y=250)

        button = ctk.CTkButton(card_frame, text='Start Quiz', fg_color="#06639E", font=('Microsoft Yahei UI Light',14,'bold'), height=35, width=200)
        button.place(x=35, y=285)

        #logo
        self.logoImage = Image.open('hyy1.png')
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo, bg='#06639E')
        self.logo.image= photo
        self.logo.place(x=50, y=80)



        # Name of User

        self.username = Label(self.sidebar, text=value, bg='#06639E', font=("Open Sans",15,"bold"), fg='white')
        self.username.place(x=65, y=200)

        # # Home Page logo
        # self.homeImage = Image.open('dashboard-icon.png')
        # photo = ImageTk.PhotoImage(self.homeImage)
        # self.home = Label(self.sidebar, image=photo, bg='#ffffff', width=20, height=50)
        # self.home.image= photo
        # self.home.place(x=45, y=289)

        self.home_text = Button(self.sidebar, text='Home', bg='#06639E', font=("Open Sans", 22, "bold"),
                                cursor='hand2', activebackground='#07639d', activeforeground='white', bd=0, fg='white', command=self.home_page)
        self.home_text.place(x=80, y=300)

        # # Profile logo
        # self.profileImage = Image.open('profileImg1.png')
        # photo = ImageTk.PhotoImage(self.profileImage)
        # self.profile = Label(self.sidebar, image=photo, bg='#ffffff')
        # self.profile.image = photo
        # self.profile.place(x=45, y=360)

        self.profile_text = Button(self.sidebar, text='Profile', bg='#06639E', font=("Open Sans", 22, "bold"),
                                cursor='hand2', activebackground='#07639d', activeforeground='white', bd=0, fg='white', command=self.profile_page)
        self.profile_text.place(x=80, y=370)

        # About us logo
        # self.profileImage = Image.open('profileImg1.png')
        # photo = ImageTk.PhotoImage(self.profileImage)
        # self.profile = Label(self.sidebar, image=photo, bg='#ffffff')
        # self.profile.image = photo
        # self.profile.place(x=45, y=390)

        self.profile_text = Button(self.sidebar, text='About', bg='#06639E', font=("Open Sans", 22, "bold"),
                                cursor='hand2', activebackground='#07639d', activeforeground='white', bd=0, fg='white', command=self.about_page)
        self.profile_text.place(x=80, y=440)


        self.profile_text = Button(self.sidebar, text='Logout', bg='#06639E', font=("Open Sans", 22, "bold"),
                                cursor='hand2', activebackground='#07639d', activeforeground='white', bd=0, fg='white', command=self.logout)
        self.profile_text.place(x=80, y=510)

        # Exit logo
        # self.exitImage = Image.open('exit-icon.png')
        # photo = ImageTk.PhotoImage(self.exitImage)
        # self.exit = Label(self.sidebar, image=photo, bg='#ffffff')
        # self.exit.image = photo
        # self.exit.place(x=30, y=410)

        self.exit_text = Button(self.sidebar, text='Exit', bg='#06639E', font=("Open Sans", 22, "bold"),
                                cursor='hand2', activebackground='#07639d', activeforeground='white', bd=0, fg='white', command=self.exit_app)
        self.exit_text.place(x=80, y=580)

    # def change_page_to_profile(self):
    #     for p in self.pages:
    #         p.place_forget()
    #
    #     self.page_2.place(x=0, y=0, width=1000, height=500)
    #
    #
    # def change_page_to_home(self):
    #     for p in self.pages:
    #         p.place_forget()
    #
    #     self.page_1.place(x=0, y=0, width=1000, height=500)

    def home_page(self):
        home_frame = Frame(self.window, bg='#e2e8fe')
        home_frame.place(x=250, y=0, width=1280, height=800)

        # #********************** CARD1 ********************

        card_frame = Frame(home_frame, bg='white', width=260, height=340)
        card_frame.place(x=160, y=40)

        image = Image.open("cloudComputing.jpg")  # Replace "example_image.jpg" with your image file
        photo = ImageTk.PhotoImage(image)

        label = Label(card_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.place(x=0, y=0)

        python_label = Label(card_frame, text="Subject : Cloud Computing",
                             font=("Open Sans", 10, "bold"), bg='white')
        python_label.place(x=40, y=230)

        python_label2 = Label(card_frame, text="Total no. of questions : 5",
                              font=("Open Sans", 10, "bold"), bg='white')
        python_label2.place(x=40, y=250)

        button = ctk.CTkButton(card_frame, text='Start Quiz', text_color='white', command=call_Cloud_script,
                               fg_color="#06639E", font=('Microsoft Yahei UI Light', 14, 'bold'), height=35, width=200)
        button.place(x=35, y=285)

        # ********************** CARD2 ********************

        card_frame = Frame(home_frame, bg='white', width=260, height=340)
        card_frame.place(x=510, y=40)

        image = Image.open("computerGraphics.jpg")  # Replace "example_image.jpg" with your image file
        photo = ImageTk.PhotoImage(image)

        label = Label(card_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.place(x=0, y=0)

        python_label = Label(card_frame, text="Subject : Computer Graphics",
                             font=("Open Sans", 10, "bold"), bg='white')
        python_label.place(x=40, y=230)

        python_label2 = Label(card_frame, text="Total no. of questions : 5",
                              font=("Open Sans", 10, "bold"), bg='white')
        python_label2.place(x=40, y=250)

        button = ctk.CTkButton(card_frame, text='Start Quiz', fg_color="#06639E", command=call_CG_script,
                               font=('Microsoft Yahei UI Light', 14, 'bold'), height=35, width=200)
        button.place(x=35, y=285)

        # ********************** CARD3 ********************

        card_frame = Frame(home_frame, bg='white', width=260, height=340)
        card_frame.place(x=860, y=40)

        image = Image.open("Android.jpg")  # Replace "example_image.jpg" with your image file
        photo = ImageTk.PhotoImage(image)

        label = Label(card_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.place(x=0, y=0)

        python_label = Label(card_frame, text="Subject : Android Programming",
                             font=("Open Sans", 10, "bold"), bg='white')
        python_label.place(x=40, y=230)

        python_label2 = Label(card_frame, text="Total no. of questions : 5",
                              font=("Open Sans", 10, "bold"), bg='white')
        python_label2.place(x=40, y=250)

        button = ctk.CTkButton(card_frame, text='Start Quiz', fg_color="#06639E", command=call_android_script,
                               font=('Microsoft Yahei UI Light', 14, 'bold'), height=35, width=200)
        button.place(x=35, y=285)

        # ********************** CARD4 ********************

        card_frame = Frame(home_frame, bg='white', width=260, height=340)
        card_frame.place(x=280, y=450)

        image = Image.open("cyberForensic.jpg")  # Replace "example_image.jpg" with your image file
        photo = ImageTk.PhotoImage(image)

        label = Label(card_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.place(x=0, y=0)

        python_label = Label(card_frame, text="Subject : Cyber Forensic",
                             font=("Open Sans", 10, "bold"), bg='white')
        python_label.place(x=40, y=230)

        python_label2 = Label(card_frame, text="Total no. of questions : 5",
                              font=("Open Sans", 10, "bold"), bg='white')
        python_label2.place(x=40, y=250)

        button = ctk.CTkButton(card_frame, text='Start Quiz', fg_color="#06639E",
                               font=('Microsoft Yahei UI Light', 14, 'bold'), height=35, width=200)
        button.place(x=35, y=285)

        # ********************** CARD5 ********************

        card_frame = Frame(home_frame, bg='white', width=260, height=340)
        card_frame.place(x=665, y=450)

        image = Image.open("Asp.jpg")  # Replace "example_image.jpg" with your image file
        photo = ImageTk.PhotoImage(image)

        label = Label(card_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.place(x=0, y=0)

        python_label = Label(card_frame, text="Subject : ASP.NET & C#",
                             font=("Open Sans", 10, "bold"), bg='white')
        python_label.place(x=40, y=230)

        python_label2 = Label(card_frame, text="Total no. of questions : 5",
                              font=("Open Sans", 10, "bold"), bg='white')
        python_label2.place(x=40, y=250)

        button = ctk.CTkButton(card_frame, text='Start Quiz', fg_color="#06639E",
                               font=('Microsoft Yahei UI Light', 14, 'bold'), height=35, width=200)
        button.place(x=35, y=285)

    def profile_page(self):

        new_frame1 = Frame(self.window, bg="white")
        new_frame1.place(x=250, y=0, width=1350, height=860)

        score_frame = ctk.CTkScrollableFrame(new_frame1, width=480, fg_color='#fffadd')
        score_frame.place(x=620, y=380)

        info_frame = ctk.CTkFrame(new_frame1,width=430, fg_color='#ffe6e2')
        info_frame.place(x=110, y=380)

        info_heading = Label(new_frame1, text='User Info', font=('Open Sans',20,'bold'), fg="firebrick1", bg='white')
        info_heading.place(x=40, y=275)

        score_heading = Label(new_frame1, text='Attempt History', font=('Open Sans', 20, 'bold'), fg="firebrick1", bg='white')
        score_heading.place(x=550, y=270)

        user_nm = os.environ['user']
        # Connect to SQL Server
        conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=LAPTOP-LR7GMOE9\SQLEXPRESS;DATABASE=HandGesture;UID=sa;PWD=12345678')


        cursor = conn.cursor()

        # Execute SQL query to fetch one row
        cursor.execute("SELECT TOP 1 Name, Username, Email, mobile FROM Users WHERE Username=?",(user_nm))

        # Fetch one row
        user_row = cursor.fetchone()

        cursor.close()

        cursor1 = conn.cursor()



        # Execute a query
        cursor1.execute(
            "SELECT Quizname, Totalquestion, Score, QuizDate FROM QuizResult where Username=? order by QuizDate desc",
            (user_nm))

        # Fetch all rows
        rows = cursor1.fetchall()

        # Close the cursor and connection
        cursor1.close()

        # Close connection
        conn.close()

        # Custom header names
        custom_headers = ["Subject", "   Questions   ", "Score", "Date"]  # Replace with your custom header names

        # Create labels for custom column headers with custom font size and color
        for i, header in enumerate(custom_headers):
            header_label = Label(score_frame, text=header, font=('Helvetica', 12, 'bold'), fg='blue', bg='#fffadd', height="2")
            header_label.grid(row=0, column=i)  # Place headers in the first row



        if rows:
            # Create labels for each row
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    result = str(value).split('.')[0]
                    label = Label(score_frame, text=result, borderwidth=1, relief="solid", padx=15, pady=15, bd=0,
                                     bg='#fffadd', fg='black', font=('Times New Roman', 12))
                    label.grid(row=i + 1, column=j)  # Start from row 1 to leave space for headers
        else:
            Label(score_frame, text="No data found", padx=15, pady=15).grid(row=1, column=0,
                                                                             columnspan=len(custom_headers))

        logoimage1 = Image.open('hyy1.png')
        photo = ImageTk.PhotoImage(self.logoImage)
        logo = Label(new_frame1, image=photo, bg='#ffffff')
        logo.image= photo
        logo.place(x=500, y=60)

        prof_lb = Label(new_frame1, text='Profile', font=('Open Sans', 20, 'bold'), bg='white')
        prof_lb.place(x=530,y=170)


        lb_name = Label(info_frame, text="Name :", font=('Microsoft Yahei UI Light',11,'bold'), bg='#ffe6e2')
        lb_name.place(x=30,y=15)

        lb_username = Label(info_frame, text="Username :", font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#ffe6e2')
        lb_username.place(x=30, y=55)

        lb_email = Label(info_frame, text="Email:", font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#ffe6e2')
        lb_email.place(x=30, y=95)

        lb_mobile = Label(info_frame, text="Mobile No.:", font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#ffe6e2')
        lb_mobile.place(x=30, y=135)

        # Print data in specified format
        if user_row:
            name = Label(info_frame, text=user_row[0], font=('Microsoft Yahei UI Light',11,'bold'), bg='#ffe6e2')
            name.place(x=200, y=15)
            frame1 = Frame(info_frame, width=340, height=2, bg='#D3D3D3')
            frame1.place(x=20,y=50)
            username = Label(info_frame, text=user_row[1], font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#ffe6e2')
            username.place(x=200, y=55)
            frame1 = Frame(info_frame, width=340, height=2, bg='#D3D3D3')
            frame1.place(x=20, y=90)
            email = Label(info_frame, text=user_row[2], font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#ffe6e2')
            email.place(x=200, y=95)
            frame1 = Frame(info_frame, width=340, height=2, bg='#D3D3D3')
            frame1.place(x=20, y=130)
            mobile = Label(info_frame, text="7758936519", font=('Microsoft Yahei UI Light', 11, 'bold'), bg='#ffe6e2')
            mobile.place(x=200, y=135)
            frame1 = Frame(info_frame, width=340, height=2, bg='#D3D3D3')
            frame1.place(x=20, y=130)
        else:
            print("No data found")
    #
    # # Create labels for custom column headers with custom font size and color
    # for i, header in enumerate(custom_headers):
    #     header_label = tk.Label(new_frame, text=header, font=('Helvetica', 12, 'bold'), fg='blue')
    #     header_label.grid(row=0, column=i)  # Place headers in the first row
    #
    # if rows:
    #     # Create labels for each row
    #     for i, row in enumerate(rows):
    #         for j, value in enumerate(row):
    #             label = tk.Label(new_frame, text=value, borderwidth=1, relief="solid", padx=15, pady=15, bd=0, bg='red',
    #                              fg='white')
    #             label.grid(row=i + 1, column=j)  # Start from row 1 to leave space for headers
    # else:
    #     tk.Label(new_frame, text="No data found", padx=15, pady=15).grid(row=1, column=0,
    #                                                                      columnspan=len(custom_headers))

    def about_page(self):

        new_frame2 = Frame(self.window)

        lb = Label(new_frame2, text='About us\n\n page', font=('bold', 30), bg='orange')

        lb.place(x=200,y=200)

        new_frame2.place(x=250, y=0, width=1050, height=660)


    def printHello(self):
        print("Clicked")

    def logout(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to logout?")
        if confirm:
            self.window.destroy()  # Close the current window
            os.system('python LoginPage.py')  # Run the LoginPage.py file

    def exit_app(self):
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to Exit?")
        if confirm:
            self.window.destroy()  # Close the current window


def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()



if __name__ == '__main__':
    win()


