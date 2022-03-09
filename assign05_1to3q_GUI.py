#1st Code..
from tkinter import*

#Function of formulism of finding gst rate


def calculate_gst():
    original_cost = int(org_price.get())
    net_cost = int(net_price.get())
    gst_cal = ((net_cost - original_cost) * 100) / original_cost
    print("The original cost is: ", original_cost)
    print("The Net cost is : ", net_cost)
    print("The GST rate is : ", gst_cal)
    gst_rate.insert(12, str(gst_cal) + "%")

#function for clearing all the enteries


def clear():
    org_price.delete(0, END)
    net_price.delete(0, END)
    gst_rate.delete(0, END)


# driver code
root = Tk()
root.geometry('500x500')
root.configure(background='light grey')
root.title("GST RATE FINDER")

Entry_org_prize = Label(root, text='ENTER ORIGINAL PRICE', bg='light pink', font=("Comicsansm", 10, "bold"))
Entry_org_prize.grid(row=0, column=0)
Entry_Net_prize = Label(root, text="ENTER NET PRICE", bg='light blue', padx=20, font=("Comicsansm", 10, "bold"))
Entry_Net_prize.grid(row=1, column=0, pady=5)
B1 = Button(root, text="CALCULATE", padx=3, pady=3, bg='light grey', relief=SUNKEN, bd=3, font=("Comicsansm", 10, "bold"), command=calculate_gst, activebackground='light yellow')
B1.grid(row=2, column=1)
Gst_rate = Label(root, text="GST RATE IS :", bg='light yellow', padx=35, pady=3, font=("Comicsansm", 10, "bold"))
Gst_rate.grid(row=3, column=0, padx=10)
B2 = Button(root, text="CLEAR", padx=3, pady=3, bg='red', relief=SUNKEN, bd=5, font=('calibre', 12), command=clear, activebackground='light yellow')
B2.grid(row=4, column=1, padx=10 , pady=10)
org_price = Entry(root)
org_price.grid(row=0, column=1, padx=10)
net_price = Entry(root)
net_price.grid(row=1, column=1, padx=10)
gst_rate = Entry(root)
gst_rate.grid(row=3, column=1, padx=10, pady=10)
root.mainloop()


#2nd code
from tkinter import *
import calendar

# function for clearing inputs an outputs


def clear_all():
    en_1.delete(0, END)


# function for printing calender
def print_cal():
    # creating new root file for calender output
    root2 = Tk()
    root2.geometry('700x700')
    root2.configure(background='snow')
    root2.title("CALENDER OUTPUT..")
    year = int(en_1.get())
    cal_pr = calendar.calendar(year)
    lbl_3 = Label(root2, text=cal_pr)
    lbl_3.pack()
    root2.mainloop()


root1 = Tk()
root1.geometry('500x500')
root1.configure(background='old lace')
root1.title("Calender")
f1 = Frame(root1, borderwidth=8, bg="light grey", relief=RIDGE)
lbl_1 = Label(f1, text="CALENDER FINDER", bg='sky blue', font=(
    'calibre', 20, 'bold'), padx=650, pady=4)
lbl_1.grid(row=0, column=0, columnspan=10, pady=15)
en_1 = Entry(f1, font=('calibre', 15))
en_1.grid(row=2, column=1, pady=30)
lbl_2 = Label(f1, text="Enter the year you want calender of :",
              bg='pink', font=('calibre', 15), padx=3, pady=3)
lbl_2.grid(row=2, column=0, padx=10, pady=10)
but_1 = Button(f1, text="FIND/PRINT", relief='sunken', bd=5, bg='dark sea green', font=(
    'calibre', 15, 'bold'), fg="white", activebackground='dark olive green', command=print_cal)
but_1.grid(row=3, column=1, pady=5)
but_2 = Button(f1, text="CLEAR", relief='sunken', bd=5, bg='light sky blue4',
               command=clear_all, font=('calibre', 15, 'bold'), fg='white', activebackground='light sky blue1')
but_2.grid(row=5, column=1)
f1.grid(row=0, column=4)
root1.mainloop()


#calculator 3rd code
from tkinter import *


def sum():
    num_1 = float(e1.get())
    num_2 = float(e2.get())
    ans = num_1 + num_2
    en_3.insert(12, str(ans))


def subtract():
    num_1 = float(e1.get())
    num_2 = float(e2.get())
    ans = num_1 - num_2
    en_3.insert(12, str(ans))


def clear_all():
    e1.delete(0, END)
    e2.delete(0, END)
    en_3.delete(0, END)


def multiply():
    num_1 = float(e1.get())
    num_2 = float(e2.get())
    ans = num_1 * num_2
    en_3.insert(12, str(ans))


def divide():
    num_1 = float(e1.get())
    num_2 = float(e2.get())
    ans = num_1 / num_2
    en_3.insert(12, str(ans))


root = Tk()
root.configure(background='pink1')
root.geometry('600x600')
root.title('Basic Calculator')
f1 = Frame(root, borderwidth=8, bg="light grey", relief=RIDGE)
f1.grid(row=0, column=0, columnspan=4)
f2 = Frame(root, borderwidth=8, bg="cornflower blue", relief=SUNKEN)
f2.grid(row=3, column=0, columnspan=4)
l1 = Label(f1, text="CALCULATOR", relief='raised', bd=5, padx=190,
           bg='maroon', fg='white', font=('calibre', 20, 'bold'))
l1.grid(row=0, column=1, columnspan=4, pady=10)
l2 = Label(f2, text="Enter the first number", bg='mint cream', font=('calibre', 15, 'bold'))
l2.grid(row=1, column=0, columnspan=2)
l3 = Label(f2, text="Enter the second number", bg='mint cream', font=('calibre', 15, 'bold'))
l3.grid(row=2, column=0, padx=5, columnspan=2, pady=10)
l4 = Label(f2, text="RESULT", relief='ridge',
           bg='light blue', font=('calibre', 15, 'bold'))
l4.grid(row=7, column=0)
e1 = Entry(f2)
e1.grid(row=1, column=3, columnspan=4)
e2 = Entry(f2)
e2.grid(row=2, column=3, columnspan=4)
en_3 = Entry(f2)
en_3.grid(row=7, column=1, columnspan=4)
but_1 = Button(f2, text='addition(+)', bg='light grey', command=sum)
but_1.grid(row=3, column=0)
but_2 = Button(f2, text='subtraction(-)', bg='light grey', command=subtract)
but_2.grid(row=3, column=1)
but_3 = Button(f2, text='multipication(*)', bg='light grey', command=multiply)
but_3.grid(row=3, column=2)
but_4 = Button(f2, text='division(/)', bg='light grey', command=divide)
but_4.grid(row=3, column=3)
but_5 = Button(root,padx=5, pady=5, text="CLEAR", bg='RED', bd=3, relief='raised', command=clear_all)
but_5.grid(row=8, column=1)

root.mainloop()

