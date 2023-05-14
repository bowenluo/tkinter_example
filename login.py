import tkinter as tk
import form
from tkinter import messagebox

root = tk.Tk()

def login():
    messagebox.showinfo("Successful Login",
                        "Welcome to use Accident Reporting System.")
    form.open_form_window()
    # root.withdraw()

def cancel():
    if messagebox.askyesno("Close Window?", "Do you want to close the window?"):
        root.quit()

def open_window():

    # Root window
    root.eval('tk::PlaceWindow . center')  # Center a window on the screen
    root.title("Accident Reporting System")

    tk.Label(root, text="Username").grid(row=0, sticky="w")
    tk.Entry(root).grid(row=0, column=1)

    tk.Label(root, text="Password").grid(row=1, sticky="w")
    tk.Entry(root, show="*").grid(row=1, column=1)

    tk.Button(root, text="Cancel", width=10, command=cancel).grid(
        row=2, column=0, sticky="w")
    tk.Button(root, text="Login", width=10, command=login).grid(
        row=2, column=1, sticky="e")

    root.mainloop()

