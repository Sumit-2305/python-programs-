from tkinter import *
from tkinter import messagebox 
root=Tk()
#details given
root.title("SHOP DEPT DATA")
root.geometry("500x500")
# root.minsize("300,300")
# root.maxsize("400x400")
#shop name
var=Label(text="JAI PEETAMBRA KIRANA STORE")
var.grid(row=0,column=5,)

#file handling
def getvalue():
    print(f"{namevalue.get()},{datvalue.get()},{Amountvalue.get()},{no_of_item.get()},{mobile_value.get()},{Email_value.get()}\n")
    messagebox.showinfo('Message','Records insert succesfully!!')
    with open("costumer_records.txt","a") as f:
        f.write(f"{namevalue.get()},{datvalue.get()},{Amountvalue.get()},{no_of_item.get()},{Email_value.get()}\n")

def clearfunc():
    namevalue.set(""),datvalue.set(""),Amountvalue.set(""),no_of_item.set(""),mobile_value.set(""),Email_value.set("")
#coding start

N1=Label(text="Name")
N1.grid(row=1,column=3)
dat=Label(text="Date")
dat.grid(row=2,column=3)
Amo=Label(text="Amount")
Amo.grid(row=3,column=3)
ite=Label(text="Item no")
ite.grid(row=4,column=3)
mob=Label(text="MOBILE")
mob.grid(row=5,column=3)
ema=Label(text="Email")
ema.grid(row=6,column=3)

#variable Assign
namevalue=StringVar()
datvalue=StringVar()
Amountvalue=StringVar()
no_of_item=StringVar()
Email_value=StringVar()
mobile_value=StringVar()


#Entry var
n1val=Entry(root,textvariable=namevalue)
n1val.grid(row=1,column=5)
datval=Entry(root,textvariable=datvalue)
datval.grid(row=2,column=5)
Amoval=Entry(root,textvariable=Amountvalue)
Amoval.grid(row=3,column=5)
iteval=Entry(root,textvariable=no_of_item)
iteval.grid(row=4,column=5)
mob=Entry(root,textvariable=mobile_value)
mob.grid(row=5,column=5)
Emaval=Entry(root,textvariable=Email_value)
Emaval.grid(row=6,column=5)

b1=Button(text="Submit",command=getvalue)
b1.grid(row=7,column=5)
b2=Button(text="Reset",command=clearfunc)
b2.grid(row=7,column=6)
root.mainloop()