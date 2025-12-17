from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self, root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("Face recogonization system")
       
       
       #=============variables================
       self.attendanceID_var=StringVar()
       self.roll_no_var=StringVar()
       self.name_var=StringVar()
       self.department_var=StringVar()
       self.time_var=StringVar()
       self.date_var=StringVar()
       self.atten_status=StringVar()
        
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
       img3=Image.open("images/background_attendance.jpg")
       img3=img3.resize((1540, 600), Image.Resampling.LANCZOS)
       self.photoimg3 = ImageTk.PhotoImage(img3)

       f_lbl=Label(self.root, image=self.photoimg3)
       f_lbl.place(x=0, y=200, width=1540, height=600)
        
        #title
       title_lbl=Label(f_lbl,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
       title_lbl.place(x=0,y=0,width=1540,height=45)
        
        #frame
       main_frame=Frame(f_lbl,bd=2,bg="white")
       main_frame.place(x=8, y=50, width=1510, height=600)
        
        #left frame
       left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
       left_frame.place(x=5,y=5,width=745,height=520)
        
       img5=Image.open("C:/Users/DIGO/OneDrive/Desktop/Face Recogonization System/images/smart.jpg")
       img5=img5.resize((730, 580), Image.Resampling.LANCZOS)
       self.photoimg5 = ImageTk.PhotoImage(img5)

       f_lbl=Label(left_frame, image=self.photoimg5)
       f_lbl.place(x=5, y=0, width=735, height=130)
        
       left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
       left_inside_frame.place(x=3, y=135, width=735, height=360)
        
        #labels and entry
        #attendanceId
       attendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
       attendanceId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

       attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.attendanceID_var,font=("times new roman",12,"bold"))
       attendanceID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        #roll no
       roll_no_label=Label(left_inside_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
       roll_no_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
       roll_no_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.roll_no_var,font=("times new roman",12,"bold"))
       roll_no_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)  
        
              #name
       name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
       name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)
       name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.name_var,font=("times new roman",12,"bold"))        
       name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
              #department   
       department_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
       department_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
       department_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.department_var,font=("times new roman",12,"bold"))
       department_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
              #time
       time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
       time_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)
       time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.time_var,font=("times new roman",12,"bold"))
       time_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)
              #date
       date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
       date_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)
       date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.date_var,font=("times new roman",12,"bold"))
       date_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)
              #attendance status
       attendancelabel=Label(left_inside_frame,text="Attendance status:",font=("times new roman",12,"bold"),bg="white")
       attendancelabel.grid(row=3,column=0,padx=5)

       self.atten_status=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),width=17,textvariable=self.atten_status,state="readonly")
       self.atten_status["values"]=("Select Status","Present","Absent")
       self.atten_status.current(0)
       self.atten_status.grid(row=3,column=1,pady=8)
        
       btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
       btn_frame.place(x=2,y=320,width=726,height=35)

       save_btn=Button(btn_frame,text="Import csv",width=19,font=("times new roman",12,"bold"),bg="green",fg="white", command=self.import_csv)
       save_btn.grid(row=0,column=0)

       Update_btn=Button(btn_frame,text="Export csv",width=19,font=("times new roman",12,"bold"),bg="green",fg="white",command=self.export_csv)
       Update_btn.grid(row=0,column=1)

       Delete_btn=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="green",fg="white")
       Delete_btn.grid(row=0,column=2)

       reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="green",fg="white")
       reset_btn.grid(row=0,column=3)
       
 
        
        #right frame
       right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
       right_frame.place(x=755,y=5,width=745,height=520)
        
       table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
       table_frame.place(x=2,y=5,width=738,height=445)
        
        #===================scroll bar========================
       table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
       table_frame.place(x=5,y=5,width=738,height=445)

       scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
       self.attendance_table=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command=self.attendance_table.xview)
       scroll_y.config(command=self.attendance_table.yview)
       self.attendance_table.heading("id",text="Attendance ID")
       self.attendance_table.heading("roll",text="Roll No")
       self.attendance_table.heading("name",text="Name")
       self.attendance_table.heading("department",text="Department")
       self.attendance_table.heading("time",text="Time")
       self.attendance_table.heading("date",text="Date")
       self.attendance_table.heading("status",text="Status")
       self.attendance_table["show"]="headings"
       self.attendance_table.column("id",width=100)
       self.attendance_table.column("roll",width=100)
       self.attendance_table.column("name",width=100)
       self.attendance_table.column("department",width=100)
       self.attendance_table.column("time",width=100)
       self.attendance_table.column("date",width=100)
       self.attendance_table.column("status",width=100)
       self.attendance_table.pack(fill=BOTH,expand=1)
       
       self.attendance_table.bind("<ButtonRelease>",self.get_cursor)
       self.fetch_data(mydata)  # Fetch initial data (empty at start)
       #====================fetch data======================== 
    def fetch_data(self, rows):
       self.attendance_table.delete(*self.attendance_table.get_children())
       for i in rows:
         self.attendance_table.insert("",END,values=i)
       #====================import csv========================     
    def import_csv(self):
       global mydata
       mydata.clear()
       fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")))
       with open(fln) as myfile:
           reader=csv.reader(myfile,delimiter=",")
           for i in reader:
              mydata.append(i)
           self.fetch_data(mydata)
           
       #====================export csv========================
    def export_csv(self):
       try:
           if len(mydata)<1:
              messagebox.showerror("No data","No data found to export",parent=self.root)
              return False
           fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")))
           with open(fln,mode="w",newline="") as myfile:
               exp_write=csv.writer(myfile,delimiter=",")
               for i in mydata:
                  exp_write.writerow(i)
               messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
       except Exception as es:
                 messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                 
    def get_cursor(self, event=""):
         cursor_row=self.attendance_table.focus()
         content=self.attendance_table.item(cursor_row)
         row=content["values"]
         self.attendanceID_var.set(row[0])
         self.roll_no_var.set(row[1])
         self.name_var.set(row[2])
         self.department_var.set(row[3])
         self.time_var.set(row[4])
         self.date_var.set(row[5])
         self.atten_status.set(row[6])
         
                 
    def reset_data(self):
         self.attendanceID_var.set("")
         self.roll_no_var.set("")
         self.name_var.set("")
         self.department_var.set("")
         self.time_var.set("")
         self.date_var.set("")
         self.atten_status.set("Select Status")
         self.fetch_data(mydata)
         
                 

        
        
             
if __name__ == '__main__':
    root=Tk()
    obj=Attendance(root)
    root.mainloop()