from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recogonization system")

        #===== variables========
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_division=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()
        self.var_search_type = StringVar()

        
        img=Image.open("C:/Users/DIGO/OneDrive/Desktop/Face Recogonization System/images/Student.jpg")
        img=img.resize((430, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=430, height=200)
        #second image
        img1=Image.open("C:/Users/DIGO/OneDrive/Desktop/Face Recogonization System/images/smartstudents.webp")
        img1=img1.resize((430, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=430, y=0, width=430, height=200)

         #third image
        img2=Image.open("C:/Users/DIGO/OneDrive/Desktop/Face Recogonization System/images/collage.webp")
        img2=img2.resize((430, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=860, y=0, width=430, height=200)
         #fourth image
        img3=Image.open("C:/Users/DIGO/OneDrive/Desktop/Face Recogonization System/images/student.jpg")
        img3=img3.resize((430, 200), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1290, y=0, width=430, height=200)
        
        img4=Image.open("C:/Users/DIGO/OneDrive/Desktop/Face Recogonization System/images/attendence_system.jpg")
        img4=img4.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img=Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=790)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="grey")
        main_frame.place(x=5,y=50,width=1510,height=650)

        #left level frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=5,width=740,height=520)

        img5=Image.open("C:/Users/DIGO/OneDrive/Desktop/Face Recogonization System/images/smart.jpg")
        img5=img5.resize((730, 580), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        f_lbl=Label(left_frame, image=self.photoimg5)
        f_lbl.place(x=5, y=10, width=730, height=130)

        #current course
        current_course=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course.place(x=5,y=135,width=730,height=110)
        #Department 

        dep_label=Label(current_course,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_department,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","Civil","Electronics","Electrical","mechanical","Automobile","Geomatics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5)
         
         #Course
        course_label=Label(current_course,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE","ME","CE","GE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5)

        #year
        year_label=Label(current_course,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=5)

        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5)

        #semester
        semester_label=Label(current_course,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(current_course,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","1st-Semester","2nd-Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5)

        #Class Student Information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=245,width=730,height=250)

        #student_ID

        StudentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=5)

        StudentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=5)

         #student Name

        Student_Name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        Student_Name_label.grid(row=0,column=2,padx=10)

        Student_Name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        Student_Name_entry.grid(row=0,column=3,padx=10)

         #Class Division

        Class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        Class_div_label.grid(row=1,column=0,padx=10)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_division,font=("times new roman",12,"bold"),width=17,state="readonly")
        div_combo["values"]=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5)
        

        #Roll No.

        roll_no_label=Label(class_student_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll_no,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10)

        #Gender

        Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10)

        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5)
        

        #Date of Birth

        dob_label=Label(class_student_frame,text="Date of Birth:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10)

        #Email Address

        email_label=Label(class_student_frame,text="Email Address:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5)

        #Phone No.

        Phone_No_label=Label(class_student_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        Phone_No_label.grid(row=4,column=0,padx=10)

        Phone_No_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        Phone_No_entry.grid(row=4,column=1,padx=10)

        #Address.

        Address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=4,column=2,padx=10)

        Address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        Address_entry.grid(row=4,column=3,padx=10)

        #Teacher Name

        Teacher_Name_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        Teacher_Name_label.grid(row=3,column=2,padx=10)

        Teacher_Name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        Teacher_Name_entry.grid(row=3,column=3,padx=10)

        #radio buttons
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take sample photo",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=10,pady=3)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No sample photo",value="No")
        radiobtn2.grid(row=5,column=1,padx=10,pady=3)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=180,width=722,height=25)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="green",fg="white", command=self.update_data)
        Update_btn.grid(row=0,column=1)

        Delete_btn=Button(btn_frame,text="Delete",width=19,font=("times new roman",12,"bold"),bg="green",fg="white", command=self.delete_data)
        Delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=19,font=("times new roman",12,"bold"),bg="green",fg="white", command=self.reset_data)
        reset_btn.grid(row=0,column=3)


        btn1_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=3,y=205,width=722,height=25)

        photo_sample_btn=Button(btn1_frame,command=self.generate_dataset,text="Take_photo sample",width=39,font=("times new roman",12,"bold"),bg="green",fg="white")
        photo_sample_btn.grid(row=0,column=0)

        Update_photo_btn=Button(btn1_frame,text="Update a sample photo",width=39,font=("times new roman",12,"bold"),bg="green",fg="white")
        Update_photo_btn.grid(row=0,column=1)



        #right level frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=5,width=740,height=520)

        img6=Image.open("C:/Users/DIGO/OneDrive/Desktop/Face Recogonization System/images/students.jpg")
        img6=img6.resize((730, 580), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        f_lbl=Label(right_frame, image=self.photoimg6)
        f_lbl.place(x=5, y=5, width=730, height=130)



       # =======Search System=======
       #Class Student Information
        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=140,width=730,height=70)

        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        Search_label.grid(row=0,column=0,padx=10,pady=5)

        Search_combo=ttk.Combobox(Search_frame, textvariable=self.var_search_type, font=("times new roman",12,"bold"),width=15,state="readonly")
        Search_combo["values"]=("Select","Roll No.","Phone_no.")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=5)

        self.search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        self.search_entry.grid(row=0,column=2,padx=4)

        Search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="green",fg="white",command=self.search_data)
        Search_btn.grid(row=0,column=3,padx=4)

        Show_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="green",fg="white",command=self.show_all)
        Show_btn.grid(row=0,column=4,padx=4)
         
        #=======table frame========
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=220,width=730,height=270)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Id","Department","Course","year","semester","Name","division","Gender","Roll No.","DOB","Email","Phone No.","address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Id",text="Student_id")
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("division",text="Division")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Roll No.",text="roll_no")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone No.",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("Id",width=100)
        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("division",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Roll No.",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone No.",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        #show message
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogonizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_department.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_division.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_roll_no.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("success","student detailshas been added successfullly!",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root) 
        
        
        
    # ======================= fetch data ================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogonizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
    #===================get cursor ====
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_std_id.set(data[0]),
        self.var_department.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_division.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_roll_no.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
                 
    # ========  update function ========
    def update_data(self):
        if self.var_department.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogonizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s, Course=%s, Year=%s, semester=%s, student_name=%s, division=%s, gender=%s, roll_no=%s, dob=%s, email_address=%s, phone_no=%s, address=%s, teacher=%s, photo_sample_status=%s where student_id=%s",(
                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                        self.var_department.get(),
                                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                                        self.var_division.get(),
                                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                                        self.var_roll_no.get(),
                                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                                                    ))
                else:
                    if  not Update:
                        return
                messagebox.showinfo("Success","Student dteails successfully update completed.",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
    
    
    #======= search function ======
    def search_data(self):
        search_type = self.var_search_type.get()
        search_value = ""
        if search_type == "Roll No.":
           search_value = self.search_entry.get()
           column = "roll_no"
        elif search_type == "Phone_no.":
           search_value = self.search_entry.get()
           column = "phone_no"
        else:
           messagebox.showerror("Error", "Please select a valid search type.", parent=self.root)
           return

        if search_value == "":
           messagebox.showerror("Error", "Please enter a value to search.", parent=self.root)
           return

        try:
           conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recogonizer")
           my_cursor = conn.cursor()
           query = f"SELECT * FROM student WHERE {column}=%s"
           my_cursor.execute(query, (search_value,))
           data = my_cursor.fetchall()
           if len(data) != 0:
               self.student_table.delete(*self.student_table.get_children())
               for i in data:
                   self.student_table.insert("", END, values=i)
               conn.commit()
           else:
               messagebox.showerror("Error", "No record found", parent=self.root)
           conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
            
    #======= show all function ======
    def show_all(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recogonizer")
            my_cursor = conn.cursor()   
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()     
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
            
            
    
    # ====== Delete function =====
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Student details delete","Do you want to delete this student",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogonizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details.",parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                
    #  ====== Reset data =======
    def reset_data(self):
        self.var_department.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_division.set("Select Division")
        self.var_roll_no.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
                
                                        
    #==================== Generate dataset  take poto samples =========== 
    def generate_dataset(self):
        if self.var_department.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogonizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s, Course=%s, Year=%s, semester=%s, student_name=%s, division=%s, gender=%s, roll_no=%s, dob=%s, email_address=%s, phone_no=%s, address=%s, teacher=%s, photo_sample_status=%s where student_id=%s",(
                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                        self.var_department.get(),
                                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                                        self.var_division.get(),
                                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                                        self.var_roll_no.get(),
                                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
    # ===== load predefined data on face frontals from opencv=======
                
                face_classifier=cv2.CascadeClassifier(r"C:/Users/DIGO/OneDrive/Desktop/Face Recogonization System/haarcascade_frontalface_default.xml")
                if face_classifier.empty():
                    messagebox.showerror("Error","face cascade classifier xml file not found",parent=self.root)
                    
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3 and minimum neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if not ret:
                        print("Failed to capture image")
                        continue
                    cropped = face_cropped(my_frame)
                    if cropped is not None:
                        img_id += 1
                        face = cv2.resize(cropped, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"C:/Users/DIGO/OneDrive/Desktop/Face Recogonization System/data/user.{str(id)}.{str(img_id)}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                    else:
    # Optionally show the original frame or a message
                        cv2.imshow("Cropped Face", my_frame)
                        
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generated datasets completed successfully!!") 
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)    
                
                         



if __name__ == '__main__':
    root=Tk()
    obj=Student(root)
    root.mainloop()