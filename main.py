from tkinter import *
# this is for the notebook widget
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import json

win=Tk()

# setting the position and the screen size of GUI
win.geometry("1100x700+0+0") #("width x height + Xoffset + Yoffset")
# fix the size set it to non resizable
win.resizable(height=0,width=0)  # 0,0 means no more it can be resized
# title and logo
win.title('Database')
win.iconbitmap('main_window_icon\\data.ico')
#background color    <widget>.configure(background='black')
win.configure(background='#17141D')
#making a frame
frame=LabelFrame(win,height=440,width=800,padx=10,pady=10)
frame.place(x=150,y=160,height=440,width=800)#in adding height width in place we fix the  height and width other wise the fame will shrink
#--------------------------- Adding Logos and texts --------------------------------
Label(win,text ="EXPLORE",font = ("Times New Roman",22),fg='red',bg='#17141D').place(x=10,y=0)
Label(win,text ="YOUR",font = ("Times New Roman",22),fg='white',bg='#17141D').place(x=10,y=30)
Label(win,text ="POTENTIAL",font = ("Times New Roman",22),fg='red',bg='#17141D').place(x=10,y=60)
#-------------------------
Label(win,text ="CHITKARA UNIVERSITY",font = ("Times New Roman",22),fg='white',bg='#17141D').place(x=360,y=0)
Label(win,text ="STUDENT DATABASE",font = ("Times New Roman",22),fg='white',bg='#17141D').place(x=380,y=100)
#-------------------------
Label(win,text ="Department of Compluter Science and Engineering",font = ("Times New Roman",16),fg='white',bg='#17141D').place(x=320,y=623)
#-------------- Chitkara Logo
logo=ImageTk.PhotoImage(Image.open('Chitkara_logo\\ck.jpg'))
logo_label=Label(image=logo)
logo_label.place(x=963,y=3)
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-------------------------------- Making Notebooks ---------------------------------
tc = ttk.Notebook(frame)
t1 = ttk.Frame(tc)
t2 = ttk.Frame(tc)
t3 = ttk.Frame(tc)
t4 = ttk.Frame(tc)
t5 = ttk.Frame(tc)
t6 = ttk.Frame(tc)
tc.add(t1, text ='New Student')
tc.add(t2, text ='Display')
tc.add(t3, text ='Course Creation')
tc.add(t4, text ='Display Courses')
tc.add(t5, text ='Course Allocation')
tc.add(t6, text ='Students Courses')
tc.pack(expand = 1, fill ="both")
#-----------------------------------------------------------------------------------
#------------------------------- window 1  New Student  ----------------------------
for i in range(6):
    t1.columnconfigure(i,weight=1)#this for loop is to make columns reference:Python Master class
#----------------------------------------------------------------------row 0
ttk.Label(t1,text ="Enter Your Name",font = ("Times New Roman", 12)).grid(column =0,row = 0,columnspan=2,sticky=E, padx = 10, pady = 10)
name=Entry(t1,width=50,borderwidth=2)
name.grid(row=0,column=4,columnspan=2, padx = 10, pady = 10)
#----------------------------------------------------------------------row 1
ttk.Label(t1,text ="Enter Your Roll No",font = ("Times New Roman", 12)).grid(column =0,row = 1,columnspan=2,sticky=E, padx = 10, pady = 10)
rollno=Entry(t1,width=50,borderwidth=2)
rollno.grid(row=1,column=4,columnspan=2, padx = 10, pady = 10)
#----------------------------------------------------------------------row 2
ttk.Label(t1,text ="Choose Your Gender",font = ("Times New Roman", 12)).grid(column =0,row = 2,columnspan=2,sticky=E, padx = 10, pady = 10)

