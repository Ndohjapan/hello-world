from tkinter import *

window = Tk()
window.title("Simple Calculator")
screen = Entry(window, width=25, bd=4, font=("Arial bold", 16))
screen.grid(row=0, column=0, columnspan=4, pady=10)


def button_subs():
    current = screen.get()
    global f_num
    global math
    math = 'difference'
    f_num = int(current)
    screen.delete(0, END)


def button_div():
    current = screen.get()
    global f_num
    global math
    math = 'division'
    f_num = int(current)
    screen.delete(0, END)


def button_prod():
    current = screen.get()
    global f_num
    global math
    math = 'product'
    f_num = int(current)
    screen.delete(0, END)


def button_clear():
    screen.delete(0, END)


def button_add():
    current = screen.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(current)
    screen.delete(0, END)


def button_click(number):
    current = str(screen.get()) + str(number)
    screen.delete(0, END)
    screen.insert(0, current)


def button_equal():
    current = screen.get()
    s_num = int(current)
    screen.delete(0, END)
    if math == 'addition':
        screen.insert(0, f_num + s_num)
    if math == 'difference':
        screen.insert(0, f_num - s_num)
    if math == 'product':
        screen.insert(0, f_num * s_num)
    if math == 'division':
        screen.insert(0, f_num / s_num)

# Define the buttons below

button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_sum = Button(window, text="+", padx=15, pady=0.15, command=button_add,
                    font=("Arial bold ", 25), bg='light blue')
button_clr = Button(window, text="CE", padx=21.5, pady=17, command=button_clear
                    , font=("Arial bold ", 11), bg='light blue')
button_eq = Button(window, text="=", padx=24, pady=0.0001, command=button_equal,
                   font=("Arial bold ", 25), bg='light blue')
button_diff = Button(window, text="-", padx=19, pady=0.1, command=button_subs,
                     font=("Arial bold ", 25), bg='light blue')
button_prod = Button(window, text="x", padx=17, pady=0.15, command=button_prod,
                     font=("Arial bold ", 25), bg='light blue')
button_div = Button(window, text="/", padx=30, pady=0.0001, command=button_div,
                    font=("Arial bold ", 25), bg='light blue')

# Display the buttons

button_sum.grid(row=2, column=3)
button_clr.grid(row=1, column=3)
button_eq.grid(row=4, column=1)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_diff.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_div.grid(row=4, column=2)
button_prod.grid(row=4, column=3)

window.mainloop()
