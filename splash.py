from Tkinter import *
root=Tk()
k=PhotoImage(file='back.gif')
Label(root,image=k).pack()

    
root.after(5000,root.destroy)
root.mainloop()
from Tkinter import *
from tkMessageBox import *
import random
import tkMessageBox
import time;
import datetime
global page1


root=Tk()

    
def enter():
    root1=Tk()
    root1.geometry("1600x800+0+0")
    root1.attributes('-fullscreen',True)
    root1.title("PAGE 1")
    root1.configure(background="blue")
    

    f2=Frame(root1,width=900,height=650,bd=12,relief="flat")
    f2.pack(side=LEFT,fill="both",expand="yes")

    f3=Frame(root1,width=440,height=650,bd=12,relief="flat")
    f3.pack(side=RIGHT,fill="both",expand="yes")

    f2a=Frame(f2,width=900,height=330,bd=8,relief="flat")
    f2a.pack(side=BOTTOM,fill="both",expand="yes")
    f2b=Frame(f2,width=900,height=320,bd=6,relief="flat")
    f2b.pack(side=TOP,fill="both",expand="yes")

    f3a=Frame(f3,width=440,height=450,bd=12,relief="groove")
    f3a.pack(side=BOTTOM,fill="both",expand="yes")
    f3b=Frame(f3,width=440,height=250,bd=12,relief="groove")
    f3b.pack(side=TOP,fill="both",expand="yes")

    f2aa=Frame(f2a,width=400,height=330,bd=16,relief="flat")
    f2aa.pack(side=LEFT,fill="both",expand="yes")
    f2bb=Frame(f2a,width=400,height=330,bd=16,relief="flat")
    f2bb.pack(side=RIGHT,fill="both",expand="yes")
    f2cc=Frame(f2a,width=400,height=330,bd=16,relief="flat")
    f2cc.pack(fill="both",expand="yes")

    f2aa1=Frame(f2b,width=450,height=330,bd=14,relief="flat")
    f2aa1.pack(side=LEFT,fill="both",expand="yes")
    

    f2.configure(background="blue")
    f3.configure(background="red")


    

    a=IntVar()
    a1=IntVar()
    a2=IntVar()
    a3=IntVar()
    a4=IntVar()
    a5=IntVar()
    a6=IntVar()
    a7=IntVar()
    a8=IntVar()
    a9=IntVar()

    b=IntVar()
    b1=IntVar()
    b2=IntVar()
    b3=IntVar()
    b4=IntVar()
    

    d1=StringVar()
    d2=StringVar()
    d3=StringVar()
    d4=StringVar()
    d5=StringVar()
    d6=StringVar()
    d7=StringVar()
    d8=StringVar()
    d9=StringVar()
    d10=StringVar()
    d11=StringVar()
    d12=StringVar()
    d13=StringVar()
    d14=StringVar()
    d15=StringVar()

    
    def click():
        if a.get()==1:
            e1.configure(state=NORMAL)
        elif a.get()==0:
            e1.configure(state=DISABLED)
        if a1.get()==2:
            e2.configure(state=NORMAL)
        elif a1.get()==0:
            e2.configure(state=DISABLED)
        if a2.get()==3:
            e3.configure(state=NORMAL)
        elif a2.get()==0:
            e3.configure(state=DISABLED)
        if a3.get()==4:
            e4.configure(state=NORMAL)
        elif a3.get()==0:
            e4.configure(state=DISABLED)
        if a4.get()==5:
            e5.configure(state=NORMAL)
        elif a4.get()==0:
            e5.configure(state=DISABLED)
        if a5.get()==6:
            e6.configure(state=NORMAL)
        elif a5.get()==0:
            e6.configure(state=DISABLED)
        if a6.get()==7:
            e7.configure(state=NORMAL)
        elif a6.get()==0:
            e7.configure(state=DISABLED)
        if a7.get()==8: 
            e8.configure(state=NORMAL)
        elif a7.get()==0:
            e8.configure(state=DISABLED)
        if a8.get()==9:
            e9.configure(state=NORMAL)
        elif a8.get()==0:
            e9.configure(state=DISABLED)
        if a9.get()==10:
            e10.configure(state=NORMAL)
        elif a9.get()==0:
            e10.configure(state=DISABLED)
        if b.get()==11:
            f1.configure(state=NORMAL)
        elif b.get()==0:
            f1.configure(state=DISABLED)
        if b1.get()==12:
            f2.configure(state=NORMAL)
        elif b1.get()==0:
            f2.configure(state=DISABLED)
        if b2.get()==13:
            f3.configure(state=NORMAL)
        elif b2.get()==0:
            f3.configure(state=DISABLED)
        if b3.get()==14:
            f4.configure(state=NORMAL)
        elif b3.get()==0:
            f4.configure(state=DISABLED)
        if b4.get()==15:
            f5.configure(state=NORMAL)
        elif b4.get()==0:
            f5.configure(state=DISABLED)
            



    Label(f2aa,text="Daily use",fg='blue',font="Algerian 16 bold").grid(row=0,column=0,sticky=W)
    c1=Checkbutton(f2aa,font="Harrington 14 bold",text="Sanchi milk  (1 ltr)",command=click,variable=a,onvalue=1).grid(row=1,column=0,sticky=W)
    Label(f2aa,font="Arial 14 bold",text="50").grid(row=1,column=4)
    c2=Checkbutton(f2aa,font="Harrington 14 bold",text="Amul milk (1 ltr)",command=click,variable=a1,onvalue=2).grid(row=2,column=0,sticky=W)
    Label(f2aa,font="Arial 14 bold",text="48").grid(row=2,column=4)
    c3=Checkbutton(f2aa,font="Harrington 14 bold",text="Lassi(200 grm)",command=click,variable=a2,onvalue=3).grid(row=3,column=0,sticky=W)
    Label(f2aa,font="Arial 14 bold",text="35").grid(row=3,column=4)
    c4=Checkbutton(f2aa,font="Harrington 14 bold",text="Paneer(1 kg)",variable=a3,command=click,onvalue=4).grid(row=4,column=0,sticky=W)
    Label(f2aa,font="Arial 14 bold",text="330").grid(row=4,column=4)
    c5=Checkbutton(f2aa,font="Harrington 14 bold",text="Curd(200 grm)",command=click,variable=a4,onvalue=5).grid(row=5,column=0,sticky=W)
    Label(f2aa,font="Arial 14 bold",text="75").grid(row=5,column=4)

    e1=Entry(f2aa,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d1,state=DISABLED)
    e1.grid(row=1,column=1)
    e2=Entry(f2aa,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d2,state=DISABLED)
    e2.grid(row=2,column=1)
    e3=Entry(f2aa,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d3,state=DISABLED)
    e3.grid(row=3,column=1)
    e4=Entry(f2aa,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d4,state=DISABLED)
    e4.grid(row=4,column=1)
    e5=Entry(f2aa,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d5,state=DISABLED)
    e5.grid(row=5,column=1)

    Label(f2bb,text="Yummy",font="Algerian 16 bold").grid(row=0,column=0,sticky=W)
    c6=Checkbutton(f2bb,font="Harrington 14 bold",text="Bread",command=click,variable=a5,onvalue=6).grid(row=1,column=0,sticky=W)
    Label(f2bb,font="Arial 14 bold",text="30").grid(row=1,column=4)
    c7=Checkbutton(f2bb,font="Harrington 14 bold",text="Butter(200grm)",command=click,variable=a6,onvalue=7).grid(row=2,column=0,sticky=W)
    Label(f2bb,font="Arial 14 bold",text="120").grid(row=2,column=4)
    c8=Checkbutton(f2bb,font="Harrington 14 bold",text="Cheese(250 grm)",command=click,variable=a7,onvalue=8).grid(row=3,column=0,sticky=W)
    Label(f2bb,font="Arial 14 bold",text="160").grid(row=3,column=4)
    c9=Checkbutton(f2bb,font="Harrington 14 bold",text="Butter donut",command=click,variable=a8,onvalue=9).grid(row=4,column=0,sticky=W)
    Label(f2bb,font="Arial 14 bold",text="70").grid(row=4,column=4)
    c10=Checkbutton(f2bb,font="Harrington 14 bold",text="Mayonnaise(500 grm)",command=click,variable=a9,onvalue=10).grid(row=5,column=0,sticky=W)
    Label(f2bb,font="Arial 14 bold",text="100").grid(row=5,column=4)

    e6=Entry(f2bb,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d6,state=DISABLED)
    e6.grid(row=1,column=1)
    e7=Entry(f2bb,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d7,state=DISABLED)
    e7.grid(row=2,column=1)
    e8=Entry(f2bb,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d8,state=DISABLED)
    e8.grid(row=3,column=1)
    e9=Entry(f2bb,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d9,state=DISABLED)
    e9.grid(row=4,column=1)
    e10=Entry(f2bb,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d10,state=DISABLED)
    e10.grid(row=5,column=1)

    Label(f2cc,text="SWEET",font="Algerian 16 bold").grid(row=0,column=0,sticky=W)
    c11=Checkbutton(f2cc,font="Harrington 14 bold",text="Shri khand(200 grm)",command=click,variable=b,onvalue=11).grid(row=1,column=0,sticky=W)
    Label(f2cc,font="Arial 14 bold",text="60").grid(row=1,column=4)
    c12=Checkbutton(f2cc,font="Harrington 14 bold",text="Chenna Kheer(100 grm)",command=click,variable=b1,onvalue=12).grid(row=2,column=0,sticky=W)
    Label(f2cc,font="Arial 14 bold",text="18").grid(row=2,column=4)
    c13=Checkbutton(f2cc,font="Harrington 14 bold",text="Amul Chocolate",command=click,variable=b2,onvalue=13).grid(row=3,column=0,sticky=W)
    Label(f2cc,font="Arial 14 bold",text="110").grid(row=3,column=4)
    c14=Checkbutton(f2cc,font="Harrington 14 bold",text="Brownie",command=click,variable=b3,onvalue=14).grid(row=4,column=0,sticky=W)
    Label(f2cc,font="Arial 14 bold",text="50").grid(row=4,column=4)
    c15=Checkbutton(f2cc,font="Harrington 14 bold",text="pastry",command=click,variable=b4,onvalue=15).grid(row=5,column=0,sticky=W)
    Label(f2cc,font="Arial 14 bold",text="55").grid(row=5,column=4)

    f1=Entry(f2cc,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d11,state=DISABLED)
    f1.grid(row=1,column=1)
    f2=Entry(f2cc,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d12,state=DISABLED)
    f2.grid(row=2,column=1)
    f3=Entry(f2cc,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d13,state=DISABLED)
    f3.grid(row=3,column=1)
    f4=Entry(f2cc,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d14,state=DISABLED)
    f4.grid(row=4,column=1)
    f5=Entry(f2cc,bd=8,width=6,font="Arial 14 bold",justify='left',textvariable=d15,state=DISABLED)
    f5.grid(row=5,column=1)
    def qexit():
        qexit=askyesnocancel("Quit System","Do you want to quit?")
        if qexit>0:
            root1.destroy()
            return

    def reset():
        
        
        d1.set("0")
        d2.set("0")
        d3.set("0")
        d4.set("0")
        d5.set("0")
        d6.set("0")
        d7.set("0")
        d8.set("0")
        d9.set("0")
        d10.set("0")
        d11.set("0")
        d12.set("0")
        d13.set("0")
        d14.set("0")
        d15.set("0")

        a.set(0)
        a1.set(0)
        a2.set(0)
        a3.set(0)
        a4.set(0)
        a5.set(0)
        a6.set(0)
        a7.set(0)
        a8.set(0)
        a9.set(0)
        b.set(0)
        b1.set(0)
        b2.set(0)
        b3.set(0)
        b4.set(0)

        f2.configure(state=DISABLED)
        f3.configure(state=DISABLED)
        f4.configure(state=DISABLED)
        f5.configure(state=DISABLED)

        l1.destroy()
        l2.destroy()
        l3.destroy()
        l4.destroy()
        l5.destroy()
        
        l6.destroy()
        l7.destroy()
        l8.destroy()
        l9.destroy()
        l10.destroy()
        
        l11.destroy()
        l12.destroy()
        l13.destroy()
        l14.destroy()
        l15.destroy()
        
        t1.destroy()
        t2.destroy()
        t3.destroy()
        t4.destroy()

        t5.destroy()
        
        t6.destroy()
        t7.destroy()
        t8.destroy()
        t9.destroy()
        t10.destroy()
        
        t11.destroy()
        t12.destroy()
        t13.destroy()
        t14.destroy()
        t15.destroy()
        
       
    def printbill():
        global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15
        


        
        Label(f3a,text="Receipt:",font="Arial 16 bold").grid(row=1,column=0,sticky=W)
        if a.get()==1:
            l1=Label(f3a,text="Sanchi milk (l ltr)")
            l1.grid(row=16,column=0,sticky=W)
            if(e1.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            t1=Label(f3a,text= (int(e1.get()))*50)
            t1.grid(row=16,column=1,sticky=E)
        if a1.get()==2:
            l2=Label(f3a,text="Amul milk (1 ltr)")
            l2.grid(row=2,column=0,sticky=W)
            if(e2.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            t2=Label(f3a,text= (int(e2.get()))*48)
            t2.grid(row=2,column=1,sticky=E)
        if a2.get()==3:
            l3=Label(f3a,text=" Lassi(200 grm)")
            l3.grid(row=3,column=0,sticky=W)
            if(e3.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            t3=Label(f3a,text= (int(e3.get()))*35)
            t3.grid(row=3,column=1,sticky=E)
        if a3.get()==4:
            l4=Label(f3a,text="Paneer(1 kg)")
            l4.grid(row=4,column=0,sticky=W)
            if(e4.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            t4=Label(f3a,text= (int(e4.get()))*330)
            t4.grid(row=4,column=1,sticky=E)
        if a4.get()==5:
            l5=Label(f3a,text="Curd(200 grm)")
            l5.grid(row=5,column=0,sticky=W)
            if(e5.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            t5=Label(f3a,text= (int(e5.get()))*75)
            t5.grid(row=5,column=1,sticky=E)
        if a5.get()==6:
            l6=Label(f3a,text="Bread")
            l6.grid(row=6,column=0,sticky=W)
            if(e6.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            t6=Label(f3a,text= (int(e6.get()))*30)
            t6.grid(row=6,column=1,sticky=E)
        if a6.get()==7:
            l7=Label(f3a,text="Butter(200grm)")
            l7.grid(row=7,column=0,sticky=W)
            if(e7.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            t7=Label(f3a,text= (int(e7.get()))*120)
            t7.grid(row=7,column=1,sticky=E)
        if a7.get()==8:
            l8=Label(f3a,text="Cheese(250 grm)")
            l8.grid(row=8,column=0,sticky=W)
            if(e8.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            t8=Label(f3a,text= (int(e8.get()))*160)
            t8.grid(row=8,column=1,sticky=E)
        if a8.get()==9:
            l9=Label(f3a,text="Butter donut")
            l9.grid(row=9,column=0,sticky=W)
            if(e9.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            t9=Label(f3a,text= (int(e9.get()))*70)
            t9.grid(row=9,column=1,sticky=E)
        if a9.get()==10:
            l10=Label(f3a,text="Mayonnaise(500 grm)")
            l10.grid(row=17,column=0,sticky=W)
            if(e10.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            t10=Label(f3a,text= (int(e10.get()))*100)
            t10.grid(row=17,column=1,sticky=E)
        if b.get()==11:
            l11=Label(f3a,text="Shri khand(200 grm)")
            l11.grid(row=11,column=0,sticky=W)
            if(f1.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            t11=Label(f3a,text= (int(f1.get()))*60)
            t11.grid(row=11,column=1,sticky=E)
        if b1.get()==12:
            l12=Label(f3a,text="Chenna Kheer(100 grm)")
            l12.grid(row=12,column=0,sticky=W)
            if(f2.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            t12=Label(f3a,text= (int(f2.get()))*18)
            t12.grid(row=12,column=1,sticky=E)
        if b2.get()==13:
            l13=Label(f3a,text="Amul Chocolate")
            l13.grid(row=13,column=0,sticky=W)
            if(f3.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            t13=Label(f3a,text= (int(f3.get()))*110)
            t13.grid(row=13,column=1,sticky=E)
        if b3.get()==14:
            l14=Label(f3a,text="Amul icecream pack")
            l14.grid(row=14,column=0,sticky=W)
            if(f4.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            t14=Label(f3a,text= (int(f4.get()))*50)
            t14.grid(row=14,column=1,sticky=E)
        if b4.get()==15:
            l15=Label(f3a,text="pastry")
            l15.grid(row=15,column=0,sticky=W)
            if(f5.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            t15=Label(f3a,text= (int(f5.get()))*55)
            t15.grid(row=15,column=1,sticky=E)

    photo=PhotoImage(file="Python Project.gif")
    Label(f2aa1,image=photo).pack(fill='both',expand='yes')

    def new():
        #root1.destroy()
        master=Tk()
        master.attributes('-fullscreen',True)
        
        global num,num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15
        num,num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        #num=0,num1=0,num2=0,num3=0,num4=0,num5=0,num6=0,num7=0,num8=0,num9=0,num10=0,num11=0,num12=0,num13=0,num14=0,num15=0
        if a.get()==1:
            if(e1.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            num=(num+50)*(int(e1.get()))
        if a1.get()==2:
            if(e2.get()==''):
                tkMessageBox.showerror("error","please fill a value")

            num1=(num1+48)*(int(e2.get()))
        if a2.get()==3:
            if(e3.get()==''):
                tkMessageBox.showerror("error","please fill a value")

            num2=(num2+35)*(int(e3.get()))
        if a3.get()==4:
            if(e4.get()==''):
                tkMessageBox.showerror("error","please fill a value")
                
            num3=(num3+330)*(int(e4.get()))
        if a4.get()==5:
            if(e5.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            num4=(num4+75)*(int(e5.get()))
        if a5.get()==6:
            if(e6.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            num5=(num5+30)*(int(e6.get()))
        if a6.get()==7:
            if(e7.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            num6=(num6+120)*(int(e7.get()))
        if a7.get()==8:
            if(e8.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            
            num7=(num7+160)*(int(e8.get()))
        if a8.get()==9:
            if(e9.get()==''):
                tkMessageBox.showerror("error","please fill a value")

            num8=(num8+70)*(int(e9.get()))
        if a9.get()==10:
            if(e10.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            num9=(num9+100)*(int(e10.get()))
        if b.get()==11:
            if(f1.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            num10=(num10+60)*(int(f1.get()))
        if b1.get()==12:
            if(f2.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            num11=(num11+18)*(int(f2.get()))
        if b2.get()==13:
            if(f3.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            num12=(num12+110)*(int(f3.get()))
        if b3.get()==14:
            if(f4.get()==''):
                tkMessageBox.showerror("error","please fill a value")

            num13=(num13+50)*(int(f4.get()))
        if b4.get()==15:
            if(f5.get()==''):
                tkMessageBox.showerror("error","please fill a value")
            num14=(num14+55)*(int(f5.get()))

        total=num+num1+num2+num3+num4+num5+num6+num7+num8+num9+num10+num11+num12+num13+num14+num15
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master, text='\n\n\n\n thankyou for shopping \n\n visit again \n\n\n\n\n total price = ',fg='black',bg='light blue',font='forte 22').pack(side=TOP,anchor=CENTER)
        Label(master, text='\n'+'Rs'+' '+str(total),fg='white',bg='black',font='Times 24 bold').pack(side=TOP,anchor=CENTER)
        button4=Button(master,padx=16,pady=1,bd=4,fg='black',bg='blue',font="Arial 12 bold",width=5,text="EXIT",command=master.destroy,relief='flat')
        button4.pack(side=BOTTOM,fill="both")

        
    
    
            
        
    button1=Button(f3b,padx=16,pady=1,bd=4,fg='brown',bg='yellow',font="Harrington 12 bold",width=5,text="GENERATE BILL",command=printbill,relief='flat')
    button1.pack(side=TOP,fill="both")

    button2=Button(f3b,padx=16,pady=1,bd=4,fg='brown',bg='yellow',font="Harrington 12 bold",width=5,text="RESET",command=reset,relief='flat')
    button2.pack(fill="both")

    button4=Button(f3b,padx=16,pady=1,bd=4,fg='brown',bg='yellow',font="Harrington 12 bold",width=5,text="PRINT BILL",command=new,relief='flat')
    button4.pack(fill="both")

    button4=Button(f3b,padx=16,pady=1,bd=4,fg='brown',bg='yellow',font="Harrington 12 bold",width=5,text="EXIT",command=qexit,relief='flat')
    button4.pack(fill="both")
    
    root1.mainloop()

def q1():
    root.destroy()
    enter()
def aboutus():
    master=Tk()
        
    master.attributes('-fullscreen',True)

    shortcutbar = Frame(master, height=30, bg='light green')
    Button(shortcutbar,justify=CENTER,text='BACK',activeforeground='khaki',overrelief=SOLID,relief=GROOVE,command=master.destroy,bg='red',activebackground='#00A0A0').pack(side=RIGHT,anchor=NE,fill=Y)
    toolbar = Label(shortcutbar, text='Daily Dairy Products by ',bg='light green',fg='dark green',font='CalibriLight 30 bold')
    toolbar1=Label(shortcutbar, text='',bg='light green',fg='dark green',font='CalibriLight 15 bold')
    toolbar.pack(side=TOP,fill=X)
    toolbar1.pack(side=TOP,fill=X)
    shortcutbar.pack(side=TOP,fill=X)
    Label(master, text='').pack(side=TOP,fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master, text='\n\n\n\n\n Siddarth singh parihar (7415778033))',fg='red',font='Constantia 22 bold').pack(side=TOP,anchor=CENTER)
    Label(master, text='\n\n 161B233 (B-8) ',fg='brown',font='forte 22 bold').pack(side=TOP,anchor=CENTER)

    Label(master, text='Email :siddarth1998parihar@gmail.com',fg='#00A0A0',font='forte 18 bold',relief=RAISED,width=50).pack(side=BOTTOM,anchor=CENTER,fill=X)
    Label(master,text='Project designed by: Siddarth singh parihar',justify=CENTER,relief=RIDGE,fg='brown',font='Georgia 18 bold',bg='khaki').pack(side=BOTTOM,fill=X)
    
root.geometry("1600x800+0+0")
root.title("Daily Dairy ")
root.configure(background="green")
root.attributes('-fullscreen',True)


photo=PhotoImage(file="bgg1.gif")
l=Label(root,image=photo,font="Ravie 80 bold",text="  DAILY DAIRY  ",compound=CENTER,fg='BROWN',bg='black',bd=10)
Button(l,padx=16,pady=1,bd=4,fg='black',bg='sky blue',font="Narkisim 19 bold",width=9,height=2,text="BYE-BYE",command=root.destroy).pack(side=BOTTOM,anchor=W)
Button(l,padx=16,pady=1,bd=4,fg='black',bg='sky blue',font="Narkisim 19 bold",width=30,height=1,text="ENTER",command=q1).pack(side=BOTTOM,anchor=S)
Button(l,padx=16,pady=1,bd=4,fg='black',bg='sky blue',font="Narkisim 19 bold",width=9,height=2,text="ABOUT US",command=aboutus).pack(side=BOTTOM,anchor=SE)

l.pack(fill="both",expand="yes")
root.mainloop()
    