# tristatevalue=0 means unchecked radio button
gender=StringVar()
Radiobutton(t1,text="Male",value="Male",variable=gender,tristatevalue=0,font = ("Times New Roman", 12)).grid(column =4,row = 2,columnspan=1, padx = 10, pady = 10)
Radiobutton(t1,text="Female",value="Female",variable=gender,tristatevalue=0,font = ("Times New Roman", 12)).grid(column =5,row = 2,columnspan=1, padx = 10, pady = 10)
#----------------------------------------------------------------------row 3
ttk.Label(t1,text ="Adress of Correspondance",font = ("Times New Roman", 12)).grid(column =0,row = 3,columnspan=2,sticky=E, padx = 10, pady = 10)
address=Entry(t1,width=50,borderwidth=2)
address.grid(row=3,column=4,columnspan=2, padx = 10, pady = 10)
#----------------------------------------------------------------------row 4
ttk.Label(t1,text ="Phone no",font = ("Times New Roman", 12)).grid(column =0,row = 4,columnspan=2,sticky=E, padx = 10, pady = 10)
phoneno=Entry(t1,width=50,borderwidth=2)
phoneno.grid(row=4,column=4,columnspan=2, padx = 10, pady = 10)
#----------------------------------------------------------------------row 5
# Label 
ttk.Label(t1, text = "Your Batch",font = ("Times New Roman", 12)).grid(column = 0,row = 5,columnspan=2, padx = 10, pady = 10,sticky=E) 
  
n=StringVar() 
batch = ttk.Combobox(t1,state='readonly', width = 18,textvariable=n) 
# Adding combobox drop down list 
batch['values'] = ('2020','2019','2018','2017') 
 
batch.grid(column = 5, row = 5) 
# Shows Computer Science as a default value 
batch.current(0)
#----------------------------------------------------------------------row 6
ttk.Label(t1,text ="Do you Want Hostel",font = ("Times New Roman", 12)).grid(column =0,row = 6,columnspan=2,sticky=E, padx = 10, pady = 10)
hostel=StringVar()
checkbox1= Checkbutton(t1, text = "Yes",variable = hostel, 
                      onvalue = 'yes', 
                      offvalue = 'no', 
                      height = 2, 
                      width = 10)
checkbox1.grid(column =5,row = 6,columnspan=2,sticky=W, padx = 0, pady = 10)
checkbox1.deselect()
#----------------------------------------------------------------------row 7
def clear1():
        name.delete(0,END)
        rollno.delete(0,END)
        address.delete(0,END)
        phoneno.delete(0,END)
def msg_submit():
    # showinfo ,showwarning,showerror,askquestion,askokcancel,askyesno
    messagebox.showinfo("Status", "Record added")
    clear1()
def msg_clear():
        messagebox.showinfo("Status", "Cleared")
        clear1()
def std_det_add():
        d1=name.get()
        d2=rollno.get()
        d3=gender.get() 
        d4=address.get()
        d5=phoneno.get()
        d6=n.get()
        d7=hostel.get()
        d8=False
        if d7=='yes':
                d8=True
        msg_submit()
        r={ "Rollno": d2, "Name": d1,
         "Gender": d3,"address": d4,
         "Phone no": d5, "Batch": " Batch "+d6,
         "Hostel": d8
        }
        with open('Student.json') as f:
                data=json.load(f)
        data["Students"].append(r)
        data_serialise=json.dumps(data, indent=2)

        with open('Student.json','w') as f:
                json.dump(data,f,indent=1)

ttk.Button(t1,text="Submit", width = 18,command=std_det_add).grid(column =3,row = 7,columnspan=1,sticky=W, padx = 10, pady = 10)
ttk.Button(t1,text="Clear", width = 18,command=msg_clear).grid(column =4,row = 7,columnspan=1,sticky=W, padx = 10, pady = 10)





#-----------------------------------------------------------------------------------
#------------------------------Window 2 Diplay -------------------------------------

win2_tree=ttk.Treeview(t2)
# define Our Columns
win2_tree['columns']=('RollNo','Name','Gender','Address','Phoneno','Batch','Hostel')
# Formate Our Columns
win2_tree.column('#0',width=0,minwidth=0)
win2_tree.column('RollNo',width=80,minwidth=80)
win2_tree.column('Name',width=120,minwidth=120)
win2_tree.column('Gender',width=80,minwidth=80)
win2_tree.column('Address',width=120,minwidth=120)
win2_tree.column('Phoneno',width=120,minwidth=120)
win2_tree.column('Batch',width=120,minwidth=120)
win2_tree.column('Hostel',width=80,minwidth=80)
# Create Headings
win2_tree.heading('#0',text="",anchor=W)
win2_tree.heading('RollNo',text="RollNo",anchor=W)
win2_tree.heading('Name',text="Name",anchor=W)
win2_tree.heading('Gender',text="Gender",anchor=W)
win2_tree.heading('Address',text="Address",anchor=W)
win2_tree.heading('Phoneno',text="Phoneno",anchor=W)
win2_tree.heading('Batch',text="Batch",anchor=W)
win2_tree.heading('Hostel',text="Hostel",anchor=W)
#------------ SHOW
def show():
        win2_tree.delete(*win2_tree.get_children())
        # insert data
        with open('Student.json') as f:
                data=json.load(f)
        temp=0
        for i in data['Students']:
                win2_tree.insert(parent='',index='end',iid=temp,text='',values=(i["Rollno"],i["Name"],i["Gender"],i["address"],i["Phone no"],i["Batch"],i['Hostel']))
                temp+=1
        # place
        win2_tree.place(x=0,y=0,width=800)

