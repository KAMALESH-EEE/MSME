import tkinter as tk
from tkinter import messagebox
import pickle



Field_window=None
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
        return pickle.load(f)

Field_List = Load_Field()








def Get_Field(window):

    global Main_Window , Field_window
    Main_Window = window

    Field_window = tk.Toplevel(Main_Window,bg=BG)  # Create a new window
    Field_window.geometry("300x500")  # Set dimensions for the subwindow
    Field_window.title(Titel)

    # Add a button to close the subwindow

    bottom_menu = tk.Frame(Field_window, bg=BG, height=10)
    bottom_menu.pack(side="bottom", fill="x")

    tk.Label(Field_window, text="Name:", font=("Arial", 12), bg=BG, fg="darkblue").pack(pady=5, padx=10, anchor="w")
    name_entry = tk.Entry(Field_window, font=("Arial", 14))
    name_entry.pack(pady=5, padx=10)

    tk.Label(Field_window, text="No.of.Rows", font=("Arial", 12), bg=BG, fg="darkblue").pack(pady=5, padx=10, anchor="w")
    row_entry = tk.Entry(Field_window, font=("Arial", 14))
    row_entry.pack(pady=5, padx=10)
    
    tk.Label(Field_window, text="No.of.Column", font=("Arial", 12), bg=BG, fg="darkblue").pack(pady=5, padx=10, anchor="w")
    cum_entry = tk.Entry(Field_window, font=("Arial", 14))
    cum_entry.pack(pady=5, padx=10)

    tk.Label(Field_window, text="Select an Crop", font=("Arial", 12), bg=BG, fg="darkblue").pack(pady=5, padx=10, anchor="w")

    options = ["Ground Nut", "Cron", "Wheat"]
    dropdown_var = tk.StringVar()
    dropdown_var.set(options[0])  # Set default value
    dropdown_menu = tk.OptionMenu(Field_window, dropdown_var, *options)
    dropdown_menu.pack(pady=5)


    tk.Button(Field_window, text="Add Field",font=("Arial", 14), command=lambda:add(name_entry.get(),row_entry.get(),cum_entry.get(),dropdown_var.get(),Field_window)).pack(pady=10, padx=10)


def Field_Close(s,Field_window):
    Field_window.destroy()
    messagebox.showinfo("Info", s)
    
    
for i in Field_List:
    print(i.Name)    

def add(n,r,c,crop,Field_window):
    try:

        obj = Field(n,int(r),int(c),crop)

        Field_List.append(obj)
        Save_Fields(Field_List)
        
        
        Field_Close("Field Added",Field_window)


    except:
        print("Error")
        Field_Close("Error",Field_window)
