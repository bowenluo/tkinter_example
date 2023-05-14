import tkinter as tk
import login
import report
from tkinter import Menu
from tkcalendar import DateEntry
from tktimepicker import SpinTimePickerOld, SpinTimePickerModern
from tkinter import messagebox


def reset():
    print("Reset form")


def submit():
    messagebox.showinfo(None,"Submit form successfully")


def open_form_window():
    form = tk.Toplevel()

    # Create a menubar
    menubar = Menu(form)
    form.config(menu=menubar)

    # Create a menu
    file_menu = Menu(menubar, tearoff=False)

    # Add a menu item to the menu
    file_menu.add_command(label="Report", command=report.open_window)
    file_menu.add_command(label="Exit", command=login.cancel)
    menubar.add_cascade(label="File", menu=file_menu)

    tk.Label(form, text="First Name").grid(row=0, column=0, sticky="w")
    tk.Entry(form).grid(row=0, column=1, sticky="we")

    tk.Label(form, text="Last Name").grid(row=0, column=2, sticky="w")
    tk.Entry(form).grid(row=0, column=3, sticky="we")

    tk.Label(form, text="Date").grid(row=1, column=0, sticky="w")
    DateEntry(form).grid(row=1, column=1, columnspan=3, sticky="we")

    tk.Label(form, text="Time").grid(row=2, column=0, sticky="w")
    time_picker = SpinTimePickerOld(form)
    time_picker.addHours12()
    time_picker.addMinutes()
    time_picker.addPeriod()
    time_picker.grid(row=2, column=1, columnspan=3, sticky="we")

    tk.Label(form, text="Comment").grid(
        row=3, column=0, columnspan=4, sticky="w")
    tk.Text(form).grid(row=4, column=0, columnspan=4, sticky="nsew")

    tk.Button(form, text="Reset", width=10, command=reset).grid(
        row=5, column=0, columnspan=2, sticky="nsew")
    tk.Button(form, text="Submit", width=10, command=submit).grid(
        row=5, column=2, columnspan=2, sticky="nsew")
