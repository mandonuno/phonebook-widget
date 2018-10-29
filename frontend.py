"""
A program that stores contact information:
"""
from tkinter import *
from backend import Database

database = Database("contacts.db")

"""FUNCTIONS"""
def view_command():
    list_box.delete(0,END)
    for row in database.view():
        list_box.insert(END,row)

def search_command():
    list_box.delete(0,END)
    for row in database.search(first_text.get(), last_text.get(), cell_text.get(), email_text.get()):
        list_box.insert(END,row)

def add_command():
    database.insert(first_text.get(), last_text.get(), cell_text.get(), email_text.get())
    list_box.delete(0,END)
    list_box.insert(END,(first_text.get(), last_text.get(), cell_text.get(), email_text.get()))

def update_command():
    database.update(selected_row[0],first_text.get(), last_text.get(), cell_text.get(), email_text.get())


def delete_command():
    database.delete(selected_row[0])

def get_selected_row(event):
    """Get list of items from FIRST to LAST and prints seleted row"""
    try:
        global selected_row 
        index = list_box.curselection()[0]
        selected_row = list_box.get(index)
        first_entry.delete(0,END)
        first_entry.insert(END,selected_row[1])
        last_entry.delete(0,END)
        last_entry.insert(END,selected_row[2])
        cell_entry.delete(0,END)
        cell_entry.insert(END,selected_row[3])
        email_entry.delete(0,END)
        email_entry.insert(END,selected_row[4])
    except IndexError:
        pass

window = Tk()

window.wm_title("PhoneBook Widget")

first = Label(window, text = "First")
first.grid(row=0, column=0)

last = Label(window, text = "Last")
last.grid(row=0, column=2)

cell = Label(window, text = "Cell")
cell.grid(row=1, column=0)

email = Label(window, text = "Email")
email.grid(row=1, column=2)

first_text = StringVar()
first_entry = Entry(window, textvariable=first_text)
first_entry.grid(row=0, column=1)

last_text = StringVar()
last_entry = Entry(window, textvariable=last_text)
last_entry.grid(row=0, column=3)

cell_text = StringVar()
cell_entry = Entry(window, textvariable=cell_text)
cell_entry.grid(row=1, column=1)

email_text = StringVar()
email_entry = Entry(window, textvariable=email_text)
email_entry.grid(row=1, column=3)

list_box = Listbox(window, height=6, width=30)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=10)

list_box.configure(yscrollcommand=scroll.set)
scroll.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>', get_selected_row)

view_button = Button(window, text="View all", width=12, comman=view_command)
view_button.grid(row=2, column=3)

search_button = Button(window, text="Search", width=12, command=search_command)
search_button.grid(row=3, column=3)

add_button = Button(window, text="Add", width=12, command=add_command)
add_button.grid(row=4, column=3)

update_button = Button(window, text="Update", width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)

window.mainloop()
