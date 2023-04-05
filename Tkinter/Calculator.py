from tkinter import *

root = Tk()
root.configure(background="#696969")
root.title("Addition Calculator")

# Function for buttons
def button_click(number):
    existingval = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(existingval) + str(number))

def button_clear():
    entry.delete(0, END)

def button_plus():
    savedval = entry.get()
    global saved_val
    global math
    math = "addition"
    saved_val = int(savedval)
    entry.delete(0, END)

def button_equal():
    newval = entry.get()
    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, saved_val + int(newval))

    if math == "subtraction":
        entry.insert(0, saved_val - int(newval))

    if math == "multiplication":
        entry.insert(0, saved_val * int(newval))

    if math == "division":
        entry.insert(0, saved_val / int(newval))


def button_minus():
    savedval = entry.get()
    global saved_val
    global math
    math = "subtraction"
    saved_val = int(savedval)
    entry.delete(0, END)

def button_multiply():
    savedval = entry.get()
    global saved_val
    global math
    math = "multiplication"
    saved_val = int(savedval)
    entry.delete(0, END)

def button_divide():
    savedval = entry.get()
    global saved_val
    global math
    math = "division"
    saved_val = int(savedval)
    entry.delete(0, END)

# Entry field
entry = Entry(root, width=35, borderwidth=7, bg="#696969", fg="white")
# Inserting entry field
entry.grid(row=0, column=0, columnspan=3, ipady=10)

# Invisible "sticky" cells
myLabelS1 = Label(root, text="", bg="#696969")

#Inserting sticky cells
myLabelS1.grid(row=1, column=0)

#-----------------------------------------------------------------------------------------------------------------------

# Buttons
myButton1 = Button(root, text="1", font="sans 16 bold", command=lambda: button_click(1), bg="black", fg="white", padx=20, width=2)
myButton2 = Button(root, text="2", font="sans 16 bold", command=lambda: button_click(2), bg="black", fg="white", padx=20, width=2)
myButton3 = Button(root, text="3", font="sans 16 bold", command=lambda: button_click(3), bg="black", fg="white", padx=20, width=2)
myButton4 = Button(root, text="4", font="sans 16 bold", command=lambda: button_click(4), bg="black", fg="white", padx=20, width=2)
myButton5 = Button(root, text="5", font="sans 16 bold", command=lambda: button_click(5), bg="black", fg="white", padx=20, width=2)
myButton6 = Button(root, text="6", font="sans 16 bold", command=lambda: button_click(6), bg="black", fg="white", padx=20, width=2)
myButton7 = Button(root, text="7", font="sans 16 bold", command=lambda: button_click(7), bg="black", fg="white", padx=20, width=2)
myButton8 = Button(root, text="8", font="sans 16 bold", command=lambda: button_click(8), bg="black", fg="white", padx=20, width=2)
myButton9 = Button(root, text="9", font="sans 16 bold", command=lambda: button_click(9), bg="black", fg="white", padx=20, width=2)
myButton0 = Button(root, text="0", font="sans 16 bold", command=lambda: button_click(0), bg="black", fg="white", padx=20, width=2)
myButtonplus = Button(root, text="+", font="sans 16 bold", command=lambda: button_plus(), bg="#708090", fg="white", padx=20, width=2)
myButtonminus = Button(root, text="-", font="sans 16 bold", command=lambda: button_minus(), bg="#708090", fg="white", padx=20, width=2)
myButtonmultiply = Button(root, text="x", font="sans 16 bold", command=lambda: button_multiply(), bg="#708090", fg="white", padx=20, width=2)
myButtondivide = Button(root, text="/", font="sans 16 bold", command=lambda: button_divide(), bg="#708090", fg="white", padx=20, width=2)
myButtonequal = Button(root, text="=", font="sans 16 bold", command=lambda: button_equal(), bg="#2F4F4F", fg="white", padx=20, width=2)
myButtonclear = Button(root, width=14, text="Clear", font="sans 16 bold", command=lambda: button_clear(), bg="#708090", fg="white", padx=20)

# Placing buttons in grid
myButton1.grid(row=3, column=0)
myButton2.grid(row=3, column=1)
myButton3.grid(row=3, column=2)
myButton4.grid(row=4, column=0)
myButton5.grid(row=4, column=1)
myButton6.grid(row=4, column=2)
myButton7.grid(row=5, column=0)
myButton8.grid(row=5, column=1)
myButton9.grid(row=5, column=2)
myButton0.grid(row=6, column=0)
myButtonplus.grid(row=6, column=1)
myButtonminus.grid(row=6, column=2)
myButtonmultiply.grid(row=7, column=0)
myButtondivide.grid(row=7, column=1)
myButtonequal.grid(row=7, column=2)
myButtonclear.grid(row=8, column=0, columnspan=3)



root.mainloop()