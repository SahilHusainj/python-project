from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry('1100x560')
root.title('Billing System')
root.resizable(False,False)
image_label = ''


def Reset():
    entry_sandwich.delete(0,END)
    entry_cheeseburger.delete(0,END)
    entry_vegburger.delete(0,END)
    entry_vegpizza.delete(0,END)
    entry_bbqburger.delete(0,END)
    entry_bbqpizza.delete(0,END)
    entry_cocacola.delete(0,END)
    entry_pepsi.delete(0,END)


def Total():
    try:a1=int(Sandwich.get())
    except:a1=0
    try:a2=int(CheeseBurger.get())
    except:a2=0
    try:a3=int(VegBurger.get())
    except:a3=0
    try:a4=int(VegPizza.get())
    except:a4=0
    try:a5=int(BBQBurger.get())
    except:a5=0
    try:a6=int(BBQPizza.get())
    except:a6=0
    try:a7=int(CocaCola.get())
    except:a7=0
    try:a8=int(Pepsi.get())
    except:a8=0
    c1=40*a1
    c2=120*a2
    c3=100*a3
    c4=100*a4
    c5=170*a5
    c6=150*a6
    c7=100*a7
    c8=100*a8
     
    
#total topic with function
    lbl_total=Label(f2,font=('Script MT Bold',20,'bold'),text='Total',
                    bg='red',fg='black',width='12')
    lbl_total.place(x=50,y=90)
#total amount entry box
    entry_total=Entry(f2,font=('Script MT Bold',20,'bold'),
            textvariable=Total_bill,bd=5,
            bg='white',fg='black',width='10')
    entry_total.place(x=70,y=135)

#total amount function    
    totalvalue=c1+c2+c3+c4+c5+c6+c7+c8
    string_bill='Rs.',str('%.2f'%totalvalue)
    Total_bill.set(string_bill)
    return totalvalue

#---------------------------------------------------------------------------------------------------------------------------------------#
# add a page
def showmore():
    totalvalue=Total()
    if totalvalue==0:
        print('Total is Zero')
    else:
        global image_label  # Declare image_label as a global variable
        image_path = 'C:/python/files/rcode.png'
        original_image = Image.open(image_path)
        image_resize = original_image.resize((400, 400))
        tk_image = ImageTk.PhotoImage(image_resize)
        image_label = Label(root, image=tk_image)
        image_label.image = tk_image
        root.resizable(False, False)
        image_label.pack()
        root.mainloop()
def total_enter(e):
    Total()
root.bind('<Return>',total_enter)
     

# create a title for project
Label(text='BBQ BURGER BOX',
      font=('Algerian',30,'bold'),
      bg='#ff1a1a',fg='white',width='300',height='2').pack()
f=Frame
f=Frame(root,bd=5,bg='#ffcc99',
        highlightthickness=1,width='300',height='350')
f.place(x=10,y=118)

#menu card
Label(f,font=('Felix Titling',15,'bold'),
       fg='black',text='Menu',bg='#ffcc99').place(x=100,y=0)

Label(f,font=('Felix Titling',10,'bold'),
       fg='black',text='Sandwich-------------------------->>>>Rs:40',
      bg='#ffcc99').place(x=0,y=50)

Label(f,font=('Felix Titling',10,'bold'),
       fg='black',text='Cheese Burger--------------->>>>Rs:120',
      bg='#ffcc99').place(x=0,y=80)

Label(f,font=('Felix Titling',10,'bold'),
       fg='black',text='Veggie Burger--------------->>>>Rs:100',
      bg='#ffcc99').place(x=0,y=110)

Label(f,font=('Felix Titling',10,'bold'),
       fg='black',text='Veggie Pizza------------------->>>>Rs:100',
      bg='#ffcc99').place(x=0,y=140)


Label(f,font=('Felix Titling',10,'bold'),
       fg='black',text='BBQ Burgur------------------->>>>Rs:170',
      bg='#ffcc99').place(x=0,y=170)


Label(f,font=('Felix Titling',10,'bold'),
       fg='black',text='BBQ Pizza------------------------>>>>Rs:150',
      bg='#ffcc99').place(x=0,y=200)


Label(f,font=('Felix Titling',10,'bold'),
       fg='black',text='CoCa Cola-------------------->>>>Rs:100',
      bg='#ffcc99').place(x=0,y=230)

Label(f,font=('Felix Titling',10,'bold'),
       fg='black',text='Pepsi--------------------------------->>>>Rs:100',
      bg='#ffcc99').place(x=0,y=260)


Label(f,font=('Felix Titling',10,'bold'),
       fg='#ff0000',text='<<<<---------Your Presence At-------->>>>',
      bg='#ffcc99').place(x=0,y=290)


Label(f,font=('Felix Titling',10,'bold'),
       fg='#ff0000',text='<<<<---------BBQ Burger Box--------->>>>',
      bg='#ffcc99').place(x=0,y=310)
# frame 2 create
f1=Frame(root,bd=5,
        width='350',height='350',relief=RAISED)
f1.place(x=350,y=118)

'''Label(f1,font=('Felix Titling',15,'bold'),
       fg='white',text='List',
      bg='black').place(x=60,y=10)

Label(f1,font=('Felix Titling',15,'bold'),
       fg='white',text='Quantity',
      bg='black').place(x=200,y=10)'''
Sandwich=StringVar()
CheeseBurger=StringVar()
VegBurger=StringVar()
VegPizza=StringVar()
BBQBurger=StringVar()
BBQPizza=StringVar()
CocaCola=StringVar()
Pepsi=StringVar()
Total_bill=StringVar()

