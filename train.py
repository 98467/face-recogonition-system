from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os


class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recogonization system")
        
        
        title_lbl=Label(self.root,text="Train Dataset",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top_left=Image.open("images/training3.jpg")
        img_top_left=img_top_left.resize((1530, 330), Image.Resampling.LANCZOS)
        self.photoimg_top_left = ImageTk.PhotoImage(img_top_left)

        f_lbl=Label(self.root, image=self.photoimg_top_left)
        f_lbl.place(x=0, y=45, width=1530, height=330)
        
        # button
        B1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        B1_1.place(x=0, y=375,width=1530,height=40)
        
        img_bottom=Image.open("images/photos.jpg")
        img_bottom=img_bottom.resize((1530, 330), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=410, width=1530, height=340)
        
        
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)] # get all files in the data directory
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') # grayscale image
            
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
            
        ids = np.array(ids)
        #training the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        #saving the trained classifier
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")
            
        
        
        
        
        
        
        
if __name__ == '__main__':
    root=Tk()
    obj=Train(root)
    root.mainloop()