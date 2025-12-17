from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from students import Student
from train import Train
from face_recogonition import Face_Recogonition
from developer import Developer
from attendance import Attendance
from help_desk import Help_Desk
import os


class Recogonition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recogonization system")
        #first image
        img=Image.open("images/collage1.jpg")
        img=img.resize((430, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=430, height=200)
        #second image
        img1=Image.open("images/OIP.jpg")
        img1=img1.resize((430, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=430, y=0, width=430, height=200)

         #third image
        img2=Image.open("images/collage.webp")
        img2=img2.resize((430, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=860, y=0, width=430, height=200)
         #fourth image
        img3=Image.open("images/collage1.jpg")
        img3=img3.resize((430, 200), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1290, y=0, width=430, height=200)

        img4=Image.open("images/white.jpg")
        img4=img4.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img=Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=790)

        title_lbl=Label(bg_img,text="FACE RECOGONITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #Student button
        img5=Image.open("images/user_profile.jpg")
        img5=img5.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        B1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2", bd=0, highlightthickness=0, relief="flat")
        B1.place(x=80, y=50,width=200,height=200)

        B1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        B1_1.place(x=80, y=250,width=200,height=30)

        img6=Image.open("images/attendance1.png")
        img6=img6.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        B2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data, bd=0, highlightthickness=0, relief="flat")
        B2.place(x=400, y=50,width=200,height=200)

        B2_2=Button(bg_img,text="Record Attendance",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        B2_2.place(x=400, y=250,width=200,height=40)

        img7=Image.open("images/attendance_details.png")
        img7=img7.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        B3=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data, bd=0, highlightthickness=0, relief="flat")
        B3.place(x=700, y=50,width=200,height=200)

        B3_3=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        B3_3.place(x=700, y=250,width=200,height=40)

        img8=Image.open("images/help.png")
        img8=img8.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        B4=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data, bd=0, highlightthickness=0, relief="flat")
        B4.place(x=1000, y=50,width=200,height=200)

        B4_4=Button(bg_img,text="Help desk",command=self.help_data,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        B4_4.place(x=1000, y=250,width=200,height=40)

        img9=Image.open("images/shutdown.webp")
        img9=img9.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        B5=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.exit_app, bd=0, highlightthickness=0, relief="flat")
        B5.place(x=1000, y=330,width=200,height=200)

        B5_5=Button(bg_img,text="Exit",cursor="hand2",command=self.exit_app,font=("times new roman",15,"bold"),bg="black",fg="white")
        B5_5.place(x=1000, y=530,width=200,height=40)

        img10=Image.open("images/developeer.jpg")
        img10=img10.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        B6=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data, bd=0, highlightthickness=0, relief="flat")
        B6.place(x=80, y=330,width=200,height=200)

        B6_6=Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        B6_6.place(x=80, y=530,width=200,height=40)

        img11=Image.open("images/images.jpg")
        img11=img11.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        B7=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.open_img, bd=0, highlightthickness=0, relief="flat")
        B7.place(x=400, y=330,width=200,height=200)

        B7_7=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="white")
        B7_7.place(x=400, y=530,width=200,height=40)

        img12=Image.open("images/train_data.jpg")
        img12=img12.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        B8=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.train_data, bd=0, highlightthickness=0, relief="flat")
        B8.place(x=700, y=330,width=200,height=200)

        B8_8=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        B8_8.place(x=700, y=530,width=200,height=40)
        
    def open_img(self):
        os.startfile("data")
        
        
        #============function buttons=========

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        #self.app.train_classifier()

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recogonition(self.new_window) 
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help_Desk(self.new_window)
        
    def exit_app(self):
        self.root.destroy()


if __name__ == '__main__':
    root=Tk()
    obj=Recogonition(root)
    root.mainloop()