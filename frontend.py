"""
A program that creates a Desktop Application widget
that stores contact information inside database
"""
import tkinter as tk
from backend import Database

database = Database("contacts.db")


class Window:
    """Window class that creates the PhoneBook Widget, formats the display
    and calls the instance methods when buttons are clicked
    """

    def __init__(self, window):
        """Initializer / Instance Attributes"""

        self.window = window
        self.window.wm_title("PhoneBook Widget")

        first = tk.Label(window, text="First")
        first.grid(row=0, column=0)

        last = tk.Label(window, text="Last")
        last.grid(row=0, column=2)

        cell = tk.Label(window, text="Cell")
        cell.grid(row=1, column=0)

        email = tk.Label(window, text="Email")
        email.grid(row=1, column=2)

        self.first_text = tk.StringVar()
        self.first_entry = tk.Entry(window, textvariable=self.first_text)
        self.first_entry.grid(row=0, column=1)

        self.last_text = tk.StringVar()
        self.last_entry = tk.Entry(window, textvariable=self.last_text)
        self.last_entry.grid(row=0, column=3)

        self.cell_text = tk.StringVar()
        self.cell_entry = tk.Entry(window, textvariable=self.cell_text)
        self.cell_entry.grid(row=1, column=1)

        self.email_text = tk.StringVar()
        self.email_entry = tk.Entry(window, textvariable=self.email_text)
        self.email_entry.grid(row=1, column=3)

        self.list_box = tk.Listbox(window, height=6, width=40)
        self.list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

        scroll = tk.Scrollbar(window)
        scroll.grid(row=2, column=2, rowspan=10)

        self.list_box.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.list_box.yview)

        self.list_box.bind('<<ListboxSelect>>', self.get_selected_row)

        view_button = tk.Button(window,
                                text="View all",
                                width=12,
                                comman=self.view_command)

        view_button.grid(row=2, column=3)

        search_button = tk.Button(window,
                                  text="Search",
                                  width=12,
                                  command=self.search_command)
        search_button.grid(row=3, column=3)

        add_button = tk.Button(window,
                               text="Add",
                               width=12,
                               command=self.add_command)

        add_button.grid(row=4, column=3)

        update_button = tk.Button(window,
                                  text="Update",
                                  width=12,
                                  command=self.update_command)
        update_button.grid(row=5, column=3)

        delete_button = tk.Button(window,
                                  text="Delete",
                                  width=12,
                                  command=self.delete_command)
        delete_button.grid(row=6, column=3)

        close_button = tk.Button(window,
                                 text="Close",
                                 width=12,
                                 command=window.destroy)
        close_button.grid(row=7, column=3)

    def view_command(self):
        self.list_box.delete(0, tk.END)
        for row in database.view():
            self.list_box.insert(tk.END, row)

    def search_command(self):
        self.list_box.delete(0, tk.END)
        for row in database.search(self.first_text.get(),
                                   self.last_text.get(),
                                   self.cell_text.get(),
                                   self.email_text.get()):
            self.list_box.insert(tk.END, row)

    def add_command(self):
        database.insert(self.first_text.get(),
                        self.last_text.get(),
                        self.cell_text.get(),
                        self.email_text.get())
        self.list_box.delete(0, tk.END)
        self.list_box.insert(tk.END, (self.first_text.get(),
                                      self.last_text.get(),
                                      self.cell_text.get(),
                                      self.email_text.get()))

    def update_command(self):
        database.update(self.selected_row[0],
                        self.first_text.get(),
                        self.last_text.get(),
                        self.cell_text.get(),
                        self.email_text.get())

    def delete_command(self):
        database.delete(self.selected_row[0])

    def get_selected_row(self, event):
        """Get list of items from FIRST to LAST and prints seleted row"""
        try:
            index = self.list_box.curselection()[0]
            self.selected_row = self.list_box.get(index)
            self.first_entry.delete(0, tk.END)
            self.first_entry.insert(tk.END, self.selected_row[1])
            self.last_entry.delete(0, tk.END)
            self.last_entry.insert(tk.END, self.selected_row[2])
            self.cell_entry.delete(0, tk.END)
            self.cell_entry.insert(tk.END, self.selected_row[3])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, self.selected_row[4])
        except IndexError:
            pass


window = tk.Tk()
Window(window)
window.mainloop()
