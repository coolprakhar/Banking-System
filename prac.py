import sqlite3
con=sqlite3.Connection('bank')
cur=con.cursor()
cur.execute("create table if not exists  ban(customerid  varchar(20) primary key not null,first_name  char(10),last_name char(10),address varchar(30),phone number(10),email_id varchar(20),dob_date date, balance number, pass varchar(20))")
from Tkinter import *
from tkMessageBox import *
global root

pro=Tk()
pro.title('INTRODUCTION')
def menu():
     pro.destroy()
     start()
def start():
     def main():
          window.destroy()
          start()
     def acc():
          root.destroy()
          global window
          window = Tk()
          window.title('CreateAccount')
          window.config(bg='PaleVioletRed1')
          Label(window,text='CUSTOMER INFO',font='times 20 bold',bg='dodger blue',bd=5).grid(columnspan=2)
          Label(window,text='Enter Customer id:',bg='PaleVioletRed1').grid(row=1,column=0)
          e=Entry(window,width=35,bd=5)
          e.grid(row=1,column=1)
          Label(window,text='Enter First Name:',bg='PaleVioletRed1').grid(row=2,column=0)
          f=Entry(window,width=35,bd=5)
          f.grid(row=2,column=1)
          Label(window,text='Enter Last Name:',bg='PaleVioletRed1').grid(row=3,column=0)
          g=Entry(window,width=35,bd=5)
          g.grid(row=3,column=1)
          Label(window,text='Enter Full Address:',bg='PaleVioletRed1').grid(row=4,column=0)
          h=Entry(window,width=35,bd=5)
          h.grid(row=4,column=1)
          Label(window,text='Phone:',bg='PaleVioletRed1').grid(row=5,column=0)
          i=Entry(window,width=35,bd=5)
          i.grid(row=5,column=1)
          Label(window,text='Enter Email id:',bg='PaleVioletRed1').grid(row=6,column=0)
          j=Entry(window,width=35,bd=5)
          j.grid(row=6,column=1)
          Label(window,text='Enter Date Of Birth:',bg='PaleVioletRed1').grid(row=7,column=0)
          k=Entry(window,width=35,bd=5)
          k.grid(row=7,column=1)
          Label(window,text='Enter Initial balance: ',bg='PaleVioletRed1').grid(row=8,column=0)
          l=Entry(window,width=35,bd=5)
          l.grid(row=8,column=1)
          Label(window, text='Create Password: ',bg='PaleVioletRed1').grid(row=9, column=0)
          pas = Entry(window,width=35, bd=5)
          pas.grid(row=9, column=1)
          

          def insert():
               cur.execute('insert into ban values(?,?,?,?,?,?,?,?,?)',(e.get(),f.get(),g.get(),h.get(),int(i.get()),j.get(),k.get(),int(l.get()),pas.get()))
               showinfo('Congrats!!','Insertion Done')
               con.commit()
          def show():
               e1=e.get()     
               cur.execute('select * from ban ')
               b=cur.fetchall()
               print b
               
          Button(window,text='SHOW',bg='ivory3',command=show,height=2,width=6,bd=7).grid(row=13,column=0)
          Button(window,text='INSERT',bg='ivory3',command=insert,height=2,width=6,bd=7).grid(row=13,column=1)
          Button(window,text="BACK",command=main,bg='ivory3',height=2,width=6,bd=7).grid(row=14,column=0)
          window.mainloop()
          
     def main1():
          window1.destroy()
          start()
          
     def depos():
          root.destroy()
          global window1
          window1 = Tk()
          window1.title('Deposit')
          
          window1.geometry('685x375')
          image2=PhotoImage(file="deposit.gif")
          label2=Label(window1,image=image2,height=200).grid(row=0,columnspan=2)
          
          Label(window1,text='DEPOSIT COUNTER',font='times 20 bold',bg='orchid1').grid(row=0,column = 0,columnspan=2)
          Label(window1,text='Enter Amount:').grid(row=3,column=0)
          o=Entry(window1,bd=5)
          o.grid(row=3,column=1)
          Label(window1,text='Enter Account Number:').grid(row=1,column=0)
          acc=Entry(window1,bd=5)
          acc.grid(row=1,column=1)
          Label(window1,text='Enter Password:').grid(row=2,column=0)
          pas=Entry(window1,bd=5)
          pas.grid(row=2,column=1)
          
          def fetch():
               print acc.get()
               print o.get()
               val=acc.get()
               cur.execute("select pass from ban where customerid=(?)",[val])
               password = cur.fetchall()[0][0]
               print password
               cur.execute("select customerid from ban where pass = ?",[pas.get()])
               m = cur.fetchall()
               cur.execute("select balance from ban where customerid=(?)",[val])
               cur_bal = cur.fetchall()
               print m
               if len(m)==0:
                    showerror('ERROR', 'Check your password')
               else:
                    new = int(cur_bal[0][0]) + int(o.get())      
                    cur.execute("Update ban set balance = (?) where customerid = (?)",(new,val))
                    print new
                    cur.execute("select * from ban where customerid = (?)",[val])
                    q = cur.fetchall()
                    print q
                    showinfo('CREDITED', 'MONEY IS SUCCESSFULLY CREDITED!!!')

                    ans=''
                    for val in q:
                         ans = ans +' '+ str(val)
                    Label(window1, text=ans).grid(row=4)
                    ans = 'New balance is : '+str(val[7])
                    Label(window1, text=ans).grid(row=5,column=0)
               con.commit()

          Button(window1,text="ENTER",command=fetch,bg='ivory3',bd=7).grid(row=6,column=1)
          Button(window1,text="BACK",command=main1,bg='ivory3',bd=7).grid(row=6,column=0)
          mainloop()
          
     def main2():
          window3.destroy()
          start()
          
     def checkbal():
          root.destroy()
          global window3
          window3 = Tk()
          window3.title('Check Balance')

          window3.geometry('303x390')
          image4=PhotoImage(file="checkbal.gif")
          label3=Label(window3,image=image4,height=260).grid(row=0,columnspan=2)
          
          Label(window3,text='CHECK BALANCE',font='times 20 bold',bg='DarkOliveGreen1').grid(row=0,column=0,columnspan=2)
          Label(window3,text='Enter Customer ID:',font='times 12 bold',bd=5).grid(row=1,column=0)
          kval = Entry(window3,bd=5)
          kval.grid(row=1,column=1)
          ans=IntVar()
          Label(window3,text='Enter Password:',font='times 12 bold',bd=5).grid(row=2,column=0)
          kval1 = Entry(window3,bd=5)
          kval1.grid(row=2,column=1)
          
          def ch():
               cur.execute("select pass from ban where customerid=(?)",[kval.get()])
               password = cur.fetchall()[0][0]
               print password
               cur.execute("select customerid from ban where pass = ?",[kval1.get()])
               m = cur.fetchall()
               print m
               if len(m)==0:
                    showerror('ERROR', 'Check your password')
               else:
                    cur.execute("select balance from ban where customerid = (?)",[kval.get()])
                    q = cur.fetchall()
                    print q
                    Label(window3,text='Your Balance is: '+str(q)).grid(row=5,column=0)

               ###################################################################
               
          Button(window3,text="CHECK",command=ch,bg='ivory3',bd=7).grid(row=3,column=1)
          Button(window3,text="BACK",command=main2,bg='ivory3',bd=7).grid(row=3,column=0)
          mainloop()

     def main3():
          window2.destroy()
          start()
     
     def withd():
         root.destroy()
         global window2
         window2 = Tk()
         window2.title('Withdrawl')
          
         window2.geometry('685x375')
         image3=PhotoImage(file="withdrawl.gif")
         label3=Label(window2,image=image3,height=200).grid(row=0,columnspan=2)
         
         Label(window2,text='WITHDRAWL COUNTER',font='times 20 bold',bg='blue violet').grid(row=0,columnspan=2)
         Label(window2,text='Enter Amount:').grid(row=3,column=0)
         l=Entry(window2,bd=5)
         l.grid(row=3,column=1)
         Label(window2,text='Enter Account Number:').grid(row=1,column=0)
         acc1=Entry(window2,bd=5)
         acc1.grid(row=1,column=1)
         Label(window2,text='Enter Password:').grid(row=2,column=0)
         pas2=Entry(window2,bd=5)
         pas2.grid(row=2,column=1)
         
         def fetch1():
               ########################################################
               val=acc1.get()
               cur.execute("select pass from ban where customerid=(?)",[val])
               password = cur.fetchall()[0][0]
               print password
               cur.execute("select customerid from ban where pass = ?",[pas2.get()])
               m = cur.fetchall()
               cur.execute("select balance from ban where customerid=(?)",[val])
               cur_bal = cur.fetchall()
               print m
               if len(m)==0:
                    showerror('ERROR', 'Check your password')
               else:
                    new = int(cur_bal[0][0]) - int(l.get())       ####################
                    if new<0:
                         showerror('ERROR', 'Debited amount greater than avaiable balance')
                    else:
                         cur.execute("Update ban set balance = (?) where customerid = (?)",(new,val))
                         print new
                         cur.execute("select * from ban where customerid = (?)",[val])
                         q = cur.fetchall()
                         print q
                         showinfo('CREDITED', 'MONEY IS SUCCESSFULLY DEBITED!!!')

                         ans=''
                         for val in q:
                              ans = ans +' '+ str(val)
                         Label(window2, text=ans).grid(row=4)
                         ans = 'New balance is : '+str(val[7])
                         Label(window2, text=ans).grid(row=5,column=0)
                    con.commit()

               ########################################################
         Button(window2,text="ENTER",command=fetch1,bg='ivory3',bd=7).grid(row=6,column=1)
         Button(window2,text="BACK",command=main3,bg='ivory3',bd=7).grid(row=6,column=0)
         mainloop()

     def main4():
          window4.destroy()
          start()
    
     def about():
         root.destroy()
         global window4
         window4 = Tk()
         window4.title('About')
         window4.config(bg='light sky blue')
         Label(window4,text='ABOUT US',font='times 20 bold',bg='RoyalBlue2').grid(row=0)
         Label(window4,text="Banking System have been with us for as long as people have been using money. Banks and other financial institutions provide security for individuals,businesses and governments.For average person banks accept deposits,provide safe place for money.",font='times 9 bold',bg='light sky blue').grid(row=2,column=0)
         Label(window4,text="Banks are quite important to the economy and are involved in such economic activities as issuing money, settling payments.Banking’s original role was in serving primarily the wealthy and the financially sophisticated.Throughout history there has ",font='times 9 bold',bg='light sky blue').grid(row=3,column=0)
         Label(window4,text="been a long trend toward the democratization of finance, the opening of financial opportunities to an ever wider circle of people and reduce the risks to which they are subject.The leadership challenge requires more than smoothing of rough edges.",font='times 9 bold',bg='light sky blue').grid(row=5,column=0)
         Label(window4,text="Banks today are bigger and more opaque than ever, and they continue to trade in derivatives in many of the same ways they did before the crash, but on a larger scale and with precisely the same unknown risks.” It has massive opportunity costs.",font='times 9 bold',bg='light sky blue').grid(row=6,column=0)
         Button(window4,text="BACK",command=main4,bg='ivory3',bd=7).grid(row=8)
         window4.mainloop()
         
     root=Tk()
     root.geometry('730x401')
     root.title('BANKING SYSTEM')
     image1=PhotoImage(file="front.gif")
     label1=Label(root,image=image1)
     label1.grid(row=0,column=0, rowspan=100, columnspan=5)
     Label(root,text="BANKING SYSTEM",relief='groove',font='times 30 bold',bg='firebrick2',bd=10,height=2,width=20).grid(row=0,column=1)
     Button(root,text='CREATE ACCOUNT',padx=20,bg='dodger blue',height="4",width="15",command=acc,bd=7).grid(row=1,column=1)
     Button(root,text='DEPOSIT',padx=15,pady=5,bg='orchid1',command=depos,height=3,width=8,bd=7).grid(row=2,column=0)
     Button(root,text='WITHDRAW',pady=3,padx=10,bg='blue violet',height=3,width=7,command=withd,bd=7).grid(row=2,column=1)
     Button(root,text='CHECK BALANCE',padx=15,pady=5,bg='DarkOliveGreen1',height=3,width=9,command=checkbal,bd=7).grid(row=2,column=2)
     Button(root,text='ABOUT',bg='ivory3',command=about,height=2,width=5,bd=7).grid(row=3,column=1)
     root.mainloop()
     
pro.config(bg='salmon')
Label(pro,text='PROJECT  ON  BANKING  SYSTEM',font='times 35 bold italic underline',relief='sunken',bg='khaki1').grid(row=0,sticky=W)
Label(pro,text='NAME -> PRAKHAR GUPTA',font='times 25 bold underline',bg='salmon').grid(row=3,column=0,sticky=W)
Label(pro,text='ENROLLMENT NO.-> 161B146',font='times 25 bold underline',bg='salmon').grid(row=4,column=0,sticky=W)
Label(pro,text='BATCH -> B-5 (BY)',font='times 25 bold underline',bg='salmon').grid(row=5,column=0,sticky=W)
Label(pro,text='EMAIL ID -> prakhargupta4145@gmail.com',font='times 25 bold underline',bg='salmon').grid(row=6,column=0,sticky=W)
Button(pro,text='CLICK HERE TO START',command=menu,bg='seashell3',height=4,bd=10).grid(row=10)
mainloop()
