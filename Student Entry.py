from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
from email.message import EmailMessage
import ssl
import smtplib
 
 

 

root=Tk()
root.geometry('1250x700')
root.title('Student Data Entry System')
Label(text='Student Data Entry System',
      font=('Felix Titling',30,'bold'),
      bg='#0099cc',fg='white',width=200,height=2).pack()



 

class Database:
    def __init__(self, host, user, password, database):
        self.con = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS data(
            RollNo int primary key,
            RegisterNo int,
            FullName varchar(200),
            DateofBirth varchar(50),
            Gender varchar(200),
            Class varchar(80),
            MobileNo varchar(50),
            FatherName varchar(300),
            MotherName varchar(300)
        );"""
        self.cur.execute(sql)
        self.con.commit()

    # Insert data
    def insert(self, RollNo, RegisterNo, FullName, DateofBirth, Gender, Class, MobileNo, FatherName, MotherName):
        self.cur.execute('INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                         (RollNo, RegisterNo, FullName, DateofBirth, Gender, Class, MobileNo, FatherName, MotherName))
        self.con.commit()

    # Fetch all data
    def fetch(self):
        self.cur.execute('SELECT * FROM data')
        rows = self.cur.fetchall()
        return rows

    # Delete a record from database
    def remove(self, RollNo):
        self.cur.execute('DELETE FROM data WHERE RollNo=%s', (RollNo,))
        self.con.commit()
 
        
    # Update a record in database
    def update(self, RollNo, RegisterNo, FullName, DateofBirth, Gender, Class, MobileNo, FatherName, MotherName):
        self.cur.execute('UPDATE data SET RegisterNo=?, FullName=?, DateOfBirth=?, Gender=?, Class=?, MobileNo=?, FatherName=?, MotherName=? WHERE RollNo=?',
                     (RegisterNo, FullName, DateofBirth, Gender, Class, MobileNo, FatherName, MotherName, RollNo))
        self.con.commit()

# Creating an instance of the Database class
ob = Database('localhost', 'root', 'sahil786', 'studentdata')


 
def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data['values']
    RegisterNo.set(row[1])  
    FullName.set(row[2]) 
    DateofBrith.set(row[3])
    Gender.set(row[4])
    Class.set(row[5])
    MobileNo.set(row[6])
    FatherName.set(row[7])
    MotherName.set(row[8])
     
    

 
def display_data():
     tv.delete(*tv.get_children())
    # Creating an instance of the Database class
     ob = Database('localhost', 'root', 'sahil786', 'studentdata')
    
    # Fetching data
  #data = ob.fetch()
    
    # Displaying data
     for rows in ob.fetch():
         
         tv.insert('',END,value=rows)

         RollNo.set('')


def Save():
    if RollNo.get()=='' or RegisterNo.get()=='' or FullName.get()==''  or DateofBrith.get()=='' or  Gender.get()=='' or  Class.get()=='' or MobileNo.get()=='' or FatherName.get()==''or MotherName.get()=='':
        messagebox.showerror('Erorr','Please Fill All the Details')
        return
    try:
        ob.insert(
            RollNo.get(), RegisterNo.get(), FullName.get(), DateofBrith.get(),
            Gender.get(), Class.get(), MobileNo.get(), FatherName.get(), MotherName.get()
        )
        messagebox.showinfo('Success', 'Data saved successfully!')
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')
    Reset()
    display_data()

 

 
 


def Admission():
    #frame 4 ----->  for admission button

    f4=Frame
    f4=Frame(root,bg='#80dfff',highlightthickness=1,width=300,height=230)
    f4.place(x=940,y=420)
    if RollNo.get() == '' or RegisterNo.get() == '' or FullName.get() == '' or DateofBrith.get() == '' or Gender.get() == '' or Class.get() == '' or MobileNo.get() == '' or FatherName.get() == '' or MotherName.get() == '':
        messagebox.showerror('Error', 'Please Fill All the Details')
        return
    try:
        # Your code for Admission function here
        img_new = Image.open('gpay.png')

        # Resize the image to a new width and height
        new_width = 250
        new_height = 255
        resized_img = img_new.resize((new_width, new_height))

        # Save the resized image to a new file
        resized_img.save('resized_gpay.png')

        # Convert the resized image to a Tkinter PhotoImage object
        image_tk = ImageTk.PhotoImage(resized_img)

        label = Label(f4, image=image_tk) 
        label.image = image_tk   
        label.pack()
 


        btn_pay=Button(f4,text='Pay',font=('STLiti',10,'bold'),bg='#6600cc',fg='white',bd=5,width=5,height=1,command=Pay).place(x=5,y=200)

        btn_cancel=Button(f4,text='Cancel',font=('STLiti',10,'bold'),bg='#00ffff',fg='black',bd=5,width=7,height=1,command=Cancel).place(x=180,y=200)
        # You need to define 'over' somewhere in this function
        over = "admitted"   
        return over
    except Exception as e:
        # Handle any exceptions that might occur
        print("An error occurred in Admission function:", e)

def Pay():
    if RollNo.get()=='' or RegisterNo.get()=='' or FullName.get()==''  or DateofBrith.get()=='' or  Gender.get()=='' or  Class.get()=='' or MobileNo.get()=='' or FatherName.get()==''or MotherName.get()=='':
        messagebox.showerror('Erorr','Please Fill All the Details')
        return
    try:
        email_sender = 'sahiljhusain55@gmail.com'
        email_password = 'lhfc vpno ahdi pgze'
        email_receiver = 'sahiljhusain55@gmail.com'
        subject = 'Admission Process'
        body = '''Your Amount Successfully Received,
        Your Admission Successfully Finished and
        Further Information Management Will Sent Later
        Thank You
        Have a Nice Day'''
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    except smtplib.SMTPAuthenticationError as e:
        # Handle SMTP authentication error
        print("SMTP Authentication Error:", e)
        # Provide instructions to the user on how to fix the issue
        print("Make sure your email username and password are correct.")
        print("Also, check if 'Less secure app access' is enabled in your Gmail settings.")
    except Exception as e:
        # Handle any other exceptions
        print("An error occurred in Pay function:", e)

    except Exception as e:
        print("An error occurred in Pay function:", e)

        
#create new frame 5 ------> cover up pay
 
def Cancel():
    
    f5=Frame
    f5=Frame(root,bg='#80dfff',highlightthickness=1,width=300,height=230)
    f5.place(x=940,y=420)
    
    Label(f5,text='Your Payment Cancel',font=('Rockwell',13,'bold'),bg='#a3c2c2',fg='black').place(x=50,y=100)

    Label(f5,text='Please Try Again',font=('Rockwell',13,'bold'),bg='#a3c2c2',fg='black').place(x=70,y=130)
 
      
    
   
     
    
    
 
     


def Reset():
    RollNo.set('') 
    RegisterNo.set('')  
    FullName.set('') 
    Class.set('')
    DateofBrith.set('')
    Gender.set('')
    MobileNo.set('')
    FatherName.set('')
    MotherName.set('')
     


 
def Search():
    # Clear the existing data in the Treeview
    tv.delete(*tv.get_children())

    # Get the RollNo to search from the Entry widget
    roll_number = RollNo.get()
    print("Searching for RollNo:", roll_number)  

    try:
        # Connect to the database
        connection = mysql.connector.connect(host='localhost', user='root', password='sahil786', database='studentdata')
        
        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Execute a query to select data based on the provided roll number
        query = "SELECT * FROM data WHERE RollNo = %s"   
        cursor.execute(query, (roll_number,))
        
        # Fetch all rows from the query result
        rows = cursor.fetchall()

        for row in rows:
            # Insert each row into the Treeview
            tv.insert('', 'end', values=row)
            print("Found data:", row)  

        if not rows:
            print("No data found for RollNo:", roll_number)  

    except mysql.connector.Error as err:
        print("Error:", err)  
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()






def ShowFees():
    # new root name give as [fees_window] because already create as [root]
    fees_window = tk.Tk()
    fees_window.geometry('1250x700')
    fees_window.title("Fees Information")
    Label(fees_window,text='Tuition Fees Information for All Student',
      font=('Felix Titling',30,'bold'),
      bg='#3d5c5c',fg='white',width=200,height=2).pack()

 
    fn=Frame
    fn=Frame(fees_window,bg='#a3c2c2',highlightthickness=1,width=500,height=500)
    fn.place(x=400,y=130)

    
#title for fees stucture
    
    Label(fn,text='Fees Structure',font=('Algerian',30,'bold'),bg='#a3c2c2',fg='White',width=15,height=1).place(x=50,y=10)



# studend fees enter in fn frame--

    Label(fn,text='*I-Standard - Yearly Fees = RS.15000/-*',font=('Rockwell',15,'bold'),bg='#a3c2c2',fg='black').place(x=50,y=70)

    Label(fn,text='*II-Standard - Yearly Fees = RS.17000/-*',font=('Rockwell',15,'bold'),bg='#a3c2c2',fg='black').place(x=50,y=110)

    Label(fn,text='*III-Standard - Yearly Fees = RS.19000/-*',font=('Rockwell',15,'bold'),bg='#a3c2c2',fg='black').place(x=50,y=150)

    Label(fn,text='*IV-Standard - Yearly Fees = RS.22000/-*',font=('Rockwell',15,'bold'),bg='#a3c2c2',fg='black').place(x=50,y=190)

    Label(fn,text='*V-Standard - Yearly Fees = RS.24000/-*',font=('Rockwell',15,'bold'),bg='#a3c2c2',fg='black').place(x=50,y=230)

    Label(fn,text='*VI-Standard - Yearly Fees = RS.26000/-*',font=('Rockwell',15,'bold'),bg='#a3c2c2',fg='black').place(x=50,y=270)

    Label(fn,text='*VII-Standard - Yearly Fees = RS.28000/-*',font=('Rockwell',15,'bold'),bg='#a3c2c2',fg='black').place(x=50,y=310)

    Label(fn,text='*VIII-Standard - Yearly Fees = RS.30000/-*',font=('Rockwell',15,'bold'),bg='#a3c2c2',fg='black').place(x=50,y=350) 
    
    Label(fn,text='*IX-Standard - Yearly Fees = RS.32000/-*',font=('Rockwell',15,'bold'),bg='#a3c2c2',fg='black').place(x=50,y=390)

    Label(fn,text='*X-Standard - Yearly Fees = RS.35000/-*',font=('Rockwell',15,'bold'),bg='#a3c2c2',fg='black').place(x=50,y=430)



    fees_window.mainloop()
 


 


def Delete():
    ob.remove(row[0])
    Reset()
    display_data()





RollNo=StringVar()
RegisterNo=StringVar()
FullName=StringVar()
Class=StringVar()
DateofBrith=StringVar()
Gender=StringVar()
MobileNo=StringVar()
FatherName=StringVar()
MotherName=StringVar()
 
 

Label(root,text='Student Details:',font=('STLiti',20,'bold'),fg='black',width=15,height=1,anchor=W).pack()


#creating frame 1----> data entry box
f=Frame
f=Frame(root,bg='#80dfff',highlightthickness=1,width=900,height=300)
f.place(x=1,y=130)

#creating frame 2----> for search box
f2=Frame
f2=Frame(root,bg='#80dfff',highlightthickness=1,width=300,height=120)
f2.place(x=940,y=100)


#creating  frame 3---> Delete button
f3=Frame
f3=Frame(root,bg='#80dfff',highlightthickness=1,width=300,height=200)
f3.place(x=940,y=220)


 


#student data -------> label 

Label(f,text='Roll No',font=('STLiti',15,'bold'),bg='#ffbf80',fg='black',width=10,height=1).place(x=5,y=10)

Label(f,text='Register No',font=('STLiti',15,'bold'),bg='#ffbf80',fg='black',width=10,height=1).place(x=300,y=10)

Label(f,text='Full Name',font=('STLiti',15,'bold'),bg='#ffbf80',fg='black',width=10,height=1).place(x=595,y=10)

Label(f,text='Date of Birth',font=('STLiti',15,'bold'),bg='#ffbf80',fg='black',width=10,height=1).place(x=5,y=100)

Label(f,text='Gender',font=('STLiti',15,'bold'),bg='#ffbf80',fg='black',width=10,height=1).place(x=300,y=100)
 
Label(f,text='Class',font=('STLiti',15,'bold'),bg='#ffbf80',fg='black',width=10,height=1).place(x=595,y=100)

Label(f,text='Mobile No',font=('STLiti',15,'bold'),bg='#ffbf80',fg='black',width=10,height=1).place(x=5,y=190)

Label(f,text='Father Name',font=('STLiti',15,'bold'),bg='#ffbf80',fg='black',width=10,height=1).place(x=300,y=190)

Label(f,text='Mother Name',font=('STLiti',15,'bold'),bg='#ffbf80',fg='black',width=10,height=1).place(x=595,y=190)

 







#entry box------>
entry_roll=Entry(f,textvariable=RollNo,bd=5,font=('Georgia',10,'bold'),fg='black',bg='#d9d9d9',width=15).place(x=115,y=10)

entry_name=Entry(f,textvariable=RegisterNo,bd=5,font=('Georgia',10,'bold'),fg='black',bg='#d9d9d9',width=15).place(x=410,y=10)
 
entry_reg=Entry(f,textvariable=FullName,bd=5,font=('Georgia',10,'bold'),fg='black',bg='#d9d9d9',width=15).place(x=710,y=10)

entry_dob=Entry(f,textvariable=DateofBrith,bd=5,font=('Georgia',10,'bold'),fg='black',bg='#d9d9d9',width=15).place(x=120,y=100)
 
#entry_gender=Entry(f,textvariable=Gender,bd=5,font=('Georgia',10,'bold'),fg='black',bg='#d9d9d9',width=15).place(x=410,y=100)

 # combobox for Gender

combogender = ttk.Combobox(f, font=('Georgia', 10, 'bold'), width=15, textvariable=Gender)
combogender['values'] = ('Male', 'Female')
combogender.place(x=415, y=102)




#entry_class=Entry(f,textvariable=Class,bd=5,font=('Georgia',10,'bold'),fg='black',bg='#d9d9d9',width=15).place(x=710,y=100)
 # combobox for class 

comboclass = ttk.Combobox(f, font=('Georgia', 10, 'bold'), width=15, textvariable=Class)
comboclass['values'] = ('I','II','III','IV','V','VI','VII','VII','XI','X')
comboclass.place(x=710, y=102)

entry_mobile=Entry(f,textvariable=MobileNo,bd=5,font=('Georgia',10,'bold'),fg='black',bg='#d9d9d9',width=15).place(x=115,y=190)

entry_fathername=Entry(f,textvariable=FatherName,bd=5,font=('Georgia',10,'bold'),fg='black',bg='#d9d9d9',width=15).place(x=410,y=190)

entry_mothername=Entry(f,textvariable=MotherName,bd=5,font=('Georgia',10,'bold'),fg='black',bg='#d9d9d9',width=15).place(x=710,y=190)

 


# Buttons [update , save , reset]

#btn_update=Button(f,text='Update',font=('STLiti',20,'bold'),bg='#0000cc',fg='white',bd=7,width=15,height=1,command=Update).place(x=20,y=230)

btn_reset=Button(f,text='Reset',font=('STLiti',20,'bold'),bg='red',fg='white',bd=7,width=15,height=1,command=Reset).place(x=20,y=230)

btn_save=Button(f,text='Save',font=('STLiti',20,'bold'),bg='#0000cc',fg='white',bd=7,width=15,height=1,command=Save).place(x=600,y=230)


 
#entry box for [search]  and [close] box button

entry_search=Entry(f2,textvariable=RollNo,bd=5,font=('Georgia',15,'bold'),fg='black',bg='#d9d9d9',width=10).place(x=80,y=20)


btn_search=Button(f2,text='Search',font=('STLiti',12,'bold'),bg='#33cc33',fg='white',bd=5,width=10,height=1,command=Search).place(x=25,y=70)




btn_close=Button(f2,text='Close',font=('STLiti',12,'bold'),bg='red',fg='white',bd=5,width=10,height=1,command=display_data).place(x=180,y=70)

#button for save ,showmore fees and delete

btn_showfees=Button(f3,text='show Fees',font=('STLiti',15,'bold'),bg='#6600cc',fg='white',bd=5,width=15,height=1,command=ShowFees).place(x=70,y=80)

btn_admission=Button(f3,text='Admission',font=('STLiti',15,'bold'),bg='#cc00ff',fg='white',bd=5,width=15,height=1,command=Admission).place(x=70,y=140)

btn_delete=Button(f3,text='Delete',font=('STLiti',15,'bold'),bg='red',fg='white',bd=5,width=15,height=1,command=Delete).place(x=70,y=20)
 







# table for data store in sql

tree_frame=Frame(root,bg='pink')
tree_frame.place(x=2,y=430,width=900,height=215)





# style for database table row and font
style=ttk.Style()
style.configure('mystyle.Treeview',font=('Courier New CE',10),rowheight=50)

#style for table heading
style.configure('mystyle.Treeview.Heading',font=('Courier New CE',15))






tv=ttk.Treeview(tree_frame,column=(1,2,3,4,5,6,7,8,9))
#column name of table
tv.heading('1',text='RollNo')
#column size adjust
tv.column('1',width=100)
tv.heading('2',text='Reg No')
tv.column('2',width=100)
tv.heading('3',text='Name')
tv.column('3',width=100)
tv.heading('4',text='DOB')
tv.column('4',width=100)
tv.heading('5',text='Gender')
tv.column('5',width=100)
tv.heading('6',text='Class')
tv.column('6',width=100)
tv.heading('7',text='Mobile No')
tv.column('7',width=100)
tv.heading('8',text='Father Name')
tv.column('8',width=100)
tv.heading('9',text='Mother Name')
tv.column('9',width=100)
tv['show']='headings'
tv.bind('<ButtonRelease-1>',getData)
tv.pack(fill='x')



# Call the display_data function
 
display_data()



root.mainloop()