Button(t2,text="Display",bg='black',fg='white',command=show).place(x=350,y=300)

#-----------------------------------------------------------------------------------
#------------------------------Window 3 Course Creation -------------------------------------



for i in range(6):
    t3.columnconfigure(i,weight=1)#this for loop is to make columns
#---------------------------------------------    row 0
ttk.Label(t3,text ="Course ID",font = ("Times New Roman", 12)).grid(column =1,row = 0,columnspan=2,sticky=E, padx = 10, pady = 45)
courseid=Entry(t3,width=50,borderwidth=2)
courseid.grid(row=0,column=4,columnspan=2, padx = 10, pady = 45)
#---------------------------------------------    row 1
ttk.Label(t3,text ="Course Name",font = ("Times New Roman", 12)).grid(column =1,row = 1,columnspan=2,sticky=E, padx = 10, pady = 5)
coursename=Entry(t3,width=50,borderwidth=2)
coursename.grid(row=1,column=4,columnspan=2, padx = 10, pady = 45)
#---------------------------------------------    row 2
def clear9():
        courseid.delete(0,END)
        coursename.delete(0,END)

def msg_submit1():
    # showinfo ,showwarning,showerror,askquestion,askokcancel,askyesno
    messagebox.showinfo("Status", "Course added")
    clear9()
def msg_clear1():
        messagebox.showinfo("Status", "Cleared")
        clear9()

def course_add():
        e1=courseid.get()
        e2=coursename.get()
        r={"CourseID": e1, "CourseName": e2}
        msg_submit1()
        with open('Course.json') as f:
                data1=json.load(f)
        data1["Courses"].append(r)
        data_serialise=json.dumps(data1, indent=2)

        with open('Course.json','w') as f:
                json.dump(data1,f,indent=1)



ttk.Button(t3,text="Submit",command=course_add, width = 18).grid(column =4,row = 2,columnspan=1,sticky=W, padx = 10, pady = 45)
ttk.Button(t3,text="Clear",command=msg_clear1, width = 18).grid(column =5,row = 2,columnspan=1,sticky=W, padx = 10, pady = 45)




#-----------------------------------------------------------------------------------
#------------------------------Window 4 Display Course -----------------------------
win4_tree=ttk.Treeview(t4)
# define Our Columns
win4_tree['columns']=('CourseID','CourseName')
# Formate Our Columns
win4_tree.column('#0',width=0,minwidth=0)
win4_tree.column('CourseID',width=80,minwidth=80)
win4_tree.column('CourseName',width=120,minwidth=120)
# Create Headings
win4_tree.heading('#0',text="",anchor=W)
win4_tree.heading('CourseID',text="CourseID",anchor=W)
win4_tree.heading('CourseName',text="CourseName",anchor=W)
#------------ SHOW
def show1():
        win4_tree.delete(*win4_tree.get_children())
        # insert data
        with open('Course.json') as f:
                data1=json.load(f)
        temp=0
        for i in data1['Courses']:
                win4_tree.insert(parent='',index='end',iid=temp,text='',values=(i["CourseID"],i["CourseName"]))
                temp+=1
        # place
        win4_tree.place(x=0,y=0,width=800)

Button(t4,text="Display",bg='black',fg='white',command=show1).place(x=350,y=300)

#-----------------------------------------------------------------------------------
#------------------------------Window 5 Course Allocation --------------------------
for i in range(6):
    t5.columnconfigure(i,weight=1)#this for loop is to make columns
