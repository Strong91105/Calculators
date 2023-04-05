from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from math import *

# Frame1: Home
# Frame2: Linear
# Frame3: Quadratic




# Setting which frame to show first
def show_frame(frame):
    frame.tkraise()


root = Tk()
root.title("Graphing Calculator")
#root.state("zoomed")

functions = [
    "Linear",
    "Quadratic",
    "Cubic",
    "Sin"
]
selected_function = StringVar()
selected_function.set(functions[0])

def f_select():
        user_function = selected_function.get()
        if user_function == "Linear":
            show_frame(frame2)

        if user_function == "Quadratic":
            show_frame(frame3)

        if user_function == "Cubic":
            show_frame(frame4)

        if user_function == "Sin":
            show_frame(frame5)

def return_home():
        show_frame(frame1)




# Frame 1 (Home Screen)
frame1 = Frame(root)


frame1_title = Label(frame1, text="Graphing Calculator", font="Sans 16 bold")
frame1_label = Label(frame1, text="Type of function: ", font="Sans 10 bold")
frame1_drop = OptionMenu(frame1, selected_function, *functions)
frame1_button = Button(frame1, text="Select", command=f_select)
frame1_dummy = Label(frame1, text="", font="Sans 30 bold")



frame1_title.grid(row=0, column=0, columnspan=3)
frame1_label.grid(row=1, column=0)
frame1_drop.grid(row=1, column=1)
frame1_button.grid(row=2, column=1)
frame1_dummy.grid(row=3, column=0)




# Frame 2 (Linear)
frame2 = Frame(root)


def solve_linear():
    m_val = frame2_entry_m.get()
    global m
    m = float(m_val)
    c_val = frame2_entry_c.get()
    global c
    c = float(c_val)

    print("Selected function: ", selected_function.get())
    print("m = ", m)
    print("c = ",c)


    # Linear operation
    def linear(x, m, c):
        return m*x+c

    global linear_xlist
    linear_xlist = np.linspace(-10, 10, num=1000)  # np.linspace makes a list of evenly spaced values from -10 to 10 with 1000 datapoints

    global linear_ylist
    linear_ylist = linear(linear_xlist, m, c)

    linear_x_intercept = (0-c)/m
    lin_xint = ("x-intercept = ", linear_x_intercept)
    linear_xint_label = Label(frame2, text=lin_xint)
    linear_xint_label.grid(row=5, column=0)


    # Embedding pyplot chart (linear)
    linear_fig = plt.Figure(figsize=(5, 5), dpi=120)
    linear_fig.add_subplot(111).plot(linear_xlist, linear_ylist)
    linear_ax = linear_fig.gca()
    linear_ax.spines['left'].set_position('center')
    linear_ax.spines['bottom'].set_position('zero')
    linear_ax.spines['right'].set_color('none')
    linear_ax.spines['top'].set_color('none')
    linear_ax.xaxis.set_ticks_position('bottom')
    linear_ax.yaxis.set_ticks_position('left')
    canvas_linear = FigureCanvasTkAgg(linear_fig, frame2)
    canvas_linear.get_tk_widget().grid(row=1, column=2)






frame2_title = Label(frame2, text="Linear equations", font="Sans 16 bold")
frame2_equation = Label(frame2, text="y = mx + c", font="Sans 14 bold")
frame2_instruction = Label(frame2, text="Enter values for m and c", font="Sans 10 bold")
frame2_label_m = Label(frame2, text="m: ")
frame2_entry_m = Entry(frame2, width=10, borderwidth=1)
frame2_label_c = Label(frame2, text="c: ")
frame2_entry_c = Entry(frame2, width=10, borderwidth=1)
frame2_solve = Button(frame2, text="Solve", command=solve_linear)
frame2_exit = Button(frame2, text="Return to home", command=return_home)

