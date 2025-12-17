from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Developer:
    def __init__(self, root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("Face recogonization system")
       img=Image.open("images/attendance.jpg")
       img=img.resize((510, 200), Image.Resampling.LANCZOS)
       self.photoimg = ImageTk.PhotoImage(img)

       f_lbl=Label(self.root, image=self.photoimg)
       f_lbl.place(x=0, y=0, width=510, height=200)
        #second image
       img1=Image.open("images/attendance2.jpg")
       img1=img1.resize((510, 200), Image.Resampling.LANCZOS)
       self.photoimg1 = ImageTk.PhotoImage(img1)

       f_lbl=Label(self.root, image=self.photoimg1)
       f_lbl.place(x=510, y=0, width=510, height=200)
        #third image
       img2=Image.open("images/attendence_system.jpg")
       img2=img2.resize((510, 200), Image.Resampling.LANCZOS)
       self.photoimg2 = ImageTk.PhotoImage(img2)

       f_lbl=Label(self.root, image=self.photoimg2)
       f_lbl.place(x=1020, y=0, width=510, height=200)
        
        #background image
       img3=Image.open("images/white1.jpg")
       img3=img3.resize((1540, 600), Image.Resampling.LANCZOS)
       self.photoimg3 = ImageTk.PhotoImage(img3)

       f_lbl=Label(self.root, image=self.photoimg3)
       f_lbl.place(x=0, y=200, width=1540, height=600)
        
        #title
       title_lbl=Label(f_lbl,text="INTRODUCTION OF DEVELOPER ",font=("times new roman",35,"bold"),bg="white",fg="red")
       title_lbl.place(x=0,y=0,width=1540,height=45)
       
       main_frame=Frame(f_lbl,bd=2,bg="white")
       main_frame.place(x=500, y=50, width=500, height=520)
       
       #time
       self.time_label = Label(title_lbl, font=("times new roman", 16, "bold"), bg="white", fg="blue")
       self.time_label.place(x=0, y=5, width=225, height=35)
       self.update_time()# Adjust x, y, width, height as needed

       
       img5=Image.open("C:/Users/DIGO/OneDrive/Desktop/Face Recogonization System/images/developerr.jpg")
       img5=img5.resize((200, 200), Image.Resampling.LANCZOS)
       self.photoimg5 = ImageTk.PhotoImage(img5)

       f_lbl=Label(main_frame, image=self.photoimg5)
       f_lbl.place(x=150, y=30, width=200, height=200)
       

# Example: Add a heading label at the top of the window
       label = Label(main_frame, text="Python Developer", font=("times new roman", 20, "bold"), bg="white", fg="green")
       label.place(x=20, y=250, width=460, height=30)
       label = Label(main_frame, text="Bipin Dhakal", font=("times new roman", 18, "bold"), bg="white", fg="green")
       label.place(x=20, y=290, width=460, height=25)
       
       label = Label(main_frame, text="I am a passionate python developer with", font=("times new roman", 18, "bold"), bg="white", fg="black")
       label.place(x=5, y=330, width=460, height=25)
       label = Label(main_frame, text="a strong focus on building user-friendly", font=("times new roman", 18, "bold"), bg="white", fg="black")
       label.place(x=5, y=360, width=460, height=28)
       label = Label(main_frame, text="desktop applications using Tkinter. My", font=("times new roman", 18, "bold"), bg="white", fg="black")
       label.place(x=5, y=390, width=460, height=28)
       label = Label(main_frame, text="expertise lies in designing interactive and", font=("times new roman", 18, "bold"), bg="white", fg="black")
       label.place(x=5, y=420, width=460, height=28)
       label = Label(main_frame, text="effective GUIs that integrate AI", font=("times new roman", 18, "bold"), bg="white", fg="black")
       label.place(x=5, y=450, width=460, height=28)
       label = Label(main_frame, text="technologies such as face recogonition.", font=("times new roman", 18, "bold"), bg="white", fg="black")
       label.place(x=5, y=480, width=460, height=28)
       
    def update_time(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=f"Time: {now}")
        self.root.after(1000, self.update_time)
       
       
       
       
       
       
       
if __name__ == '__main__':
    root=Tk()
    obj=Developer(root)
    root.mainloop()