Label(f1,font=('Felix Titling',15,'bold'),
       fg='white',text='List',
      bg='black',width='6').grid(row=1,column=0)

Label(f1,font=('Felix Titling',15,'bold'),
       fg='white',text='Quantity',
      bg='black').grid(row=1,column=1)

lbl_sandwich=Label(f1,text='Sandwich',font=('STLiti',15,'bold'),
               fg='white',bg='#669999',width='20')
lbl_sandwich.grid(row=2,column=0)

#Entry box for sandwich
entry_sandwich=Entry(f1,textvariable=Sandwich,bd=5,
                     font=('STLiti',15,'bold'),
               fg='white',bg='#c61aff',width='10')

entry_sandwich.grid(row=2,column=1)



lbl_cheeseburger=Label(f1,text='Cheese Burger',font=('STLiti',15,'bold'),
               fg='white',bg='#669999',width='20')
lbl_cheeseburger.grid(row=3,column=0)

entry_cheeseburger=Entry(f1,textvariable=CheeseBurger,bd=5,
                     font=('STLiti',15,'bold'),
               fg='white',bg='#c61aff',width='10')

entry_cheeseburger.grid(row=3,column=1)



lbl_vegburger=Label(f1,text='Veggie Burger',font=('STLiti',15,'bold'),
               fg='white',bg='#669999',width='20')
lbl_vegburger.grid(row=4,column=0)

entry_vegburger=Entry(f1,textvariable=VegBurger,bd=5,
                     font=('STLiti',15,'bold'),
               fg='white',bg='#c61aff',width='10')

entry_vegburger.grid(row=4,column=1)


lbl_vegpizza=Label(f1,text='Veggie Pizza',font=('STLiti',15,'bold'),
               fg='white',bg='#669999',width='20')
lbl_vegpizza.grid(row=5,column=0)

entry_vegpizza=Entry(f1,textvariable=VegPizza,bd=5,
                     font=('STLiti',15,'bold'),
               fg='white',bg='#c61aff',width='10')

entry_vegpizza.grid(row=5,column=1)



lbl_bbqburger=Label(f1,text='BBQ Burger',font=('STLiti',15,'bold'),
               fg='white',bg='#669999',width='20')
lbl_bbqburger.grid(row=6,column=0)

entry_bbqburger=Entry(f1,textvariable=BBQBurger,bd=5,
                     font=('STLiti',15,'bold'),
               fg='white',bg='#c61aff',width='10')

entry_bbqburger.grid(row=6,column=1)




lbl_bbqpizza=Label(f1,text='BBQ Pizza',font=('STLiti',15,'bold'),
               fg='white',bg='#669999',width='20')
lbl_bbqpizza.grid(row=7,column=0)

entry_bbqpizza=Entry(f1,textvariable=BBQPizza,bd=5,
                     font=('STLiti',15,'bold'),
               fg='white',bg='#c61aff',width='10')

entry_bbqpizza.grid(row=7,column=1)




lbl_cocacola=Label(f1,text='Coca Cola',font=('STLiti',15,'bold'),
               fg='white',bg='#669999',width='20')
lbl_cocacola.grid(row=8,column=0)

entry_cocacola=Entry(f1,textvariable=CocaCola,bd=5,
                     font=('STLiti',15,'bold'),
               fg='white',bg='#c61aff',width='10')

entry_cocacola.grid(row=8,column=1)



lbl_pepsi=Label(f1,text='Pepsi',font=('STLiti',15,'bold'),
               fg='white',bg='#669999',width='20')
lbl_pepsi.grid(row=9,column=0)

entry_pepsi=Entry(f1,textvariable=Pepsi,bd=5,
                     font=('STLiti',15,'bold'),
               fg='white',bg='#c61aff',width='10')

entry_pepsi.grid(row=9,column=1)

# create reset and total button
resetbutton=Button(f1,text='Reset',font=('Jokerman',15,'bold'),
                   fg='black',bg='#00ffff',width='10',command=Reset)

resetbutton.grid(row=10,column=0)


totalbutton=Button(f1,text='Total',font=('Jokerman',15,'bold'),
                   fg='black',bg='red',width='10',command=Total)
totalbutton.grid(row=10,column=1)


# create third frame

f2=Frame(root,bd=2,width='300',height='360',bg='#ff4dff')
f2.place(x=780,y=118)


Label(f2,text='BBQ BURGER BOX',font=('Felix Titling',20,'bold'),
      fg='black').place(x=20,y=10)



Label(f2,text='Invoice',font=('Geogiya',20,'bold'),
      fg='black',bg='#ff4dff').place(x=90,y=50)

 
Label(f2,text='"Thank you for Visit"',
      font=('Mageto',15,'bold'),
      fg='white',bg='#ff4dff').place(x=50,y=250)


Label(f2,text='"Savor the Moment:[BBQ BURGER BOX]',
      font=('Geogiya',10,'bold'),
      fg='black',bg='#ff4dff').place(x=15,y=300)

Label(f2,text='-Where Taste Meets Tradition"',
      font=('Geogiya',10,'bold'),
      fg='black',bg='#ff4dff').place(x=50,y=320)

pay_button=Button(f2,text='pay',
      font=('Felix Titling',15,'bold'),
      fg='black',bg='#00e673',width='8',command=showmore).place(x=85,y=200)

root.mainloop()