frame2_title.grid(row=0, column=0)
frame2_equation.grid(row=1, column=0)
frame2_instruction.grid(row=2, column=0)
frame2_label_m.grid(row=3, column=0)
frame2_entry_m.grid(row=3, column=1)
frame2_label_c.grid(row=4, column=0)
frame2_entry_c.grid(row=4, column=1)
frame2_solve.grid(row=6, column=0)
frame2_exit.grid(row=7, column=0)






# Frame 3 (Quadratic)
frame3 = Frame(root)


def solve_quadratic():
    a_val = frame3_entry_a.get()
    global a
    a = float(a_val)
    b_val = frame3_entry_b.get()
    global b
    b = float(b_val)
    c_val = frame3_entry_c.get()
    global c
    c = float(c_val)

    print("Selected function: ", selected_function.get())
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)

    # Quadratic operation
    def quadratic(x, a, b, c):
        return (a*x)**2 + (b*x) + c


    global quadratic_xlist
    quadratic_xlist = np.linspace(-10, 10, num=1000)  # np.linspace makes a list of evenly spaced values from -10 to 10 with 1000 datapoints

    global quadratic_ylist
    quadratic_ylist = quadratic(quadratic_xlist, a, b, c)

    x_and_y_list = list(zip(quadratic_xlist, quadratic_ylist))
    print(x_and_y_list)

    # Roots of the quadratic
    ans_x1 = (-b) + np.sqrt((b * b - 4 * a * c)+0j) / (2 * a)
    result_x1 = "Root 1: x = ", ans_x1
    ans_x2 = (-b) - np.sqrt((b * b - 4 * a * c)+0j) / (2 * a)
    result_x2 = "Root 2: x = ", ans_x2

    quad_root_x1 = Label(frame3, text=result_x1)
    quad_root_x2 = Label(frame3, text=result_x2)

    quad_root_x1.grid(row=3, column=2)
    quad_root_x2.grid(row=4, column=2)

    # Embedding pyplot chart (quadratic)
    quadratic_fig = plt.Figure(figsize=(5, 5), dpi=120)
    quadratic_fig.add_subplot(111).plot(quadratic_xlist, quadratic_ylist)
    quad_ax = quadratic_fig.gca()
    quad_ax.spines['left'].set_position('center')
    quad_ax.spines['bottom'].set_position('zero')
    quad_ax.spines['right'].set_color('none')
    quad_ax.spines['top'].set_color('none')
    quad_ax.xaxis.set_ticks_position('bottom')
    quad_ax.yaxis.set_ticks_position('left')
    canvas_quadratic = FigureCanvasTkAgg(quadratic_fig, frame3)
    canvas_quadratic.get_tk_widget().grid(row=1, column=2)

frame3_title = Label(frame3, text="Quadratic equations", font="Sans 16 bold")
frame3_equation = Label(frame3, text="y = ax^2 + bx + c", font="Sans 14 bold")
frame3_instruction = Label(frame3, text="Enter values for a, b and c", font="Sans 10 bold")
frame3_label_a = Label(frame3, text="a: ")
frame3_entry_a = Entry(frame3, width=10, borderwidth=1)
frame3_label_b = Label(frame3, text="b: ")
frame3_entry_b = Entry(frame3, width=10, borderwidth=1)
frame3_label_c = Label(frame3, text="c: ")
frame3_entry_c = Entry(frame3, width=10, borderwidth=1)
frame3_solve = Button(frame3, text="Solve", command=solve_quadratic)
frame3_exit = Button(frame3, text="Return to home", command=return_home)

frame3_title.grid(row=0, column=0)
frame3_equation.grid(row=1, column=0)
frame3_instruction.grid(row=2, column=0)
frame3_label_a.grid(row=3, column=0)
frame3_entry_a.grid(row=3, column=1)
frame3_label_b.grid(row=4, column=0)
frame3_entry_b.grid(row=4, column=1)
frame3_label_c.grid(row=5, column=0)
frame3_entry_c.grid(row=5, column=1)
frame3_solve.grid(row=6, column=0)
frame3_exit.grid(row=7, column=0)




# Frame 4 (cubic)
frame4 = Frame(root)



