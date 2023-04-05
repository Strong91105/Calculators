from tkinter import *
from math import *

root = Tk()
root.title("Quadratic Solver")

label_x1 = Label(root, text="x1: ", font="Sans 16 bold")
label_x1.grid(row=5, column=0)

output_x1 = Entry(root, width=25, borderwidth=5)
output_x1.grid(row=5, column=1)

label_x2 = Label(root, text="x2: ", font="Sans 16 bold")
label_x2.grid(row=6, column=0)

output_x2 = Entry(root, width=25, borderwidth=5)
output_x2.grid(row=6, column=1)

equation_label = Label(root, text="y = ax^2 + bx + c", font="Sans 16 bold")
equation_label.grid(row=7, column=1)

# Functions for buttons
def press_solve():
    a_val = float(input_a.get())
    a = float(a_val)

    b_val = float(input_b.get())
    b = float(b_val)

    c_val = float(input_c.get())
    c = float(c_val)

    ans_x1 = (-b) + sqrt((b*b-4*a*c)) / (2*a)
    result_x1 = str(ans_x1)
    print("x_1 = " + result_x1)
    output_x1.insert(0, ans_x1)

    ans_x2 = (-b) - sqrt((b * b - 4 * a * c)) / (2 * a)
    result_x2 = str(ans_x2)
    print("x_2 = " + result_x2)
    output_x2.insert(0, ans_x2)


# Placing labels and input fields on screen
label_title = Label(root, text="Quadratic Solver", font="Sans 30 bold")
label_title.grid(row=0, column=0, columnspan=5)

label_a = Label(root, text="a: ", font="Sans 16 bold")
label_a.grid(row=1, column=0)

input_a = Entry(root, width=25, borderwidth=5)
input_a.insert(0, "1")
input_a.grid(row=1, column=1)

label_b = Label(root, text="b: ", font="Sans 16 bold")
label_b.grid(row=2, column=0)

input_b = Entry(root, width=25, borderwidth=5)
input_b.insert(0, "100")
input_b.grid(row=2, column=1)

label_c = Label(root, text="c: ", font="Sans 16 bold")
label_c.grid(row=3, column=0)

input_c = Entry(root, width=25, borderwidth=5)
input_c.insert(0, "1")
input_c.grid(row=3, column=1)

button_solve = Button(root, text="Solve", command=press_solve)
button_solve.grid(row=4, column=1)





root.mainloop()

