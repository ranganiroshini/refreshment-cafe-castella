from tkinter import*
from tkinter import messagebox
import random
import time;
import datetime;
import sqlite3
mydb = sqlite3.connect('miniproject.db')
from tkinter import *
import sqlite3

window=Tk()
window.geometry("300x150")

def login():
	def login_database():
		conn=sqlite3.connect("1.db")
		cur=conn.cursor()
		cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
		row=cur.fetchall()
		conn.close()
		print(row)
		if row!=[]:
			user_name=row[0][1]
			l3.config(text="user name found with name: "+user_name)
		else:
			l3.config(text="user not found ")



	window.destroy()
	login_window=Tk()
	login_window.geometry("400x250")
	l1=Label(login_window,text="email",font="times 20")
	l1.grid(row=1,column=1)
	l2=Label(login_window,text="password",font="times 20")
	l2.grid(row=2,column=1)
	l3=Label(login_window,font="times 20")
	l3.grid(row=5,column=2)

	email_text=StringVar()
	e1=Entry(login_window,textvariable=email_text)
	e1.grid(row=1,column=2)
	password_text=StringVar()
	e2=Entry(login_window,textvariable=password_text)
	e2.grid(row=2,column=2)


	b1=Button(login_window,text="login",width=20,command=login_database)
	b1.grid(row=4,column=2)
	login_window.mainloop()




def signup():


	def signup_database():
		conn=sqlite3.connect("1.db")
		cur=conn.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text, password text)")
		cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
		l4=Label(signup_window,text="account created",font="times 15")
		l4.grid(row=6,column=2)
		conn.commit()
		conn.close()





	window.destroy()
	signup_window=Tk()
	signup_window.geometry("400x250")
	l1=Label(signup_window,text="user name",font="times 20")
	l1.grid(row=1,column=1)
	l2=Label(signup_window,text="user email",font="times 20")
	l2.grid(row=2,column=1)
	l3=Label(signup_window,text="user password",font="times 20")
	l3.grid(row=3,column=1)


	name_text=StringVar()
	e1=Entry(signup_window,textvariable=name_text)
	e1.grid(row=1,column=2)
	email_text=StringVar()
	e2=Entry(signup_window,textvariable=email_text)
	e2.grid(row=2,column=2)
	password_text=StringVar()
	e3=Entry(signup_window,textvariable=password_text)
	e3.grid(row=3,column=2)

	b1=Button(signup_window,text="login",width=20,command=signup_database)
	b1.grid(row=4,column=2)







