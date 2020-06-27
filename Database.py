from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import itertools

root = Tk()
root.title("Codemy.com")
root.iconbitmap("GRAPH.ICO")
root.geometry("400x400")


# Functions for adding updates
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # the connect function automatically creates a database in the directory we are working on

    # create the cursor
    c = conn.cursor()
    # This is the cursor which helps us make any change to the database

    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        WHERE oid  = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
                  
              }
    )

    # commit changes to the database file
    conn.commit()

    # Close Connection
    conn.close()
    editor.destroy()


def edit():
    try:
        global editor
        editor = Tk()
        editor.title("Update A Record")
        editor.iconbitmap("GRAPH.ICO")
        editor.geometry("400x200")

        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        # the connect function automatically creates a database in the directory we are working on

        # create the cursor
        c = conn.cursor()
        # This is the cursor which helps us make any change to the database

        record_id = delete_box.get()
        # Query the Database
        c.execute(f"SELECT * FROM addresses WHERE oid = {record_id}")
        records = c.fetchall()

        # Create the global for the entry variables
        global f_name_editor
        global l_name_editor
        global address_editor
        global city_editor
        global state_editor
        global zipcode_editor

        # Create Text Boxes
        f_name_editor=Entry(editor, width=30)
        f_name_editor.grid(row=0, column=1, padx=10, pady=(20, 0))
        f_name_editor.focus()

        l_name_editor = Entry(editor, width=30)
        l_name_editor.grid(row=1, column=1, padx=20)

        address_editor = Entry(editor, width=30)
        address_editor.grid(row=2, column=1, padx=20)

        city_editor = Entry(editor, width=30)
        city_editor.grid(row=3, column=1, padx=20)

        state_editor = Entry(editor, width=30)
        state_editor.grid(row=4, column=1, padx=20)

        zipcode_editor = Entry(editor, width=30)
        zipcode_editor.grid(row=5, column=1, padx=20)

        # Create list to store names of all entry boxes
        names_entry = [f_name_editor, l_name_editor, address_editor, city_editor, state_editor, zipcode_editor]

        # Create the labels
        f_name_label_editor = Label(editor, text="First Name")
        f_name_label_editor.grid(row=0, column=0, pady=(20, 0))

        l_name_label_editor = Label(editor, text="Last Name")
        l_name_label_editor.grid(row=1, column=0)

        address_label_editor = Label(editor, text="Address")
        address_label_editor.grid(row=2, column=0)

        city_label_editor = Label(editor, text="City")
        city_label_editor.grid(row=3, column=0)

        state_label_editor = Label(editor, text="State")
        state_label_editor.grid(row=4, column=0)

        zipcode_label_editor = Label(editor, text="Zip_code")
        zipcode_label_editor.grid(row=5, column=0)

        # Create Save button
        update_btn = Button(editor, text='Update Record', command=update)
        update_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=(20, 10), ipadx=137)



        # Loop through the results
        record = []
        for _ in records:
            record = _
        i = 0
        # Automatically display the data of record you want to edit
        for name in names_entry:
            name.insert(0, record[i])
            i += 1

        # commit changes to the database file
        conn.commit()

        # Close Connection
        conn.close()

    except sqlite3.OperationalError:
        editor.destroy()
        messagebox.showerror("Error", "Input ID for editing")


# Create function to delete record
def delete():
    try:
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        # the connect function automatically creates a database in the directory we are working on

        # create the cursor
        c = conn.cursor()
        # This is the cursor which helps us make any change to the database

        # Delete record
        c.execute(f"DELETE from addresses WHERE oid= {delete_box.get()}")

        # commit changes to the database file
        conn.commit()

        # Close Connection
        conn.close()
    except sqlite3.OperationalError:
        messagebox.showerror("Error", "No ID to delete")


def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # the connect function automatically creates a database in the directory we are working on

    # create the cursor
    c = conn.cursor()
    # This is the cursor which helps us make any change to the database

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name,:address, "
              ":city, :state, :zipcode )",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              }

              )

    # commit changes to the database file
    conn.commit()

    # Close Connection
    conn.close()

    # clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # To query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    print_records = " "
    for record in records:
        print_records += str(record) + "\n"
    win = Tk()
    win.title("Records")
    win.iconbitmap("GRAPH.ICO")
    win.geometry("400x200")
    query_label = Label(win, text=print_records)
    query_label.grid(row=11, column=0, columnspan=7)

    win.mainloop()
    conn.commit()
    conn.close()


'''
# Create a table in the
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer 
)
    """)
'''
# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=10, pady=(20, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(20, 0))
f_name.focus()

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zip_code")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0)

# Create Submit button
submit_btn = Button(root, text="Add To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, ipadx=100)

# Query button
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete button
delete_btn = Button(root, text='Delete Records', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create update button
edit_btn = Button(root, text='Edit Records', command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=(10, 0), ipadx=137)

root.mainloop()
