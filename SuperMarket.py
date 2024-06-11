from lzma import FORMAT_RAW
from msilib.schema import Error
from optparse import TitledHelpFormatter
from ssl import Options
from tkinter import * 
from tkinter import messagebox
from turtle import title
import webbrowser
import os
import sys
pro = Tk()
pro.geometry('800x450+350+200')
pro.resizable(False,False)
pro.title('SUPERMARKET')
pro.iconbitmap('C:\\Users\\rouaa\\OneDrive\\Desktop\\Uni\\Uni.3\\icone2.ico')
title = Label(pro, text='SuperMarket System',fg='white',bg='teal',font=('tajwal',20,'bold'))
title.pack(fill=X)


u1='https://www.facebook.com/ruaa.alaabed.7'
u2='https://www.instagram.com/ruaa_alaabed/'
u3='https://twitter.com/ruaa_alaabed'
u4='https://www.youtube.com/channel/UCtRtnqzaQWGMMmhKE6KyHBw'
def Open1():
    webbrowser.open_new(u1)
def Open2():
    webbrowser.open_new(u2)
def Open3():
    webbrowser.open_new(u3)
def Open4():
    webbrowser.open_new(u4)
def about1():
    messagebox.showinfo('About the project','SuperMarket management system to make it easier to the owner to deal with it')
def log():
    user = En1.get()
    passw =En2.get()
    if user== 'Roua' and passw == '987654321':
        
         messagebox.showinfo('Welcome','Welcome')
    else:
            messagebox.showerror('Wrong longin', 'Error')    

F1=Frame(pro,width=230, height=420, bg='gray')
F1.place(x=570,y=37)
Titlel=Label(F1, text='Ercel & Alabed', bg='teal', fg='white', font=('Lobster' , 15 , 'bold'))
Titlel.place(x=30 , y=5 )
Title2 = Label(F1, text='Super market', bg='grey', fg='white', font=('tajawal' , 11 , 'bold') )
Title2.place(x=70 , y=35)
Title3= Label(F1, text='Social Media Accounts :', bg='gray', fg='white', font=('tajawal' , 12 , 'bold'))
Title3.place(x=30 , y=70 )
B1=Button(F1, text='Facebook', width=24, fg='black',bg='salmon', font=('tajawal' , 11 ),command=Open1)
B1.place(x=2,y=120 )
B2=Button(F1, text='Instagram', width=24, fg='black',bg='salmon', font=('tajawal' , 11 ),command=Open2)
B2.place(x=2,y=160 )
B3=Button(F1, text='Twitter', width=24, fg='black',bg='salmon', font=('tajawal' , 11 ),command=Open3)
B3.place(x=2,y=200 )
B4=Button(F1, text='You Tube', width=24, fg='black',bg='salmon', font=('tajawal' , 11 ),command=Open4)
B4.place(x=2,y=240 )
B5=Button(F1, text='About the project', width=24, fg='black',bg='salmon', font=('tajawal' , 11 ),command=about1)
B5.place(x=2,y=280 )
B6=Button(F1, text='Close the program', width=24, fg='black',bg='salmon', font=('tajawal' , 9 , 'bold'),command=quit)
B6.place(x=25,y=350 )
photo = PhotoImage(file="C:\\Users\\rouaa\\OneDrive\\Desktop\\Uni\\Uni.3\\icone3.png")
imo = Label(pro, image=photo)
imo.place(x=50, y=40, width=400, height=300)

F2 = Frame(pro, width=570, height=120, bg='gray')
F2.place(x=0, y=330)
photo1 = PhotoImage(file='C:\\Users\\rouaa\\OneDrive\\Desktop\\Uni\\Uni.3\\log22.png')
imo1 = Label(pro, image=photo1)
imo1.place(x= 1, y=335, width=110 , height=100 )
L1=Label(F2, text='User name', fg='black', bg='gray',font=( 10))
L1.place(x=110, y=15)
L2=Label(F2, text='Password', fg='black', bg='gray',font=( 10))
L2.place(x=110, y=60)
En1= Entry(F2, font=( 12))
En1.place(x=210 ,y=16 )
En2= Entry(F2, font=( 12))
En2.place(x=210 ,y=60 )
B= Button(F2 , text='Log in', bg='salmon',font=('tajawal',11, 'bold'),width=12 , height=3 ,command=log)
B.place(x= 445 ,y=18 )


pro.mainloop()