l1=Label(window,text="what do you want to do",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

b1=Button(window,text="login",width=20,command=login)
b1.grid(row=2,column=2)

b2=Button(window,text="signup",width=20,command=signup)
b2.grid(row=2,column=3)


window.mainloop()

c = mydb.cursor()
root =Tk()
root.geometry("1350x750+0+0")
messagebox.askyesno("WELCOME ADMIN","login to your page???")

def check():
    u_name=un.get()
    p_word=pw.get()
    conn=mysql.connector.connect(host="localhost",user="root",passwd="bhav@6546",database="coffedatabase")
    cur=conn.cursor()
    query="select * from admin where name='"+u_name+"';"
    cur.execute(query)
    result=cur.fetchall()
    conn.commit()
SEARCH = StringVar()
a = StringVar()

root.mainloop()

def Ok():
    uname = e1.get()
    password = e2.get()
 
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
 
 
    elif(uname == "Admin" and password == "123"):
 
        messagebox.showinfo("","successfully loggedin")
        root.destroy()
 
    else :
        messagebox.showinfo("","Incorrent Username and Password")
 
 
root = Tk()
root.title("Login")
root.geometry("300x200")
global e1
global e2
 
Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")
 
 
Button(root, text="Login", command=Ok ,height = 3, width = 13).place(x=10, y=100)
 
root.mainloop()




    
# Basic window is created
root =Tk()
root.geometry("1350x750+0+0")
root.title("fast food")
root.configure(background='black')

Tops = Frame(root,width=1350, height=70, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root,width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root,width=440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1,width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a=Frame(f1,width=900, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2=Frame(f2,width=440, height=450, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2=Frame(f2,width=440, height=50, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa=Frame(f1a,width=400, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a,width=400, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a,width=450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)
f2ab=Frame(f2a,width=450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')
#=====price
PriceLatte=65
PriceEspresso= 115
PriceIced_Latte=115
PriceVale_Coffee=155
PriceCappuccino=135
PriceAfrican_Coffee=125
PriceAmerican_Coffee=125
PriceIced_Cappuccino=125

PriceCoffee_Cakes=130
PriceRed_Velvet_Cake=135
PriceBlack_Forest_Cake=145
PriceBoston_Cream_Cake=125
PriceLagos_Chocolate_Cake=140
PriceKilburn_Chocolate_Cake=155
PriceCarlton_Hill_Chocolate_Cake=115
PriceQueen_Park_Chocolate_Cake=120
#============CostofItem
def CostofItem():
    Item1 = float(E_Latte.get())
    Item2 = float(E_Espresso.get())
    Item3 = float(E_Iced_Latte.get())
    Item4 = float(E_Vale_Coffee.get())
    Item5 = float(E_Cappuccino.get())
    Item6 = float(E_African_Coffee.get())
    Item7 = float(E_American_Coffee.get())
    Item8 = float(E_Iced_Cappuccino.get())
    
    Item9 = float(E_Coffee_Cakes.get())
    Item10 = float(E_Red_Velvet_Cake.get())
    Item11 = float(E_Black_Forest_Cake.get())
    Item12 = float(E_Boston_Cream_Cake.get())
    Item13 = float(E_Lagos_Chocolate_Cake.get())
    Item14 = float(E_Kilburn_Chocolate_Cake.get())
    Item15 = float(E_Carlton_Hill_Chocolate_Cake.get())
    Item16 = float(E_Queen_Park_Chocolate_Cake.get())

    ItemDiscount=float(E_Discount.get())

 #==========TotalCost
    Total = ((Item1 * PriceLatte) + (Item2 * PriceEspresso )
             + (Item3 * PriceIced_Latte) + (Item4 * PriceVale_Coffee)
             + (Item5 * PriceCappuccino ) + (Item6 * PriceAfrican_Coffee)
             + (Item7 * PriceAmerican_Coffee) + (Item8 * PriceIced_Cappuccino)
             + (Item9 * PriceCoffee_Cakes) + (Item10 * PriceRed_Velvet_Cake)
             + (Item11 * PriceBlack_Forest_Cake) + (Item12 * PriceBoston_Cream_Cake)
             + (Item13 *PriceLagos_Chocolate_Cake) + (Item14 * PriceKilburn_Chocolate_Cake)
             + (Item15 *PriceCarlton_Hill_Chocolate_Cake) + (Item16 * PriceQueen_Park_Chocolate_Cake))
    Grand_Total = str(float(Total * float(1 - (ItemDiscount/100))))
    E_Total.set(str(Total))
    E_Grand_Total.set(Grand_Total)
             

#====================================== functions
def Sub():
    Return = str(float(E_Pay.get()) - float(E_Grand_Total.get()))
    E_Return.set(Return)


def Apply():
    E_Grand_Total.set(str(float(E_Total.get()) * (1 - (float(E_Discount.get())/100))))
    
def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to LOG OUT?")
    if qExit > 0:
        root.destroy()
        return

def Reset():

    SetVal() ## set 0
    var = [var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16]
    for i in range(16):
        var[i].set("0")

    var20.set("0")

    arr = [txtLatte,txtEspresso,txtIced_Latte,txtVale_Coffee,txtCappuccino,txtAfrican_Coffee,
           txtAmerican_Coffee,txtIced_Cappuccino,txtCoffee_Cakes,txtRed_Velvet_Cake,txtBlack_Forest_Cake,
           txtBoston_Cream_Cake,txtLagos_Chocolate_Cake,txtKilburn_Chocolate_Cake,
           txtCarlton_Hill_Chocolate_Cake,txtQueen_Park_Chocolate_Cake]
    for i in range(16):
        arr[i].configure(state=DISABLED)
    

    txtDiscount.configure(state=DISABLED)
#====Recieps===

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+randomRef)

    txtReceipt.insert(END,'Receipt Ref: '+ Receipt_Ref.get() +"\t\t\t"+ DateofOrder.get()+' '+ TimeofOrder.get()+"\n")
    
    txtReceipt.insert(END,'Item\t\t\t'+'Qty\t\t'+"price\n")
    txtReceipt.insert(END,"--------------------------------------------------------------------------------\n")
    if E_Latte.get()!='0':
        txtReceipt.insert(END,'Latte:\t\t\t'+E_Latte.get()+'\t'+ str(int(E_Latte.get())*PriceLatte) +"\n")
    if E_Espresso.get()!='0':
        txtReceipt.insert(END,'Espresso: \t\t\t'+E_Espresso.get()+'\t'+ str(int(E_Espresso.get())* PriceEspresso) +"\n")
    if E_Iced_Latte.get()!='0':
        txtReceipt.insert(END,'Iced_Latte:\t\t '+E_Iced_Latte.get()+'\t'+ str(int(E_Iced_Latte.get())* PriceIced_Latte) +"\n")
    if E_Vale_Coffee.get()!='0':
        txtReceipt.insert(END,'Vale_Coffee: \t\t\t'+E_Vale_Coffee.get()+'\t'+ str(int(E_Vale_Coffee.get())* PriceVale_Coffee) +"\n")
    if E_Cappuccino.get()!='0':
        txtReceipt.insert(END,'Cappuccino: \t\t\t'+E_Cappuccino.get()+'\t'+ str(int(E_Cappuccino.get())* PriceCappuccino) +"\n")
    if E_African_Coffee.get()!='0':
        txtReceipt.insert(END,'African_Coffee: \t\t\t'+E_African_Coffee.get()+'\t'+ str(int(E_African_Coffee.get())* PriceAfrican_Coffee) +"\n")
    if E_American_Coffee.get()!='0':
        txtReceipt.insert(END,'American_Coffee: \t\t\t'+E_American_Coffee.get()+'\t'+ str(int(E_American_Coffee.get())* PriceAmerican_Coffee) +"\n")
    if E_Iced_Cappuccino.get()!='0':
        txtReceipt.insert(END,'Iced_Cappuccino:\t\t\t '+E_Iced_Cappuccino.get()+'\t'+ str(int(E_Iced_Cappuccino.get())* PriceIced_Cappuccino) +"\n")
    if E_Coffee_Cakes.get()!='0':
        txtReceipt.insert(END,'Coffee_Cakes: \t\t'+E_Coffee_Cakes.get()+'\t'+ str(int(E_Coffee_Cakes.get())* PriceCoffee_Cakes) +"\n")
    if E_Red_Velvet_Cake.get()!='0':
        txtReceipt.insert(END,'Red_Velvet_Cake: \t\t'+E_Red_Velvet_Cake.get()+'\t'+ str(int(E_Red_Velvet_Cake.get())* PriceRed_Velvet_Cake) +"\n")
    if E_Black_Forest_Cake.get()!='0':
        txtReceipt.insert(END,'Black_Forest_Cake: \t\t'+E_Black_Forest_Cake.get()+'\t'+ str(int(E_Black_Forest_Cake.get())* PriceBlack_Forest_Cake) +"\n")
    if E_Boston_Cream_Cake.get()!='0':
        txtReceipt.insert(END,'Boston_Cream_Cake: \t\t'+E_Boston_Cream_Cake.get()+'\t\t\t\t'+ str(int(E_Boston_Cream_Cake.get())* PriceBoston_Cream_Cake) +"\n")
    if E_Lagos_Chocolate_Cake.get()!='0':
        txtReceipt.insert(END,'Lagos_Chocolate_Cake: \t\t'+E_Lagos_Chocolate_Cake.get()+'\t\t\t\t'+ str(int(E_Lagos_Chocolate_Cake.get())* PriceLagos_Chocolate_Cake) +"\n")
    if E_Kilburn_Chocolate_Cake.get()!='0':
        txtReceipt.insert(END,'Kilburn_Chocolate_Cake: \t\t'+E_Kilburn_Chocolate_Cake.get()+'\t\t'+ str(int(E_Kilburn_Chocolate_Cake.get())* PriceE_Kilburn_Chocolate_Cake) +"\n")
    if E_Carlton_Hill_Chocolate_Cake.get()!='0':
        txtReceipt.insert(END,'Carlton_Hill_Chocolate_Cake: \t\t'+E_Carlton_Hill_Chocolate_Cake.get()+"\t\t\t"+ str(int(E_Carlton_Hill_Chocolate_Cake.get())* PriceCarlton_Hill_Chocolate_Cake) +"\n")
    if E_Queen_Park_Chocolate_Cake.get()!='0':
        txtReceipt.insert(END,'Queen_Park_Chocolate_Cake: \t\t'+E_Queen_Park_Chocolate_Cake.get()+"\t\t\t"+ str(int(E_Queen_Park_Chocolate_Cake.get())* PriceQueen_Park_Chocolate_Cake) +"\n")   
    txtReceipt.insert(END,"---------------------------------------------------------------------------------\n")
    txtReceipt.insert(END,'Sub_Total: \t\t\t\t\t'+E_Total.get()+"\n")
    txtReceipt.insert(END,'Discount: \t\t\t\t\t-'+str(float(E_Discount.get())/100*float(E_Total.get()))+"\n")
    txtReceipt.insert(END,'Grand_Total: \t\t\t\t\t'+E_Grand_Total.get()+"\n")

#=======Heading
        
lblInfo=Label(Tops, font =('arrial',25 , 'bold'), text="\t\t\t REFRESHMENT CAFE CASTELLA  \t\t\t  ",bd=25)
lblInfo.grid(row=0,column=0)
#========

def chkbutton_value():
    if var1.get() == 1 :
        txtLatte.configure(state= NORMAL)
    elif var1.get() == 0:
        txtLatte.configure(state= DISABLED)
        E_Latte.set("0")
        
    if var2.get() == 1 :
        txtEspresso.configure(state=NORMAL)
    elif var2.get() == 0:
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")

    if var3.get() == 1 :
        txtIced_Latte.configure(state= NORMAL)
    elif var3.get() == 0:
        txtIced_Latte.configure(state= DISABLED)
        E_Iced_Latte.set("0")
        
    if var4.get() == 1 :
        txtVale_Coffee.configure(state=NORMAL)
    elif var4.get() == 0:
        txtVale_Coffee.configure(state=DISABLED)
        E_Vale_Coffee.set("0")

    if var5.get() == 1 :
        txtCappuccino.configure(state= NORMAL)
    elif var5.get() == 0:
        txtCappuccino.configure(state= DISABLED)
        E_Cappuccino.set("0")
        
    if var6.get() == 1 :
        txtAfrican_Coffee.configure(state=NORMAL)
    elif var6.get() == 0:
        txtAfrican_Coffee.configure(state=DISABLED)
        E_African_Coffee.set("0")

    if var7.get() == 1 :
        txtAmerican_Coffee.configure(state= NORMAL)
    elif var7.get() == 0:
        txtAmerican_Coffee.configure(state= DISABLED)
        E_American_Coffee.set("0")
        
    if var8.get() == 1 :
        txtIced_Cappuccino.configure(state=NORMAL)
    elif var8.get() == 0:
        txtIced_Cappuccino.configure(state=DISABLED)
        E_Iced_Cappuccino.set("0")

    if var9.get() == 1 :
        txtCoffee_Cakes.configure(state= NORMAL)
    elif var9.get() == 0:
        txtCoffee_Cakes.configure(state= DISABLED)
        E_Coffee_Cakes.set("0")
        
    if var10.get() == 1 :
        txtRed_Velvet_Cake.configure(state=NORMAL)
    elif var10.get() == 0:
        txtRed_Velvet_Cake.configure(state=DISABLED)
        E_Red_Velvet_Cake.set("0")

    if var11.get() == 1 :
        txtBlack_Forest_Cake.configure(state= NORMAL)
    elif var11.get() == 0:
        txtBlack_Forest_Cake.configure(state= DISABLED)
        E_Black_Forest_Cake.set("0")
        
    if var12.get() == 1 :
        txtBoston_Cream_Cake.configure(state=NORMAL)
    elif var12.get() == 0:
        txtBoston_Cream_Cake.configure(state=DISABLED)
        E_Boston_Cream_Cake.set("0")

    if var13.get() == 1 :
        txtLagos_Chocolate_Cake.configure(state= NORMAL)
    elif var13.get() == 0:
        txtLagos_Chocolate_Cake.configure(state= DISABLED)
        E_Lagos_Chocolate_Cake.set("0")
        
    if var14.get() == 1 :
        txtKilburn_Chocolate_Cake.configure(state=NORMAL)
    elif var14.get() == 0:
        txtKilburn_Chocolate_Cake.configure(state=DISABLED)
        E_Kilburn_Chocolate_Cake.set("0")

    if var15.get() == 1 :
        txtCarlton_Hill_Chocolate_Cake.configure(state= NORMAL)
    elif var15.get() == 0:
        txtCarlton_Hill_Chocolate_Cake.configure(state= DISABLED)
        E_Carlton_Hill_Chocolate_Cake.set("0")
        
    if var16.get() == 1 :
        txtQueen_Park_Chocolate_Cake.configure(state=NORMAL)
    elif var16.get() == 0:
        txtQueen_Park_Chocolate_Cake.configure(state=DISABLED)
        E_Queen_Park_Chocolate_Cake.set("0")

    if var20.get() == 1 : 
        txtDiscount.configure(state=NORMAL)
    elif var20.get() == 0:
        txtDiscount.configure(state=DISABLED)
        E_Discount.set("0")
        

#======= variable
           
var0 = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

var20 = IntVar()#
DateofOrder=StringVar()
TimeofOrder=StringVar()
Receipt_Ref=StringVar()


E_Latte=StringVar()
E_Espresso=StringVar()
E_Iced_Latte=StringVar()
E_Vale_Coffee=StringVar()
E_Cappuccino=StringVar()
E_African_Coffee=StringVar()
E_American_Coffee=StringVar()
E_Iced_Cappuccino=StringVar()

E_Coffee_Cakes=StringVar()
E_Red_Velvet_Cake=StringVar()
E_Black_Forest_Cake=StringVar()
E_Boston_Cream_Cake=StringVar()
E_Lagos_Chocolate_Cake=StringVar()
E_Kilburn_Chocolate_Cake=StringVar()
E_Carlton_Hill_Chocolate_Cake=StringVar()
E_Queen_Park_Chocolate_Cake=StringVar()
E_Total= StringVar()
E_Discount=StringVar()#
E_Grand_Total = StringVar()
E_Return =StringVar()
E_Pay = StringVar()

def SetVal():
    arr = [E_Latte,E_Espresso,E_Iced_Latte,E_Vale_Coffee,E_Cappuccino,E_African_Coffee,
           E_American_Coffee,E_Iced_Cappuccino,E_Coffee_Cakes,E_Red_Velvet_Cake,E_Black_Forest_Cake,
           E_Boston_Cream_Cake,E_Lagos_Chocolate_Cake,E_Kilburn_Chocolate_Cake,
           E_Carlton_Hill_Chocolate_Cake,E_Queen_Park_Chocolate_Cake,
           E_Discount,E_Total,E_Grand_Total,E_Return,E_Pay]
    for i in range(21):
        
        arr[i].set("0")

SetVal()


##E_Latte.set("0")
##E_Espresso.set("0")
##E_Iced_Latte.set("0")
##E_Vale_Coffee.set("0")
##E_Cappuccino.set("0")
##E_African_Coffee.set("0")
##E_American_Coffee.set("0")
##E_Iced_Cappuccino.set("0")
##E_Coffee_Cakes.set("0")
##E_Red_Velvet_Cake.set("0")
##E_Black_Forest_Cake.set("0")
##E_Boston_Cream_Cake.set("0")
##E_Lagos_Chocolate_Cake.set("0")
##E_Kilburn_Chocolate_Cake.set("0")
##E_Carlton_Hill_Chocolate_Cake.set("0")
##E_Queen_Park_Chocolate_Cake.set("0")

##E_Discount.set("0")#
##E_Total.set("0")
##E_Grand_Total.set("0")
##E_Return.set("0")
##E_Pay.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))
TimeofOrder.set(time.strftime("%H:%M:%S"))

#----------------------------------drink--------------------------
Latte = Checkbutton(f1aa, text="Latte ", variable = var1, onvalue = 1, offvalue =0,
                    font=('arial', 18, 'bold'),command=chkbutton_value).grid(row = 0,sticky=W)

Espresso = Checkbutton(f1aa, text="Espresso ", variable = var2, onvalue = 1, offvalue =0,
                    font=('arial', 18, 'bold'),command=chkbutton_value).grid(row = 1,sticky=W)

Iced_Latte = Checkbutton(f1aa, text="Iced_Latte   ", variable = var3, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 2,sticky=W)

Vale_Coffee = Checkbutton(f1aa, text="Vale_Coffee ", variable = var4, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 3,sticky=W)

Cappuccino = Checkbutton(f1aa, text="Cappuccino ", variable = var5, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 4,sticky=W)

African_Coffee = Checkbutton(f1aa, text="African_Coffee ", variable = var6, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 5,sticky=W)

American_Coffee = Checkbutton(f1aa, text="American_Coffee ", variable = var7, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 6,sticky=W)

Iced_Cappuccino= Checkbutton(f1aa, text="Iced_Cappuccino", variable = var8, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 7,sticky=W)

#=======================Cake==========================
Coffee_Cakes= Checkbutton(f1ab, text="Coffee_Cakes", variable = var9, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 0,sticky=W)

Red_Velvet_Cake= Checkbutton(f1ab, text="Red_Velvet_Cake ", variable = var10, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 1,sticky=W)

Black_Forest_Cake= Checkbutton(f1ab, text="Black_Forest_Cake ", variable = var11, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 2,sticky=W)

Boston_Cream_Cake= Checkbutton(f1ab, text="Boston_Cream_Cake ", variable = var12, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 3,sticky=W)

Lagos_Chocolate_Cake= Checkbutton(f1ab, text="Lagos_Chocolate_Cake ", variable = var13, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 4,sticky=W)

Kilburn_Chocolate_Cake= Checkbutton(f1ab, text="Kilburn_Chocolate_Cake", variable = var14, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 5,sticky=W)

Carlton_Hill_chocolate_Cake= Checkbutton(f1ab, text="Carlton_Hill_chocolate_Cake ", variable = var15, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 6,sticky=W)

Queen_Park_Chocolate_Cake= Checkbutton(f1ab, text="Queen_Park_Chocolate_Cake", variable = var16, onvalue = 1, offvalue =0,
                    font =('arial', 18, 'bold'),command=chkbutton_value).grid(row = 7,sticky=W)


#---------------------------Widget-----------
txtLatte = Entry(f1aa,font=('arial',16,'bold'), textvariable=E_Latte,
                 bd=8, width=6, justify='left', state= DISABLED)
txtLatte.grid(row =0, column=1)
txtEspresso = Entry(f1aa,font=('arial',16,'bold'), textvariable=E_Espresso,
                    bd=8, width=6, justify='left', state=DISABLED)
txtEspresso.grid(row =1, column=1)
txtIced_Latte = Entry(f1aa,font=('arial',16,'bold'), textvariable=E_Iced_Latte,
                      bd=8, width=6, justify='left', state=DISABLED)
txtIced_Latte.grid(row =2, column=1)
txtVale_Coffee = Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Vale_Coffee,
                 bd=8, width=6, justify='left', state=DISABLED)
txtVale_Coffee.grid(row =3, column=1)
txtCappuccino = Entry(f1aa,font=('arial',16,'bold'),textvariable=E_Cappuccino,
                 bd=8, width=6, justify='left', state=DISABLED)
txtCappuccino.grid(row =4, column=1)
txtAfrican_Coffee = Entry(f1aa,font=('arial',16,'bold'),textvariable=E_African_Coffee,
                 bd=8, width=6, justify='left', state=DISABLED)
txtAfrican_Coffee.grid(row =5, column=1)
txtAmerican_Coffee = Entry(f1aa,font=('arial',16,'bold'),textvariable=E_American_Coffee,
                 bd=8, width=6, justify='left', state=DISABLED)
txtAmerican_Coffee.grid(row =6, column=1)
txtIced_Cappuccino= Entry(f1aa,font=('arial',16,'bold'), textvariable=E_Iced_Cappuccino,
                 bd=8, width=6, justify='left', state=DISABLED)
txtIced_Cappuccino.grid(row =7, column=1)

#--------------------
txtCoffee_Cakes= Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Coffee_Cakes,
                       bd=8, width=6, justify='left', state=DISABLED)
txtCoffee_Cakes.grid(row =0, column=1)
txtRed_Velvet_Cake = Entry(f1ab,font=('arial',16,'bold'), textvariable=E_Red_Velvet_Cake,
                           bd=8, width=6, justify='left', state=DISABLED)
txtRed_Velvet_Cake.grid(row =1, column=1)
txtBlack_Forest_Cake = Entry(f1ab,font=('arial',16,'bold'),textvariable=E_Black_Forest_Cake,
                             bd=8, width=6, justify='left', state=DISABLED)
txtBlack_Forest_Cake.grid(row =2, column=1)
txtBoston_Cream_Cake= Entry(f1ab,font=('arial',16,'bold'), textvariable=E_Boston_Cream_Cake,
                             bd=8, width=6, justify='left', state=DISABLED)
txtBoston_Cream_Cake.grid(row =3, column=1)
txtLagos_Chocolate_Cake= Entry(f1ab,font=('arial',16,'bold'), textvariable=E_Lagos_Chocolate_Cake,
                                bd=8, width=6, justify='left', state=DISABLED)
txtLagos_Chocolate_Cake.grid(row =4, column=1)
txtKilburn_Chocolate_Cake= Entry(f1ab,font=('arial',16,'bold'), textvariable=E_Kilburn_Chocolate_Cake,
                                  bd=8, width=6, justify='left', state=DISABLED)
txtKilburn_Chocolate_Cake.grid(row =5, column=1)
txtCarlton_Hill_Chocolate_Cake= Entry(f1ab,font=('arial',16,'bold'), textvariable=E_Carlton_Hill_Chocolate_Cake,
                                       bd=8, width=6, justify='left', state=DISABLED)
txtCarlton_Hill_Chocolate_Cake.grid(row =6, column=1)
txtQueen_Park_Chocolate_Cake= Entry(f1ab,font=('arial',16,'bold'), textvariable=E_Queen_Park_Chocolate_Cake,
                                     bd=8, width=6, justify='left', state=DISABLED)
txtQueen_Park_Chocolate_Cake.grid(row =7, column=1)

                                                                              
#=================
Total = Label(f2aa,font=('arial',16,'bold'), text="Total \t",bd =8)
Total.grid(row=2, column=0, sticky=W)
txtTotal=Entry(f2aa,font=('arial',16,'bold'), textvariable=E_Total, bd=8, width=10, justify='left',state = DISABLED)
txtTotal.grid(row=2,column=1, sticky=W)
Grand_Total = Label(f2aa,font=('arial',16,'bold'), text="Grand Total \t",bd =8)
Grand_Total.grid(row=3, column=0, sticky=W)
txtGrand_Total=Entry(f2aa,font=('arial',16,'bold'), textvariable=E_Grand_Total,
                     bd=8,width=10, justify='left', state=DISABLED)
txtGrand_Total.grid(row=3,column=1, sticky=W)
lblCostofDrink = Label(f2aa,font=('arial',16,'bold'), text="Coupon Code",bd =8)
lblCostofDrink.grid(row=4, column=0, sticky=W)
txtCostofDrink=Entry(f2aa,font=('arial',16,'bold'),bd=8,width=10, justify='left')
txtCostofDrink.grid(row=4,column=1, sticky=W)
#===========================
#============================ discount & Coupon

Discount = Checkbutton(f2ab, text="Discount \t", variable = var20, onvalue = 1, offvalue =0,
                    font=('arial', 16, 'bold'),command=chkbutton_value).grid(row = 2,sticky=W)
txtDiscount=Entry(f2ab,font=('arial',16,'bold'), textvariable=E_Discount,
                  bd=8, width=10, justify='left', state=DISABLED)
txtDiscount.grid(row=2,column=1, sticky=W)
#subbtn
btnAppy = Button(f2ab, padx=16 , pady=1, bd=4, fg="black", font=('arial',16,'bold'),
                  width=5, text="Apply",bg="yellow",command=Apply).grid(row=2,column=2, sticky=W)
#===
Pay = Label(f2ab,font=('arial',16,'bold'), text="Cash Pay",bd =4)
Pay.grid(row=3, column=0, sticky=W)
txtPay=Entry(f2ab,font=('arial',16,'bold'), textvariable=E_Pay, bd=4, width=10, justify='left')
txtPay.grid(row=3,column=1, sticky=W)
#subbtn
btnSub = Button(f2ab, padx=16 , pady=1, bd=4, fg="black", font=('arial',16,'bold'),
                  width=5, text="=", command=Sub).grid(row=3,column=2, sticky=W)
#===
Return = Label(f2ab,font=('arial',16,'bold'), text="Return \t",bd =4)
Return.grid(row=4, column=0, sticky=W)
txtReturn=Entry(f2ab,font=('arial',16,'bold'), textvariable=E_Return,
                bd=4, width=10, justify='left')
txtReturn.grid(row=4,column=1, sticky=W)

#===================
lblReceipt = Label(ft2,font=('arial', 12, 'bold'), text='Reciept', bd=2, anchor='w')
lblReceipt.grid(row=0, column=0 , sticky=W)
txtReceipt = Text(ft2, width=50, height=28, bg="light pink", bd=2,
                  font=('arial', 11, 'bold'))
txtReceipt.grid(row=1, column=0)

#======================== button===============
btnTotal = Button(fb2, padx=25 , pady=1, bd=3, fg="black", font=('arial',10,'bold'),
                  width=1, text="Total ",bg="GREEN",command= CostofItem).grid(row=0,column=0)
btnReceipt = Button(fb2, padx=25 , pady=1, bd=3, fg="black", font=('arial',10,'bold'),
                  width=2, text="Receipt ", bg="purple",command=Receipt).grid(row=0,column=1)
btnReset = Button(fb2, padx=25 , pady=1, bd=3, fg="black", font=('arial',10,'bold'),
                  width=1, text="Reset ", bg="blue",command=Reset).grid(row=0,column=2)
btnExit = Button(fb2, padx=25, pady=1, bd=3, fg="black", font=('arial',10,'bold'),
                  width=1, text="Exit ",bg="red", command= qExit).grid(row=0,column=3)

root.mainloop()
