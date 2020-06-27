import tkinter
from tkinter import *
from time import sleep
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import Menu
from GUI_Cookbook import ToolTip
from threading import Thread
from queue import Queue
import GUI_Cookbook.Queue as bq
from tkinter import messagebox
from tkinter import filedialog as fd
from os import path

class OOP():
    # ================================================
    # ===============Creating Queues==================
    # ================================================
    def use_queue(self):
        while True:
            print(self.gui_queue.get())  # To get the contents of a queue

    # =================================================
    # ==============All About Thread===================
    # =================================================

    def method_in_a_thread(self, num_of_loop=10):
        for idx in range(num_of_loop):
            sleep(1)
            self.scr.insert(tkinter.INSERT, str(idx) + '\n')
        sleep(1)
        print('method_in_a_thread(): ', self.run_thread.isAlive())

    def create_thread(self):
        self.run_thread = Thread(target=oop.method_in_a_thread)
        self.run_thread.setDaemon(True)  # This will close the thread as soon as the GUI is closed
        self.run_thread.start()
        print(self.run_thread)

    # ------------Create The Thread---------------
        write_thread = Thread(target=self.use_queue(), deamon=True)
        write_thread.start()

    # ============================================
    # ============Global Variables================
    # ============================================
    def __init__(self):
        self.window = Tk()
        self.window.title("Nyptopool")
        self.window.iconbitmap("C:/Users/USER/PycharmProjects/First/GRAPH.ICO")
        # window.geometry("300x320")
        self.window.resizable(False, False)
        self.create_widgets()
        # create a Queue
        self.gui_queue = Queue()

    # =====================================
    # ===========Call Back Function========
    # =====================================
    def _spin(self):
        value = self.spin.get()
        # print(value)

        self.scr.insert(INSERT, value + '\n')
        print(self)

        # Passing in the current class instance(self)
        bq.write_to_scrol(self)
        # self.use_queue()
    # ======================================
    # ============Tabs In Window============
    # ======================================
    def create_widgets(self):
        tabControl = Notebook(self.window)  # Create a Tab Control

        tab1 = Frame(tabControl)  # Create a tab on the control tab
        tabControl.add(tab1, text="Tab 1")  # Add the tab

        tab2 = Frame(tabControl)
        tabControl.add(tab2, text="Tab 2")  # Add a second tab

        tab3 = Frame(tabControl)
        tabControl.add(tab3, text="Tab 3")  # Add a third tab

        tab4 = Frame(tabControl)
        tabControl.add(tab4, text="Tab 4")

        tabControl.pack(expand=1, fill="both")  # Pack to screen to make visible

        # ========================================
        # ============Frame in Window=============
        # ========================================

        mighty = LabelFrame(tab1, text="Mighty Python")
        mighty.grid(row=0, column=0, padx=8, pady=4)

        tab2_frame = LabelFrame(tab2, text="The Snake")
        tab2_frame.grid(column=0, row=0, padx=8, pady=4, sticky="WE")

        tab3_frame = tkinter.Frame(tab3, bg="blue")
        tab3_frame.pack()

        for orange_color in range(2):
            canvas = Canvas(tab3_frame, width=150, height=114,
                            highlightthickness=0, bg='orange')
            canvas.grid(row=orange_color, column=orange_color)

        mngFileFrame = LabelFrame(tab4, text="Manage Files: ")
        mngFileFrame.grid(column=0, row=1, sticky="WE", padx=10, pady=5)

        # ===========================================
        # ===========Add Widgets to Tab4=============
        # ===========================================

        def getFileName():
            print("Hello from getFileName")
            fDir = path.dirname("p")
            fName = fd.askopenfilenames(parent=self.window, initialdir=fDir)

        lb = Button(mngFileFrame, text="Browse to File.....", command=getFileName)
        lb.grid(column=0, row=0, sticky=W)

        file = StringVar()
        self.entryLen= 40
        self.fileEntry = Entry(mngFileFrame, width=self.entryLen, textvariable=file)
        self.fileEntry.grid(column=1, row=0, sticky=W)

        logDir = StringVar()
        self.netwEntry = Entry(mngFileFrame, width=self.entryLen, textvariable=logDir)
        self.netwEntry.grid(column=1, row=1, sticky=W)

        def copyFile():
            import shutil
            src = self.fileEntry.get()
            file = src.split('/')[-1]
            dst = self.netwEntry.get() + ''+ file
            try:
                shutil.copy(src, dst)
                messagebox.showinfo('Copy File to Network', 'Success: File copied')
            except FileNotFoundError as err:
                messagebox.showerror('Copy File to Network', '*** Failed to copy file! ***\n\n' + str(err))
            except Exception as ex:
                messagebox.showerror("Copy File to Network", "*** Failed to copy file! ***\n\n" + str(ex))

        cb = Button(mngFileFrame, text="Copy File To : ", command=copyFile)
        cb.grid(column=0, row=1, sticky=E)

        for child in mngFileFrame.winfo_children():
            child.grid_configure(padx=6,pady=6)

        # ======================================
        # ============Combo_Box=================
        # ======================================

        choose = Combobox(mighty, state="readonly", width=10)
        choose['values'] = [i for i in "1234566789"]
        choose.current(0)
        choose.grid(row=0, column=0, sticky=W)

        # =================================
        # =========Check_Boxes=============
        # =================================

        name = BooleanVar()
        name.set(True)
        check1 = Checkbutton(tab2_frame, text="Disabled", state='disable', variable=name)
        check1.grid(row=0, column=0, sticky=W, padx=15)

        ck2 = IntVar()
        check2 = Checkbutton(tab2_frame, text="Undo", variable=ck2)
        check2.grid(row=0, column=1, sticky=W, padx=15)

        ck3 = BooleanVar()
        ck3.set(True)
        check3 = Checkbutton(tab2_frame, text="Redo", variable=ck3)
        check3.grid(row=0, column=2, sticky=W, padx=15)

        # ===========================================
        # ===============Radio_Button================
        # ===========================================

        colors = {"1": "Brown", "2": "Gold", "3": "White"}

        def radCall():
            self.window.configure(bg=colors[str(self.radVar.get())])
            print("1")
            """colors[str(self.radVar.get())]"""

        self.radVar = IntVar()
        for i in colors.keys():
            self.rad = Radiobutton(tab2_frame, text=colors[i], variable=self.radVar, value=int(i),
                                   command=radCall)
            self.rad.grid(row=1, column=int(i) - 1, sticky="WE", padx=15)

        # ===============================================
        # ================Scroll_Bar=====================
        # ===============================================

        scr_w = 40
        scr_h = 10
        self.scr = scrolledtext.ScrolledText(mighty, width=scr_w, height=scr_h, wrap=WORD)
        self.scr.grid(row=2, column=0, sticky='WE', columnspan=3)
        self.scr.focus()
        ToolTip.ToolTip(self.scr, "This is a ScrolledText control")
        # ===============================================
        # =============Labels_In_Frames==================
        # ===============================================

        button_frames = LabelFrame(tab2_frame, text="ProgressBar")
        button_frames.grid(row=3, column=0, sticky="W", columnspan=2)

        # ===================================================
        # ===============Spacing in Tkinter==================
        # ===================================================

        for child in button_frames.winfo_children():
            child.grid_configure(padx=8, pady=4)

        # ===================================================
        # ====================Menu Bar=======================
        # ===================================================

        menu_tile = Menu(self.window)
        self.window.configure(menu=menu_tile)

        def _quit():
            self.window.destroy()
            # window.quit()
            # exit()

        file_menu = Menu(menu_tile, tearoff=0)
        """ Creating a menu bar in the menu tile
                Tearoff is used to remove the first breaking lines"""
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=_quit)

        help_menu = Menu(menu_tile, tearoff=0)
        help_menu.add_command(label="About")

        menu_tile.add_cascade(label="File", menu=file_menu)
        menu_tile.add_cascade(label="Help", menu=help_menu)

        # This is adding the file menu on the menu tile

        # ===============================================
        # =================Spin Box======================
        # ===============================================

        default = IntVar()
        default.set(5)
        self.spin = tkinter.Spinbox(mighty, from_=0, to=10, width=5,command=self._spin,
                                    textvariable=default, bd=9, relief=SUNKEN)
        self.spin.grid(row=1, column=0, sticky="W")

        # ================================================
        # =================Progress Bar===================
        # ================================================

        self.progress_bar = Progressbar(tab2, orient='horizontal', length=286, mode="determinate")
        self.progress_bar.grid(column=0, row=3, padx=2, pady=2)

        def run_progressbar():
            self.progress_bar["maximum"] = 100
            for i in range(101):
                sleep(0.05)
                self.progress_bar["value"] = i
                self.progress_bar.update()
            self.progress_bar["value"] = 0

        def start_progressbar():
            self.progress_bar.start()

        def stop_progressbar():
            self.progress_bar.stop()

        def progress_stop_after(wait_ms=1000):
            self.window.after(wait_ms, self.progress_bar.start())

        # ===========================================
        # ==========Buttons In Label Frame===========
        # ===========================================
        button_names = {"Run Progressbar": run_progressbar,
                        "Start Progressbar": start_progressbar,
                        "Stop Progressbar": stop_progressbar,
                        "Stop After Second": progress_stop_after}
        i = 0
        for disp, funct in button_names.items():
            Button(button_frames, text=disp, command=funct).grid(column=0, row=i, padx=2, pady=2)
            i += 1

        for child in tab2.winfo_children():
            child.grid_configure(padx=8, pady=2)


oop = OOP()
# run_thread = Thread(target=oop.method_in_a_thread)  # creating a thread
# print(run_thread)
oop.window.mainloop()
