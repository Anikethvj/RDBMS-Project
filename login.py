from tkinter import *
from PIL import ImageTk
import numpy as np

class Login:
    def __init__(self,root):

        def login():
            Frame_login=Frame(root,bg="white")
            Frame_login.place(x=150,y=150,height=530,width=500)
            title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
            desc=Label(Frame_login,text="Customer Credentials",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
            lbl_username=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
            txt_username=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
            txt_username.place(x=90,y=170,width=350,height=35)
            lbl_password=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
            txt_password=Entry(Frame_login,font=("times new roman",15),bg="lightgray",show = "*")
            txt_password.place(x=90,y=240,width=350,height=35)
            forget_btn=Button(Frame_login,text="Forget Password?",bg="White",fg="#d77337",bd=0,font=("times new roman",12),command = Forget_Password).place(x=90,y=280)
            login_btn=Button(self.root,text="Login",fg="White",bg="#d77337",font=("times new roman",20)).place(x=200,y=470,width=180,height=35)
            register_btn=Button(self.root,text="Register",fg="White",bg="#d77337",font=("times new roman",20), command = Register).place(x=400,y=470,width=180,height=35) 

        def Register():
            Frame_register=Frame(root,bg="white")
            Frame_register.place(x=150,y=150,height=530,width=500)
            title=Label(Frame_register,text="Register Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
            desc=Label(Frame_register,text="Customer Credentials",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
            lbl_username=Label(Frame_register,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
            txt_username=Entry(Frame_register,font=("times new roman",15),bg="lightgray")
            txt_username.place(x=90,y=170,width=350,height=35)
            lbl_password=Label(Frame_register,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
            txt_password=Entry(Frame_register,font=("times new roman",15),bg="lightgray",show="*")
            txt_password.place(x=90,y=240,width=350,height=35)
            lbl_email=Label(Frame_register,text="Email",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=280)
            txt_email=Entry(Frame_register,font=("times new roman",15),bg="lightgray")
            txt_email.place(x=90,y=310,width=350,height=35)
            lbl_phone=Label(Frame_register,text="Phone",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=350)
            txt_phone=Entry(Frame_register,font=("times new roman",15),bg="lightgray")
            txt_phone.place(x=90,y=380,width=350,height=35)
            register_btn=Button(self.root,text="Register",fg="White",bg="#d77337",font=("times new roman",20), command = login).place(x=300,y=590,width=180,height=35)

        def Forget_Password():
            Frame_Forget_Password=Frame(root,bg="white")
            Frame_Forget_Password.place(x=150,y=150,height=530,width=500)
            title=Label(Frame_Forget_Password,text="Forget Password",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
            desc=Label(Frame_Forget_Password,text="Customer Credentials",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
            lbl_username=Label(Frame_Forget_Password,text="Old Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
            txt_username=Entry(Frame_Forget_Password,font=("times new roman",15),bg="lightgray")
            txt_username.place(x=90,y=170,width=350,height=35)
            lbl_password=Label(Frame_Forget_Password,text="New Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
            txt_password=Entry(Frame_Forget_Password,font=("times new roman",15),bg="lightgray")
            txt_password.place(x=90,y=240,width=350,height=35)
            submit_btn=Button(self.root,text="Submit",fg="White",bg="#d77337",font=("times new roman",20), command = login).place(x=300,y=470,width=180,height=35)

        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.bg=ImageTk.PhotoImage(file="images/Stadium.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        login()

root = Tk()
obj=Login(root)
root.mainloop()