#---------------------------------------------    row 0
ttk.Label(t5,text ="Student Roll no",font = ("Times New Roman", 12)).grid(column =1,row = 0,columnspan=2,sticky=E, padx = 10, pady = 45)
rollno1=Entry(t5,width=50,borderwidth=2)
rollno1.grid(row=0,column=4,columnspan=2, padx = 10, pady = 45)
#---------------------------------------------    row 1
ttk.Label(t5,text ="Course Name",font = ("Times New Roman", 12)).grid(column =1,row = 1,columnspan=2,sticky=E, padx = 10, pady = 5)
s=StringVar() 
allocate = ttk.Combobox(t5, state='readonly',width = 48,textvariable=s) 
# Adding combobox drop down list
with open('Course.json') as f:
        data1=json.load(f) 
allo=[]
for i in data1['Courses']:
                allo.append(i['CourseName'])
def refresh():
        #---- Every thing is in global because you know Ritesh the reason if not find out?
        global s
        global allocate
        global allo
        with open('Course.json') as f:
                data2=json.load(f)
        allo=[]
        for i in data2['Courses']:
                allo.append(i['CourseName'])
        allocate['values']=allo

allocate['values'] = allo

allocate.grid(column = 4, row = 1, padx = 10, pady = 5,columnspan=2) 
# Shows Computer Science as a default value 
allocate.current(1)

Button(t5,text="Refresh",bg='black',fg='white',command=refresh).place(x=350,y=300)
#---------------------------------------------    row 2
def clear2():
        rollno1.delete(0,END)

def msg_submit2():
    # showinfo ,showwarning,showerror,askquestion,askokcancel,askyesno
    messagebox.showinfo("Status", "Course allocated")
    clear2()
def msg_clear2():
        messagebox.showinfo("Status", "Cleared")
        clear2()
def return_courseID(cn):
        #--- here this json file is opened in a function to keep the file updated till function is called
        with open('Course.json') as f:
                data5=json.load(f)
        for i in data5['Courses']:
                if i['CourseName']==cn:
                        return i['CourseID']
def course_add1():
        f1=rollno1.get()
        f2=s.get()
        f3=return_courseID(f2)
        r={"Rollno": f1, "CourseID": f3}
        msg_submit2()
        with open('Allocation.json') as f:
                data3=json.load(f)
        data3["Stu_Course"].append(r)
        data_serialise=json.dumps(data3, indent=2)
        with open('Allocation.json','w') as f:
                json.dump(data3,f,indent=1)




ttk.Button(t5,text="Allocate",command=course_add1 ,width = 18).grid(column =4,row = 2,columnspan=1,sticky=W, padx = 10, pady = 45)
ttk.Button(t5,text="Clear", command=msg_clear2,width = 18).grid(column =5,row = 2,columnspan=1,sticky=W, padx = 10, pady = 45)


#-----------------------------------------------------------------------------------
#------------------------------Window 6 Display Course -----------------------------
win6_tree=ttk.Treeview(t6)
# define Our Columns
win6_tree['columns']=('Rollno','CourseID')
# Formate Our Columns
win6_tree.column('#0',width=0,minwidth=0)
win6_tree.column('Rollno',width=80,minwidth=80)
win6_tree.column('CourseID',width=120,minwidth=120)
# Create Headings
win6_tree.heading('#0',text="",anchor=W)
win6_tree.heading('Rollno',text="Rollno",anchor=W)
win6_tree.heading('CourseID',text="CourseID",anchor=W)
#------------ SHOW
def show2():
        win6_tree.delete(*win6_tree.get_children())
        # insert data
        with open('Allocation.json') as f:
                data3=json.load(f)
        temp=0
        for i in data3['Stu_Course']:
                win6_tree.insert(parent='',index='end',iid=temp,text='',values=(i["Rollno"],i["CourseID"]))
                temp+=1
        # place
        win6_tree.place(x=0,y=0,width=800)

Button(t6,text="Display",bg='black',fg='white',command=show2).place(x=350,y=300)




#-----------------------------------------------------------------------------------
#--------------------------------  Notebook Ends  ----------------------------------
#-----------------------------------------------------------------------------------















# to run the application until we quit
win.mainloop()
#---------------------------------------  END  -----------------------------------------------


# ---- if any error related to directory not found comes than change your directory as the path given is relative---
#  --- to know your current working directory use ---
#import os
#print(os.getcwd())