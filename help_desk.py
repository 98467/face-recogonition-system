from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
from time import strftime
from datetime import datetime


class Help_Desk:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recogonization system")
        
        
        #first image
        img_top=Image.open("images/help_deskk.png")
        img_top=img_top.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1530, height=790)
        
        label = Label(self.root, text="bipindhakal445@gmail.com", font=("times new roman", 18, "bold"), bg="white", fg="black")
        label.place(x=700, y=450, width=445, height=28)
        label = Label(self.root, text="+977-9846643479", font=("times new roman", 18, "bold"), bg="white", fg="black")
        label.place(x=690, y=485, width=355, height=28)
        



if __name__ == '__main__':
    root=Tk()
    obj=Help_Desk(root)
    root.mainloop()