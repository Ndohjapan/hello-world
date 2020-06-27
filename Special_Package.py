from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import winsound

window = Tk()
window.title("It's my world")
window.iconbitmap('a713230367b8496da62cfcde627d1f62.ico')

first_info = "Click next for more information"
lbl = Label(window, text="Email : ", font=("Arial Bold", 11), fg="navy blue")
lbl.grid(row=0, column=0)
lbl2 = Label(window, text=first_info, font=("Arial bold", 16))
lbl2.grid(row=1, column=1)
txt = Entry(window, font=("Times bold", 20), width=30, bg="light blue", bd=5)
txt.grid(row=0, column=1)
lbl3 = Label(window, text="                  ")
lbl3.grid(row=0, column=2)
#  txt.insert(0, "Email :")   # To insert default text into the entry widget
txt.focus()  # This is to allow the entry widget be focused automatically


# This is to collect the widget as one and display it wholly
# Use state function to disable the entry box


def cheat():
    messagebox.showwarning("Password check", "Don't Ever Mess with Ndoh Joel again\n"
                                             "#_My_money\n Cauz I've got all your passwords Facebook,IG etc.")
    for i in range(0, 7):
        for _ in range(0, 5):
            winsound.Beep(2000, 300)
            for _ in range(0, 5):
                winsound.Beep(2000, 300)
                for _ in range(0, 5):
                    winsound.Beep(2000, 300)


def clicked():
    e1 = txt.get()
    e2 = '@gmail.com' in e1
    if e2 is False:
        messagebox.showwarning('Warning', 'Invalid email')

    else:
        hacked = "Nwobi Joseph\nYou have been hacked\n Your email password is ***********"
        lbl.configure(text=hacked, font=("Arial bold italic", 16))
        lbl2.configure(text="Click Finish")
        btn.configure(text="Finish")
        btn.configure(command=cheat)
        txt.configure(state='disabled')
        frequency = 900
        duration = 5000
        winsound.Beep(frequency, duration)
        messagebox.showwarning('Designed for Nwobi Kaecy', "Don't Ever Mess With Me")


style = ttk.Style()
style.map("C.TButton",
          fg=[('pressed', 'red'), ('active', 'blue')],
          bg=[('pressed', '!disabled', 'black'), ('active', 'white')]
          )

btn = Button(window, text="  NEXT >>> ",
             pady=10, padx=50, command=clicked)
btn.grid(row=2, column=1)

window.mainloop()
