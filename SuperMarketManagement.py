from cgitb import text
from logging import root
from tkinter import *
import math , random , os
from tkinter import messagebox
from tkinter import font
from tkinter.font import BOLD
from turtle import right, title
from setuptools import Command
from SuperMarket import F1

class Super:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1500x750+5+15')
        self.root.title('Super-Market: super market')
        self.root.resizable(False,False)
        self.root.iconbitmap('C:\\Users\\rouaa\\OneDrive\\Desktop\\Uni\\Uni.3\\icone2.ico')
        title = Label(self.root,text='Super market management', fg='lavender', bg='teal', font=('tajawal',20,'bold' ))
        title.pack(fill=X)

        self.q1=IntVar()
        self.q2=IntVar()
        self.q3=IntVar()
        self.q4=IntVar()
        self.q5=IntVar()
        self.q6=IntVar()
        self.q7=IntVar()
        self.q8=IntVar()
        self.q9=IntVar()
        self.q10=IntVar()
        self.q11=IntVar()
        self.q12=IntVar()
        self.q13=IntVar()
        self.q14=IntVar()
        self.q15=IntVar()
        self.q16=IntVar()
        self.q17=IntVar()
        self.q18=IntVar()

        self.qq1=IntVar()
        self.qq2=IntVar()
        self.qq3=IntVar()
        self.qq4=IntVar()
        self.qq5=IntVar()
        self.qq6=IntVar()
        self.qq7=IntVar()
        self.qq8=IntVar()
        self.qq9=IntVar()
        self.qq10=IntVar()
        self.qq11=IntVar()
        self.qq12=IntVar()
        self.qq13=IntVar()
        self.qq14=IntVar()
        self.qq15=IntVar()
        self.qq16=IntVar()
        self.qq17=IntVar()
        self.qq18=IntVar()

        self.qqq1=IntVar()
        self.qqq2=IntVar()
        self.qqq3=IntVar()
        self.qqq4=IntVar()
        self.qqq5=IntVar()
        self.qqq6=IntVar()
        self.qqq7=IntVar()
        self.qqq8=IntVar()
        self.qqq9=IntVar()
        self.qqq10=IntVar()
        self.qqq11=IntVar()
        self.qqq12=IntVar()
        self.qqq13=IntVar()
        self.qqq14=IntVar()
        self.qqq15=IntVar()
        #Buyer data variables
        self.namo = StringVar()
        self.phono = StringVar()
        self.fatora = StringVar()
        self.search_bill = StringVar()
        x= random.randint(1000,9999)
        self.fatora.set(str(x))
        #Total account variables
        self.bacoliat=StringVar()
        self.adoat = StringVar()
        self.kahraba =StringVar()
        #Customer data
        F1= Frame(root, bd=2, width=400, height=200, bg='teal')
        F1.place(x=1100, y=38)
        tit = Label(F1, text='Customers data ', font=('abel', 16, 'bold'), bg= 'teal', fg='salmon')
        tit.place(x=100, y=0)
        his_name= Label(F1, text='Customer name :',font=('abel', 13, ),bg='teal', fg='white')
        his_name.place(x=10,y=35)
        his_phone= Label(F1, text='Customer phone number :',font=('abel', 13, ),bg='teal', fg='white')
        his_phone.place(x=10,y=70)
        his_number= Label(F1, text='Customer number :',font=('abel', 13, ),bg='teal', fg='white')
        his_number.place(x=10,y=105)

        Ent_name = Entry(F1,textvariable=self.namo, justify='center')
        Ent_name.place(x=190,y=38)
        Ent_phone = Entry(F1,textvariable=self.phono, justify='center')
        Ent_phone.place(x=190 ,y=72 )
        Ent_bill = Entry(F1,textvariable=self.fatora,justify='center')
        Ent_bill.place(x=190 ,y=107 )
        
        btn_customer = Button(F1 , text='Search', font=('abel', 13), width=8, height=1, bg='white', command=self.find_bill)
        btn_customer.place(x=300, y=140)
        #Bill
        bills = Label(F1, text='Bills ', font=('abel', 14, 'bold'), bg='teal', fg='#FFC000')
        bills.place(x= 50, y= 145 )
        F2 = Frame(root, bd=2 , width=400, height=399, bg='white')
        F2.place(x=1100, y=240)
        scrol_y= Scrollbar(F2,orient=VERTICAL)
        self.textarea=Text(F2, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=LEFT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        #Prices
        F3 = Frame(root, bd=2, width=764, height=112, bg='teal')
        F3.place(x=733, y=633)
        TheTotalCost = Button(F3,text='The cost', width=15, height=1, font='abel', bg='#FFC000' ,fg='black', command=self.total )
        TheTotalCost.place(x=615,y=10)
        fish = Button(F3, text='Receipt document', width=15 , height=1, font='abel', bg='#FFC000',fg='black', command=self.bill_area)
        fish.place(x=615, y=60)
        clear= Button(F3, text='Clear', width=15, height=1,font='abel', bg='#FFC000',fg='black', command=self.clear_data)
        clear.place(x=460,y=10)
        exit = Button(F3, text='close the program', width=15, height=1,font='abel', bg='#FFC000',fg='black',command=quit)
        exit.place(x=460,y=60)
        legumes = Label(F3, text='Total count of legumes',font=('abel',14,'bold'), bg='teal',fg='#FFC000')
        legumes.place(x=5,y=10)
        home = Label(F3,text='Total count of household supplies',font=('abel',14,'bold'), bg='teal',fg='#FFC000')
        home.place(x=5,y=40)
        ElectricTools = Label(F3,text='Total count of electric tools',font=('abel',14,'bold'), bg='teal',fg='#FFC000')
        ElectricTools.place(x=5,y=70)
        ento1= Entry(F3,textvariable=self.bacoliat,  width=18)
        ento1.place(x=320,y=12)
        ento2= Entry(F3,textvariable=self.adoat, width=18)
        ento2.place(x=320,y=42)
        ento3= Entry(F3,textvariable=self.kahraba, width=18)
        ento3.place(x=320, y=72)

        #items1
        frame1=Frame(root, bd=2, width=365, height=710, bg='teal')
        frame1.place(x=1,y=35)
        t = Label(frame1, text='legumes list', font=('abel', 18 , 'bold'), bg='teal', fg='#FFC000')
        t.place(x=122,y=0)
        bq1 = Label(frame1, text='Rice', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq1.place(x=20,y=50)
        bq2 = Label(frame1, text='Bulgur', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq2.place(x=20,y=85)
        bq3 = Label(frame1, text='Beans', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq3.place(x=20,y=120)
        bq4 = Label(frame1, text='Lentil', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq4.place(x=20,y=155)
        bq5 = Label(frame1, text='Macaroni', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq5.place(x=20,y=190)
        bq6 = Label(frame1, text='Freekeh', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq6.place(x=20,y=225)
        bq7 = Label(frame1, text='Chickpeas', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq7.place(x=20,y=260)
        bq8 = Label(frame1, text='Bean', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq8.place(x=20,y=295)
        bq9 = Label(frame1, text='Salt', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq9.place(x=20,y=330)
        bq10 = Label(frame1, text='Sugar', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq10.place(x=20,y=365)
        bq11 = Label(frame1, text='Black pepper', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq11.place(x=20,y=400)
        bq12 = Label(frame1, text='Red pepper', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq12.place(x=20,y=435)
        bq13 = Label(frame1, text='Cowpea', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq13.place(x=20,y=470)
        bq14 = Label(frame1, text='Soybean', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq14.place(x=20,y=505)
        bq15 = Label(frame1, text='Wheat', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq15.place(x=20,y=540)
        bq16 = Label(frame1, text='Barley', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq16.place(x=20,y=575)
        bq17 = Label(frame1, text='Oats', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq17.place(x=20,y=610)
        bq18 = Label(frame1, text='Maize', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq18.place(x=20,y=645)

        bqent1 = Entry(frame1,textvariable=self.q1, width=20 )
        bqent1.place(x=160, y=55)
        bqent2 = Entry(frame1,textvariable=self.q2,width=20 )
        bqent2.place(x=160, y=85)
        bqent3 = Entry(frame1,textvariable=self.q3,width=20 )
        bqent3.place(x=160, y=120)
        bqent4 = Entry(frame1,textvariable=self.q4,width=20 )
        bqent4.place(x=160, y=155)
        bqent5 = Entry(frame1,textvariable=self.q5,width=20 )
        bqent5.place(x=160, y=190)
        bqent6 = Entry(frame1,textvariable=self.q6,width=20 )
        bqent6.place(x=160, y=225)
        bqent7 = Entry(frame1,textvariable=self.q7,width=20 )
        bqent7.place(x=160, y=260)
        bqent8 = Entry(frame1,textvariable=self.q8,width=20 )
        bqent8.place(x=160, y=295)
        bqent9 = Entry(frame1,textvariable=self.q9,width=20 )
        bqent9.place(x=160, y=330)
        bqent10 = Entry(frame1,textvariable=self.q10,width=20 )
        bqent10.place(x=160, y=365)
        bqent11 = Entry(frame1,textvariable=self.q11,width=20 )
        bqent11.place(x=160, y=400)
        bqent12 = Entry(frame1,textvariable=self.q12,width=20 )
        bqent12.place(x=160, y=435)
        bqent13 = Entry(frame1,textvariable=self.q13,width=20 )
        bqent13.place(x=160, y=470)
        bqent14 = Entry(frame1,textvariable=self.q14,width=20 )
        bqent14.place(x=160, y=505)
        bqent15 = Entry(frame1,textvariable=self.q15,width=20 )
        bqent15.place(x=160, y=540)
        bqent16 = Entry(frame1,textvariable=self.q16,width=20 )
        bqent16.place(x=160, y=575)
        bqent17 = Entry(frame1,textvariable=self.q17,width=20 )
        bqent17.place(x=160, y=610)
        bqent18 = Entry(frame1,textvariable=self.q18,width=20 )
        bqent18.place(x=160, y=645)

        #items2

        frame2=Frame(root, bd=2, width=365, height=710, bg='teal')
        frame2.place(x=367,y=35)
        tt = Label(frame2, text='Household Supplies', font=('abel', 18 , 'bold'), bg='teal', fg='#FFC000')
        tt.place(x=122,y=0)
        bq1 = Label(frame2, text='Colander', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq1.place(x=20,y=50)
        bq2 = Label(frame2, text='Dish', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq2.place(x=20,y=85)
        bq3 = Label(frame2, text='Cup', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq3.place(x=20,y=120)
        bq4 = Label(frame2, text='Kettle', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq4.place(x=20,y=155)
        bq5 = Label(frame2, text='Knife', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq5.place(x=20,y=190)
        bq6 = Label(frame2, text='Fork', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq6.place(x=20,y=225)
        bq7 = Label(frame2, text='Pot', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq7.place(x=20,y=260)
        bq8 = Label(frame2, text='Basket', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq8.place(x=20,y=295)
        bq9 = Label(frame2, text='Spoon', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq9.place(x=20,y=330)
        bq10 = Label(frame2, text='Tray', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq10.place(x=20,y=365)
        bq11 = Label(frame2, text='Mixing bowl ', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq11.place(x=20,y=400)
        bq12 = Label(frame2, text='Can opener', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq12.place(x=20,y=435)
        bq13 = Label(frame2, text='Peeler', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq13.place(x=20,y=470)
        bq14 = Label(frame2, text='Cutting Board', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq14.place(x=20,y=505)
        bq15 = Label(frame2, text='Excavator', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq15.place(x=20,y=540)
        bq16 = Label(frame2, text='Trash Basket', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq16.place(x=20,y=575)
        bq17 = Label(frame2, text='Ashtray', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq17.place(x=20,y=610)
        bq18 = Label(frame2, text='Bags', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq18.place(x=20,y=645)

        bqent1 = Entry(frame2,textvariable=self.qq1,width=20 )
        bqent1.place(x=160, y=55)
        bqent2 = Entry(frame2,textvariable=self.qq2,width=20 )
        bqent2.place(x=160, y=85)
        bqent3 = Entry(frame2,textvariable=self.qq3,width=20 )
        bqent3.place(x=160, y=120)
        bqent4 = Entry(frame2,textvariable=self.qq4,width=20 )
        bqent4.place(x=160, y=155)
        bqent5 = Entry(frame2,textvariable=self.qq5,width=20 )
        bqent5.place(x=160, y=190)
        bqent6 = Entry(frame2,textvariable=self.qq6,width=20 )
        bqent6.place(x=160, y=225)
        bqent7 = Entry(frame2,textvariable=self.qq7,width=20 )
        bqent7.place(x=160, y=260)
        bqent8 = Entry(frame2,textvariable=self.qq8,width=20 )
        bqent8.place(x=160, y=295)
        bqent9 = Entry(frame2,textvariable=self.qq9,width=20 )
        bqent9.place(x=160, y=330)
        bqent10 = Entry(frame2,textvariable=self.qq10,width=20 )
        bqent10.place(x=160, y=365)
        bqent11 = Entry(frame2,textvariable=self.qq11,width=20 )
        bqent11.place(x=160, y=400)
        bqent12 = Entry(frame2,textvariable=self.qq12,width=20 )
        bqent12.place(x=160, y=435)
        bqent13 = Entry(frame2,textvariable=self.qq13,width=20 )
        bqent13.place(x=160, y=470)
        bqent14 = Entry(frame2,textvariable=self.qq14,width=20 )
        bqent14.place(x=160, y=505)
        bqent15 = Entry(frame2,textvariable=self.qq15,width=20 )
        bqent15.place(x=160, y=540)
        bqent16 = Entry(frame2,textvariable=self.qq16,width=20 )
        bqent16.place(x=160, y=575)
        bqent17 = Entry(frame2,textvariable=self.qq17,width=20 )
        bqent17.place(x=160, y=610)
        bqent18 = Entry(frame2,textvariable=self.qq18,width=20 )
        bqent18.place(x=160, y=645)

        #items3

        
        frame3=Frame(root, bd=2, width=365, height=597, bg='teal')
        frame3.place(x=733,y=35)
        ttt = Label(frame3, text='Electric Tools', font=('abel', 18 , 'bold'), bg='teal', fg='#FFC000')
        ttt.place(x=122,y=0)
        bq1 = Label(frame3, text='Vacuum Cleaner', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq1.place(x=20,y=50)
        bq2 = Label(frame3, text='TV', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq2.place(x=20,y=85)
        bq3 = Label(frame3, text='Washing Machine', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq3.place(x=20,y=120)
        bq4 = Label(frame3, text='Microwave', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq4.place(x=20,y=155)
        bq5 = Label(frame3, text='Blender', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq5.place(x=20,y=190)
        bq6 = Label(frame3, text='Gas Stove', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq6.place(x=20,y=225)
        bq7 = Label(frame3, text='Electric fryer', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq7.place(x=20,y=260)
        bq8 = Label(frame3, text='Ceiling fan', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq8.place(x=20,y=295)
        bq9 = Label(frame3, text='Floor fan', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq9.place(x=20,y=330)
        bq10 = Label(frame3, text='Water filter', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq10.place(x=20,y=365)
        bq11 = Label(frame3, text='Iron ', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq11.place(x=20,y=400)
        bq12 = Label(frame3, text='Refrigerator', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq12.place(x=20,y=435)
        bq13 = Label(frame3, text='Hair dryer', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq13.place(x=20,y=470)
        bq14 = Label(frame3, text='Electric oven', font=('abel', 15, 'bold' ), bg='teal', fg='white')
        bq14.place(x=20,y=505)
        bq15 = Label(frame3, text='Electric juicer', font=('abel', 15 , 'bold'), bg='teal', fg='white')
        bq15.place(x=20,y=540)
        
        bqent1 = Entry(frame3,textvariable=self.qqq1,width=20 )
        bqent1.place(x=180, y=55)
        bqent2 = Entry(frame3,textvariable=self.qqq2,width=20 )
        bqent2.place(x=180, y=85)
        bqent3 = Entry(frame3,textvariable=self.qqq3,width=20 )
        bqent3.place(x=180, y=120)
        bqent4 = Entry(frame3,textvariable=self.qqq4,width=20 )
        bqent4.place(x=180, y=155)
        bqent5 = Entry(frame3,textvariable=self.qqq5,width=20 )
        bqent5.place(x=180, y=190)
        bqent6 = Entry(frame3,textvariable=self.qqq6,width=20 )
        bqent6.place(x=180, y=225)
        bqent7 = Entry(frame3,textvariable=self.qqq7,width=20 )
        bqent7.place(x=180, y=260)
        bqent8 = Entry(frame3,textvariable=self.qqq8,width=20 )
        bqent8.place(x=180, y=295)
        bqent9 = Entry(frame3,textvariable=self.qqq9,width=20 )
        bqent9.place(x=180, y=330)
        bqent10 = Entry(frame3,textvariable=self.qqq10,width=20 )
        bqent10.place(x=180, y=365)
        bqent11 = Entry(frame3,textvariable=self.qqq11,width=20 )
        bqent11.place(x=180, y=400)
        bqent12 = Entry(frame3,textvariable=self.qqq12,width=20 )
        bqent12.place(x=180, y=435)
        bqent13 = Entry(frame3,textvariable=self.qqq13,width=20 )
        bqent13.place(x=180, y=470)
        bqent14 = Entry(frame3,textvariable=self.qqq14,width=20 )
        bqent14.place(x=180, y=505)
        bqent15 = Entry(frame3,textvariable=self.qqq15,width=20 )
        bqent15.place(x=180, y=540)
    def total(self):
        self.Rice = self.q1.get()*2
        self.Bulgur = self.q2.get()*1.5
        self.Beans = self.q3.get()*2
        self.Lentli = self.q4.get()*2.5
        self.Macaroni = self.q5.get()*1.5
        self.Freekeh = self.q6.get()*2
        self.Chickpeas = self.q7.get()*2.5
        self.Bean = self.q8.get()*2
        self.Salt = self.q9.get()*1
        self.Sugar = self.q10.get()*1
        self.Blackpepper = self.q11.get()*1.25
        self.Redpepper = self.q12.get()*1.25
        self.Cowpea = self.q13.get()*4
        self.Soybean = self.q14.get()*3.5
        self.Wheat = self.q15.get()*3.75
        self.Barley = self.q16.get()*3
        self.Oats = self.q17.get()*2
        self.Maize = self.q18.get()*3
        self.totalito= float(
                        self.Rice+
                        self.Bulgur+
                        self.Beans+
                        self.Lentli+
                        self.Macaroni+
                        self.Freekeh+
                        self.Chickpeas+
                        self.Bean+
                        self.Salt+
                        self.Sugar+
                        self.Blackpepper+
                        self.Redpepper+
                        self.Cowpea+
                        self.Soybean+
                        self.Wheat+
                        self.Barley+
                        self.Oats+
                        self.Maize
                        )
        self.bacoliat.set(str(self.totalito)+ " $ ")
        self.Colander= self.qq1.get()*6
        self.Dish = self.qq2.get()*0.5
        self.Cup = self.qq3.get()*0.75
        self.Kettle = self.qq4.get()*30
        self.Knife = self.qq5.get()*0.35
        self.Fork = self.qq6.get()*0.35
        self.Pot = self.qq7.get()*1
        self.Basket = self.qq8.get()*5
        self.Spoon = self.qq9.get()*0.35
        self.Tray = self.qq10.get()*0.40
        self.MixingBowl = self.qq11.get()*1
        self.CanOpener = self.qq12.get()*0.75
        self.Peeler = self.qq13.get()*0.4
        self.CuttingBoard = self.qq14.get()*1.75
        self.Excavator = self.qq15.get()*0.4
        self.TrashBasket = self.qq16.get()*5
        self.Ashtray = self.qq17.get()*0.80
        self.Bags = self.qq18.get()*1.5
        self.totalito2=float(
                        self.Colander+
                        self.Dish+
                        self.Cup+
                        self.Kettle+
                        self.Knife+
                        self.Fork+
                        self.Pot+
                        self.Basket+
                        self.Spoon+
                        self.Tray+
                        self.MixingBowl+
                        self.CanOpener+
                        self.Peeler+
                        self.CuttingBoard+
                        self.Excavator+
                        self.TrashBasket+
                        self.Ashtray+
                        self.Bags
                        )
        self.adoat.set(str(self.totalito2)+ " $ ")               
        self.VacuumCleaner= self.qqq1.get()*200
        self.TV = self.qqq2.get()*350
        self.WashingMachine = self.qqq3.get()*175
        self.Microwave = self.qqq4.get()*100
        self.Belender = self.qqq5.get()*80
        self.GasStove = self.qqq6.get()*75
        self.ElectricFryer = self.qqq7.get()*175
        self.CeilingFan = self.qqq8.get()*60
        self.Floorfan = self.qqq9.get()*65
        self.Waterfilter = self.qqq10.get()*40
        self.Iron = self.qqq11.get()*250
        self.Refrigerator = self.qqq12.get()*370
        self.Hairdryer = self.qqq13.get()*125
        self.ElectricOven = self.qqq14.get()*120
        self.ElectricJuicer = self.qqq15.get()*115
        self.totalito3=float(
                       self.VacuumCleaner+
                       self.TV+
                       self.WashingMachine+
                       self.Microwave+
                       self.Belender+
                       self.GasStove+
                       self.ElectricFryer+
                       self.CeilingFan+
                       self.Floorfan+
                       self.Waterfilter+
                       self.Iron+
                       self.Refrigerator+
                       self.Hairdryer+
                       self.ElectricOven+
                       self.ElectricJuicer
                       )
        self.kahraba.set(str(self.totalito3)+ " $ ") 
        self.all= float(self.totalito+
                        self.totalito2+
                        self.totalito3
                        )
                    

        self.welcome()
    def welcome(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "      Welcome to Ercel & Alabed supermarket        ")
        self.textarea.insert(END,"\n ==============================================")
        self.textarea.insert(END,f"\n\t   B.NUM  :{self.fatora.get()}")
        self.textarea.insert(END,f"\n\t   NAME   : {self.namo.get()}")
        self.textarea.insert(END,f"\n\t   PHONE  :{self.phono.get()}")
        self.textarea.insert(END,"\n ==============================================")
        self.textarea.insert(END,f"\n Product\t      The number\t       The price\t")
        self.textarea.insert(END,"\n ==============================================")

    def bill_area(self):
        self.welcome()
        if self.q1.get() !=0:
            self.textarea.insert(END, f"\n Rice\t\t{self.q1.get()}\t\t{self.Rice}")
        if self.q2.get() !=0:
            self.textarea.insert(END, f"\n Bulgur\t\t{self.q2.get()}\t\t{self.Bulgur}")
        if self.q3.get() !=0:
            self.textarea.insert(END, f"\n Beans\t\t{self.q3.get()}\t\t{self.Beans}")
        if self.q4.get() !=0:
            self.textarea.insert(END, f"\n Lentli\t\t{self.q4.get()}\t\t{self.Lentli}")            
        if self.q5.get() !=0:
            self.textarea.insert(END, f"\n Macaroni \t\t{self.q5.get()}\t\t{self.Macaroni}")     
        if self.q6.get() !=0:
            self.textarea.insert(END, f"\n Freekeh \t\t{self.q6.get()}\t\t{self.Freekeh }")
        if self.q7.get() !=0:
            self.textarea.insert(END, f"\n Chickpeas \t\t{self.q7.get()}\t\t{self.Chickpeas }")
        if self.q8.get() !=0:
            self.textarea.insert(END, f"\n Bean \t\t{self.q8.get()}\t\t{self.Bean }")
        if self.q9.get() !=0:
            self.textarea.insert(END, f"\n Salt \t\t{self.q9.get()}\t\t{self.Salt }")
        if self.q10.get() !=0:
            self.textarea.insert(END, f"\n Sugar \t\t{self.q10.get()}\t\t{self.Sugar }")
        if self.q11.get() !=0:
            self.textarea.insert(END, f"\n Blackpepper \t\t{self.q11.get()}\t\t{self.Blackpepper }")
        if self.q12.get() !=0:
            self.textarea.insert(END, f"\n Redpepper \t\t{self.q12.get()}\t\t{self.Redpepper }")
        if self.q13.get() !=0:
            self.textarea.insert(END, f"\n Cowpea \t\t{self.q13.get()}\t\t{self.Cowpea }")
        if self.q14.get() !=0:
            self.textarea.insert(END, f"\n Soybean \t\t{self.q14.get()}\t\t{self.Soybean }")
        if self.q15.get() !=0:
            self.textarea.insert(END, f"\n Wheat \t\t{self.q15.get()}\t\t{self.Wheat }")
        if self.q16.get() !=0:
            self.textarea.insert(END, f"\n Barley \t\t{self.q16.get()}\t\t{self.Barley }")
        if self.q17.get() !=0:
            self.textarea.insert(END, f"\n Oats \t\t{self.q17.get()}\t\t{self.Oats }")
        if self.q18.get() !=0:
            self.textarea.insert(END, f"\n Maize \t\t{self.q18.get()}\t\t{self.Maize }")
        if self.qq1.get() !=0:
            self.textarea.insert(END, f"\n Colander\t\t{self.qq1.get()}\t\t{self.Colander}")
        if self.qq2.get() !=0:
            self.textarea.insert(END, f"\n Dish\t\t{self.qq2.get()}\t\t{self.Dish}")
        if self.qq3.get() !=0:
            self.textarea.insert(END, f"\n Cup\t\t{self.qq3.get()}\t\t{self.Cup}")
        if self.qq4.get() !=0:
            self.textarea.insert(END, f"\n Kettle\t\t{self.qq4.get()}\t\t{self.Kettle}")            
        if self.qq5.get() !=0:
            self.textarea.insert(END, f"\n Knife \t\t{self.qq5.get()}\t\t{self.Knife}")     
        if self.qq6.get() !=0:
            self.textarea.insert(END, f"\n Fork \t\t{self.qq6.get()}\t\t{self.Fork }")
        if self.qq7.get() !=0:
            self.textarea.insert(END, f"\n Pot \t\t{self.qq7.get()}\t\t{self.Pot }")
        if self.qq8.get() !=0:
            self.textarea.insert(END, f"\n Basket \t\t{self.qq8.get()}\t\t{self.Basket }")
        if self.qq9.get() !=0:
            self.textarea.insert(END, f"\n Spoon \t\t{self.qq9.get()}\t\t{self.Spoon }")
        if self.qq10.get() !=0:
            self.textarea.insert(END, f"\n Tray \t\t{self.qq10.get()}\t\t{self.Tray }")
        if self.qq11.get() !=0:
            self.textarea.insert(END, f"\n MixingBowl \t\t{self.qq11.get()}\t\t{self.MixingBowl }")
        if self.qq12.get() !=0:
            self.textarea.insert(END, f"\n CanOpener \t\t{self.qq12.get()}\t\t{self.CanOpener }")
        if self.qq13.get() !=0:
            self.textarea.insert(END, f"\n Peeler \t\t{self.qq13.get()}\t\t{self.Peeler }")
        if self.qq14.get() !=0:
            self.textarea.insert(END, f"\n CuttingBoard \t\t{self.qq14.get()}\t\t{self.CuttingBoard }")
        if self.qq15.get() !=0:
            self.textarea.insert(END, f"\n Excavator \t\t{self.qq15.get()}\t\t{self.Excavator }")
        if self.qq16.get() !=0:
            self.textarea.insert(END, f"\n TrashBasket \t\t{self.qq16.get()}\t\t{self.TrashBasket }")
        if self.qq17.get() !=0:
            self.textarea.insert(END, f"\n Ashtray \t\t{self.qq17.get()}\t\t{self.Ashtray }")
        if self.qq18.get() !=0:
            self.textarea.insert(END, f"\n Bags \t\t{self.qq18.get()}\t\t{self.Bags }") 
        if self.qqq1.get() !=0:
            self.textarea.insert(END, f"\n VacuumCleaner\t\t{self.qqq1.get()}\t\t{self.VacuumCleaner}")
        if self.qqq2.get() !=0:
            self.textarea.insert(END, f"\n TV \t\t{self.qqq2.get()}\t\t{self.TV}")
        if self.qqq3.get() !=0:
            self.textarea.insert(END, f"\n WashingMachine\t\t{self.qqq3.get()}\t\t{self.WashingMachine}")
        if self.qqq4.get() !=0:
            self.textarea.insert(END, f"\n Microwave\t\t{self.qqq4.get()}\t\t{self.Microwave}")            
        if self.qqq5.get() !=0:
            self.textarea.insert(END, f"\n Belender \t\t{self.qqq5.get()}\t\t{self.Belender}")     
        if self.qqq6.get() !=0:
            self.textarea.insert(END, f"\n GasStove \t\t{self.qqq6.get()}\t\t{self.GasStove }")
        if self.qqq7.get() !=0:
            self.textarea.insert(END, f"\n ElectricFryer \t\t{self.qqq7.get()}\t\t{self.ElectricFryer }")
        if self.qqq8.get() !=0:
            self.textarea.insert(END, f"\n CeilingFan \t\t{self.qqq8.get()}\t\t{self.CeilingFan }")
        if self.qqq9.get() !=0:
            self.textarea.insert(END, f"\n Floorfan \t\t{self.qqq9.get()}\t\t{self.Floorfan }")
        if self.qqq10.get() !=0:
            self.textarea.insert(END, f"\n Waterfilter \t\t{self.qqq10.get()}\t\t{self.Waterfilter }")
        if self.qqq11.get() !=0:
            self.textarea.insert(END, f"\n Iron \t\t{self.qqq11.get()}\t\t{self.Iron }")
        if self.qqq12.get() !=0:
            self.textarea.insert(END, f"\n Refrigerator \t\t{self.qqq12.get()}\t\t{self.Refrigerator }")
        if self.qqq13.get() !=0:
            self.textarea.insert(END, f"\n Hairdryer \t\t{self.qqq13.get()}\t\t{self.Hairdryer }")
        if self.qqq14.get() !=0:
            self.textarea.insert(END, f"\n ElectricOven \t\t{self.qqq14.get()}\t\t{self.ElectricOven }")
        if self.qqq15.get() !=0:
            self.textarea.insert(END, f"\n ElectricJuicer \t\t{self.qqq15.get()}\t\t{self.ElectricJuicer }") 
      
        self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save bill ", "Do you want to save the bill ?")
        if op>0 :
           self.bill_data= self.textarea.get('1.0',END)
           r1=open("bills/"+ str(self.fatora.get())+ ".txt", "w")
           r1.write(self.bill_data)
           r1.close
           messagebox.showinfo("Saved", f"Bill no : {self.fatora.get()}saved successfully")
        else :
            return
    def find_bill(self):
        present ="no"
        for filename in os.listdir("bills/"):
            if filename.endswith(".txt"):
                if filename == (self.fatora.get() + ".txt"):
                    f1=open(f"bills/{filename}", "r")
                    self.textarea.delete('1.0', END)
                    self.textarea.insert(END, f1.read())
                    f1.close()
                    present ="yes"
        if present == "no": 
            messagebox.showerror("Error", "Invalid Bill no.")

    def clear_data(self):
        self.q1.set(0)
        self.q2.set(0)
        self.q3.set(0)
        self.q4.set(0)
        self.q5.set(0)
        self.q6.set(0)
        self.q7.set(0)
        self.q8.set(0)
        self.q9.set(0)
        self.q10.set(0)
        self.q11.set(0)
        self.q12.set(0)
        self.q13.set(0)
        self.q14.set(0)
        self.q15.set(0)
        self.q16.set(0)
        self.q17.set(0)
        self.q18.set(0)

        self.qq1.set(0)
        self.qq2.set(0)
        self.qq3.set(0)
        self.qq4.set(0)
        self.qq5.set(0)
        self.qq6.set(0)
        self.qq7.set(0)
        self.qq8.set(0)
        self.qq9.set(0)
        self.qq10.set(0)
        self.qq11.set(0)
        self.qq12.set(0)
        self.qq13.set(0)
        self.qq14.set(0)
        self.qq15.set(0)
        self.qq16.set(0)
        self.qq17.set(0)
        self.qq18.set(0)

        self.qqq1.set(0)
        self.qqq2.set(0)
        self.qqq3.set(0)
        self.qqq4.set(0)
        self.qqq5.set(0)
        self.qqq6.set(0)
        self.qqq7.set(0)
        self.qqq8.set(0)
        self.qqq9.set(0)
        self.qqq10.set(0)
        self.qqq11.set(0)
        self.qqq12.set(0)
        self.qqq13.set(0)
        self.qqq14.set(0)
        self.qqq15.set(0)
        self.namo.set("")
        self.phono.set("")
        self.fatora.set("")      
        self.bacoliat.set("")
        self.adoat.set("")
        self.kahraba.set("")


root=Tk()
ob = Super(root)
root.mainloop()
        
