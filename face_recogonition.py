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


class Face_Recogonition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recogonization system")
        
        title_lbl=Label(self.root,text="FACE RECOGONITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        #first image
        img_top=Image.open("images/recogonition.jpg")
        img_top=img_top.resize((765, 750), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=765, height=750)
        #second image
        img_top1=Image.open("images/recogonition1.jpg")
        img_top1=img_top1.resize((765, 750), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl=Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=765, y=45, width=765, height=750)
        
        B1_1=Button(f_lbl,text="Face Recogonition",cursor="hand2",font=("times new roman",18,"bold"),bg="green",fg="white",command=self.face_recog)
        B1_1.place(x=280, y=620,width=200,height=40)
        
    #============attendance=============
    def mark_attendance(self, i, r, n, d):
        try:
            now = datetime.now()
            today_str = now.strftime("%d/%m/%Y")
            already_today = set()
            # Read existing attendance for today
            if os.path.exists("Attendance.csv"):
                with open("Attendance.csv", "r", newline="\n") as f:
                    for line in f:
                        entry = line.strip().split(",")
                        if len(entry) > 5 and entry[0] != "" and entry[5] == today_str:
                            already_today.add(entry[0])
            # Only write if this student ID is not already present for today
            if i not in already_today:
                dtString = now.strftime("%H:%M:%S")
                with open("Attendance.csv", "a", newline="\n") as f:
                    f.write(f"{i},{r},{n},{d},{dtString},{today_str},Present\n")
        except Exception as e:
            print(f"Error marking attendance: {e}")
                
                  
        
        
    #   ====== face recogonition ======
    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogonizer")
                my_cursor=conn.cursor()
                    
                
                my_cursor.execute("select student_name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n = n[0] if n else ""
                
                
                my_cursor.execute("select roll_no from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r = r[0] if r else ""  
                my_cursor.execute("select Department from student where student_id="+str(id))
                d=my_cursor.fetchone() 
                d = d[0] if d else ""
                
                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i = i[0] if i else ""


                if confidence>77:
                    cv2.putText(img,f"ID.:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll No.:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,0,0),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recogonition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                        
                        
        #face_recog(self)           
    #   ====== face recogonition ======
        #face_recog(self)
        
        
        
        
        
        
if __name__ == '__main__':
    root=Tk()
    obj=Face_Recogonition(root)
    root.mainloop()