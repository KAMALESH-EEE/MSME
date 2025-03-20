import tkinter as tk
from tkinter import messagebox


Titel="Field"
BG="lightgreen"



def open_subwindow(window):
    Field_window = tk.Toplevel(window,bg=BG)  # Create a new window
    Field_window.geometry("300x200")  # Set dimensions for the subwindow
    Field_window.title(Titel)

    # Add a button to close the subwindow

    bottom_menu = tk.Frame(Field_window, bg=BG, height=10)
    bottom_menu.pack(side="bottom", fill="x")

    return Field_window


def Get_Field(window):



    Field_window=open_subwindow(window)

    tk.Label(Field_window, text="Name:", font=("Arial", 12), bg=BG, fg="white").pack(pady=5, padx=10, anchor="w")
    name_entry = tk.Entry(Field_window, font=("Arial", 14))
    name_entry.pack(pady=5, padx=10)

    tk.Label(Field_window, text="No.of.Rows", font=("Arial", 12), bg=BG, fg="white").pack(pady=5, padx=10, anchor="w")
    row_entry = tk.Entry(Field_window, font=("Arial", 14))
    row_entry.pack(pady=5, padx=10)
    
    tk.Label(Field_window, text="No.of.Column", font=("Arial", 12), bg=BG, fg="white").pack(pady=5, padx=10, anchor="w")
    cum_entry = tk.Entry(Field_window, font=("Arial", 14))
    cum_entry.pack(pady=5, padx=10)

    tk.Button(Field_window, text="Add Field",font=("Arial", 14), command=lambda:add(name_entry,row_entry,cum_entry,Field_window)).pack(pady=10, padx=10)
        
    

   

def Field_Close(s,Field_window):
    Field_window.quit()
    
    

def add(name_entry,row_entry,cum_entry,Field_window):
    try:
        n = name_entry.get() 

        r = int(row_entry.get())

        c = int(cum_entry.get())

        print(n,r,c)
        Field_Close("Field Added",Field_window)

    except:
        Field_Close("Error",Field_window)