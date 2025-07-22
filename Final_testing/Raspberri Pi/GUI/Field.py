PASSWORD = 'MARS'

import tkinter as tk
from tkinter import messagebox
import pickle



Field_add_window=None
Main_Window = None

# Save the list of objects to a file


Titel="Field"
BG="lightgreen"

class Field:

    def __init__(self,n,r,c,crop):

        self.Name=n
        self.Row=r
        self.Com=c
        self.No_Plants=r*c

        self.Crop=crop
        self.dim=(0,0)
        print('Field Created')

    def __str__(self):
        return f"{self.crop} @ {self.Name}"
    
    def field():
        pass
            
    





def Save_Fields(F):
    with open('Final_testing\Raspberri Pi\GUI\Fields.pkl', 'wb') as f:
        pickle.dump(F, f)

# Load the list of objects from the file
def Load_Field():
    with open('Final_testing\Raspberri Pi\GUI\Fields.pkl', 'rb') as f:
       
        t = pickle.load(f)
        print('*****')   
        return t


Field_List = Load_Field()


#++++++++++++++++++++++Functional GUI+++++++++++++++++++++++++++


def Delete_Field(window):
    global Main_Window , Field_add_window
    Main_Window = window


    Field_add_window = tk.Toplevel(Main_Window,bg=BG)  # Create a new window
    Field_add_window.geometry("300x200")  # Set dimensions for the subwindow
    Field_add_window.title(Titel)

    # Add a button to the subwindow

    bottom_menu = tk.Frame(Field_add_window, bg=BG, height=10)
    bottom_menu.pack(side="bottom", fill="x")
    tk.Label(Field_add_window, text="Select Field", font=("Arial", 12), bg=BG, fg="darkblue").pack(pady=5, padx=10, anchor="w")

    options = [i.Name for i in Field_List]
    dropdown_var = tk.StringVar()
    dropdown_var.set(options[0])  # Set default value
    dropdown_menu = tk.OptionMenu(Field_add_window, dropdown_var, *options)
    dropdown_menu.pack(pady=5)


    tk.Button(Field_add_window, text="Delete Field",font=("Arial", 14), command=lambda:Del(dropdown_var.get())).pack(pady=10, padx=10)

    tk.Button(bottom_menu, text="Exit", font=("Arial", 14), command=lambda: Field_add_window.destroy()).pack(side="left", padx=20)
  

def Show_Field(window):
    global Main_Window , Field_add_window
    Main_Window = window


    Field_add_window = tk.Toplevel(Main_Window,bg=BG)  # Create a new window
    Field_add_window.geometry("300x200")  # Set dimensions for the subwindow
    Field_add_window.title(Titel)

    # Add a button to the subwindow

    bottom_menu = tk.Frame(Field_add_window, bg=BG, height=10)
    bottom_menu.pack(side="bottom", fill="x")
    tk.Label(Field_add_window, text="Select an Crop", font=("Arial", 12), bg=BG, fg="darkblue").pack(pady=5, padx=10, anchor="w")

    options = [i.Name for i in Field_List]
    dropdown_var = tk.StringVar()
    dropdown_var.set(options[0])  # Set default value
    dropdown_menu = tk.OptionMenu(Field_add_window, dropdown_var, *options)
    dropdown_menu.pack(pady=5)


    tk.Button(Field_add_window, text="Show Field",font=("Arial", 14), command=lambda:Show(dropdown_var.get())).pack(pady=10, padx=10)

    tk.Button(bottom_menu, text="Exit", font=("Arial", 14), command=lambda: Field_add_window.destroy()).pack(side="left", padx=20)
  