def solve_cubic():
    a_val = frame4_entry_a.get()
    global a
    a = float(a_val)
    b_val = frame4_entry_b.get()
    global b
    b = float(b_val)
    c_val = frame4_entry_c.get()
    global c
    c = float(c_val)
    d_val = frame4_entry_d.get()
    global d
    d = float(d_val)

    print("Selected function: ", selected_function.get())
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("d = ", d)

    # Cubic operation
    def cubic(x, a, b, c, d):
        return a*x**3 + b*x**2 + c*x + d

    global cubic_xlist
    cubic_xlist = np.linspace(-10, 10, num=1000)  # np.linspace makes a list of evenly spaced values from -10 to 10 with 1000 datapoints

    global cubic_ylist
    cubic_ylist = cubic(cubic_xlist, a, b, c, d)

    # Roots of the cubic
    cubic_roots = np.roots([a, b, c, d])

    result_x1 = "Root 1: x = ", cubic_roots[0]
    result_x2 = "Root 2: x = ", cubic_roots[1]
    result_x3 = "Root 3: x = ", cubic_roots[2]

    cubic_x1 = Label(frame4, text=result_x1)
    cubic_x2 = Label(frame4, text=result_x2)
    cubic_x3 = Label(frame4, text=result_x3)


    cubic_x1.grid(row=3, column=2)
    cubic_x2.grid(row=4, column=2)
    cubic_x3.grid(row=5, column=2)

    # Embedding pyplot chart (cubic)
    cubic_fig = plt.Figure(figsize=(5, 5), dpi=120)
    cubic_fig.add_subplot(111).plot(cubic_xlist, cubic_ylist)
    cubic_ax = cubic_fig.gca()
    cubic_ax.spines['left'].set_position('center')
    cubic_ax.spines['bottom'].set_position('zero')
    cubic_ax.spines['right'].set_color('none')
    cubic_ax.spines['top'].set_color('none')
    cubic_ax.xaxis.set_ticks_position('bottom')
    cubic_ax.yaxis.set_ticks_position('left')
    canvas_cubic = FigureCanvasTkAgg(cubic_fig, frame4)
    canvas_cubic.get_tk_widget().grid(row=1, column=2)

frame4_title = Label(frame4, text="Cubic equations", font="Sans 16 bold")
frame4_equation = Label(frame4, text="y = ax^3 + bx^2 + cx + d", font="Sans 14 bold")
frame4_instruction = Label(frame4, text="Enter values for a, b, c and d", font="Sans 10 bold")
frame4_label_a = Label(frame4, text="a: ")
frame4_entry_a = Entry(frame4, width=10, borderwidth=1)
frame4_label_b = Label(frame4, text="b: ")
frame4_entry_b = Entry(frame4, width=10, borderwidth=1)
frame4_label_c = Label(frame4, text="c: ")
frame4_entry_c = Entry(frame4, width=10, borderwidth=1)
frame4_label_d = Label(frame4, text="d: ")
frame4_entry_d = Entry(frame4, width=10, borderwidth=1)
frame4_solve = Button(frame4, text="Solve", command=solve_cubic)
frame4_exit = Button(frame4, text="Return to home", command=return_home)

frame4_title.grid(row=0, column=0)
frame4_equation.grid(row=1, column=0)
frame4_instruction.grid(row=2, column=0)
frame4_label_a.grid(row=3, column=0)
frame4_entry_a.grid(row=3, column=1)
frame4_label_b.grid(row=4, column=0)
frame4_entry_b.grid(row=4, column=1)
frame4_label_c.grid(row=5, column=0)
frame4_entry_c.grid(row=5, column=1)
frame4_label_d.grid(row=6, column=0)
frame4_entry_d.grid(row=6, column=1)
frame4_solve.grid(row=7, column=0)
frame4_exit.grid(row=8, column=0)



# Frame 5 (sin)
frame5 = Frame(root)






for frame in (frame1, frame2, frame3, frame4, frame5):
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


show_frame(frame1)


root.mainloop()