def Get_Field(window):

    global Main_Window , Field_add_window
    Main_Window = window

    Field_add_window = tk.Toplevel(Main_Window,bg=BG)  # Create a new window
    Field_add_window.geometry("300x500")  # Set dimensions for the subwindow
    Field_add_window.title(Titel)

    # Add a button to close the subwindow

    bottom_menu = tk.Frame(Field_add_window, bg=BG, height=10)
    bottom_menu.pack(side="bottom", fill="x")

    tk.Label(Field_add_window, text="Name:", font=("Arial", 12), bg=BG, fg="darkblue").pack(pady=5, padx=10, anchor="w")
    name_entry = tk.Entry(Field_add_window, font=("Arial", 14))
    name_entry.pack(pady=5, padx=10)

    tk.Label(Field_add_window, text="No.of.Rows", font=("Arial", 12), bg=BG, fg="darkblue").pack(pady=5, padx=10, anchor="w")
    row_entry = tk.Entry(Field_add_window, font=("Arial", 14))
    row_entry.pack(pady=5, padx=10)
    
    tk.Label(Field_add_window, text="No.of.Column", font=("Arial", 12), bg=BG, fg="darkblue").pack(pady=5, padx=10, anchor="w")
    cum_entry = tk.Entry(Field_add_window, font=("Arial", 14))
    cum_entry.pack(pady=5, padx=10)

    tk.Label(Field_add_window, text="Select an Crop", font=("Arial", 12), bg=BG, fg="darkblue").pack(pady=5, padx=10, anchor="w")

    options = ["Ground Nut", "Cron", "Wheat"]
    dropdown_var = tk.StringVar()
    dropdown_var.set(options[0])  # Set default value
    dropdown_menu = tk.OptionMenu(Field_add_window, dropdown_var, *options)
    dropdown_menu.pack(pady=5)


    tk.Button(Field_add_window, text="Add Field",font=("Arial", 14), command=lambda:add(name_entry.get(),row_entry.get(),cum_entry.get(),dropdown_var.get(),Field_add_window)).pack(pady=10, padx=10)
    tk.Button(bottom_menu, text="Exit", font=("Arial", 14), command=lambda: Field_add_window.destroy()).pack(side="left", padx=20)
  

def Field_Close(s,Field_add_window):
    Field_add_window.destroy()
    messagebox.showinfo("Info", s)
  

def add(n,r,c,crop,Field_add_window):
    try:

        obj = Field(n,int(r),int(c),crop)

        Field_List.append(obj)
        Save_Fields(Field_List)
        
        
        Field_Close("Field Added",Field_add_window)


    except:
        print("Error")
        Field_Close("Error",Field_add_window)

def Del(F):
    try:
        
        for i in Field_List:
            if i.Name == F:
                obj = i
                break
        n=3
        while not (n==0):
            pas = input("Enter Password to delete field: ")
            if pas == PASSWORD:
                Field_List.remove(obj)
                Save_Fields(Field_List)
                Field_Close("Field Deleted",Field_add_window)
            n-=1       
        
        Field_Close("Invalid Password",Field_add_window)


    except:
        print("Error")
        Field_Close("Error",Field_add_window)

def Show(F):
    try:
        
        for i in Field_List:
            if i.Name == F:
                obj = i
                break

        global Main_Window , Field_add_window

        sBG="pink"
        Sub_window = tk.Toplevel(Field_add_window,bg=sBG)  # Create a new window
        Sub_window.geometry("300x300")  # Set dimensions for the subwindow
        Sub_window.title("Field Show")

        # Add a button to close the subwindow

        bottom_menu = tk.Frame(Sub_window, bg=sBG, height=10)
        bottom_menu.pack(side="bottom", fill="x")

        tk.Label(Sub_window, text=f"Name: {obj.Name}", font=("Arial", 12), bg=sBG, fg="darkblue").pack(pady=5, padx=10, anchor="w")
        tk.Label(Sub_window, text=f"Dimention: {obj.Row}x{obj.Com}", font=("Arial", 12), bg=sBG, fg="darkblue").pack(pady=5, padx=10, anchor="w")
        tk.Label(Sub_window, text=f"No.of.Plants: {obj.No_Plants}", font=("Arial", 12), bg=sBG, fg="darkblue").pack(pady=5, padx=10, anchor="w")
        tk.Label(Sub_window, text=f"Crop Planted: {obj.Crop}", font=("Arial", 12), bg=sBG, fg="darkblue").pack(pady=5, padx=10, anchor="w")
        tk.Button(bottom_menu, text="Exit", font=("Arial", 14), command=lambda: Sub_window.destroy()).pack(side="left", padx=20)
  
    except:
        print("Error")
        Field_Close("Error",Field_add_window)
