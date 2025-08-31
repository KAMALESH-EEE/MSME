import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from Field import Get_Field, Delete_Field, Show_Field
from DEVICE import SetTask, Main, DATA

window = tk.Tk()
window.title("GUI")

BG="lightblue"

window.geometry("800x480")
window.configure(bg=BG)

#++++++++++Title++++++++++++++++++++++++
Main_Name = tk.Label(window, text="MARS", font=("Arial", 24), bg=BG, fg="red")
Main_Name.pack(pady=1)  

Main_Name1 = tk.Label(window, text="Mechanized Agriculture Robotic System", font=("Arial", 15), bg=BG, fg="green")
Main_Name1.pack(pady=2)
#+++++++++++++++++++++++++++++++++++++++++++++




# Function to update time and date
def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")  # Get current time (24-hour format)
    current_date = datetime.now().strftime("%d-%m-%Y")  # Get current date (Year-Month-Day)
    
    time_label.config(text="System Time: "+current_time)  # Update the time label
    date_label.config(text="Date: "+current_date)  # Update the date label
    GUI_STAUS = 'CONNECTED' if DATA[15] == 'GUI' else 'DISCONNECTED'
    Sfg = 'green' if GUI_STAUS == 'CONNECTED' else 'red'
    gui_label.config(text=GUI_STAUS, fg = Sfg) 
    # Call this function again after 1000 ms (1 second)
    window.after(1000, update_time)

time_label = tk.Label(window, font=("Arial", 15), bg=BG, fg="yellow")
time_label.pack(pady=1)
date_label = tk.Label(window, font=("Arial", 15), bg=BG, fg="yellow")
date_label.pack(pady=1)

gui_label = tk.Label(window, font=("Arial", 15), bg=BG, fg="red")
gui_label.pack(pady=1)

# Initial call to update the time
update_time()

#==========================MENU==========================================

def show_about():
    messagebox.showinfo("About", "MARS Application\nVersion: 1.00")
def show_help():
    messagebox.showinfo("Help", "Contact Developers\nMail: kamaleshravi66@gmail.com")

def Will_Add():
    print("Yet to develop")

def Field_add_window():
    Get_Field(window)

def Field_Del_window():
    Delete_Field(window)

def Field_Show_window():
    Show_Field(window)

def FERT_SPRAY ():
    SetTask('Spray',window)
    


#++++++++++++++++++++++Drop Down Button++++++++++++++++++++++++++++++++++++++

popup_buttons = []

def clear_previous_buttons():
    # Destroy any existing buttons in the popup_buttons list
    global popup_buttons
    for button in popup_buttons:
        button.destroy()
    popup_buttons = []  # Clear the list

def show_buttons_1():
    clear_previous_buttons()  # Clear the previous buttons
    
    # Create and display 4 new buttons to the right of Main Button 2
    btn1 = tk.Button(window, text="button" , command=Will_Add)
    btn1.place(x=300, y=180)  # Place right of Main Button 2
    popup_buttons.append(btn1)
    
    btn2 = tk.Button(window, text="button" , command=Will_Add)
    btn2.place(x=300, y=210)
    popup_buttons.append(btn2)
    
    btn3 = tk.Button(window, text="button" , command=Will_Add)
    btn3.place(x=300, y=240)
    popup_buttons.append(btn3)
    
    btn4 = tk.Button(window, text="button" , command=Will_Add)
    btn4.place(x=300, y=270)
    popup_buttons.append(btn4)


def show_buttons_2():
    clear_previous_buttons()  # Clear the previous buttons
    
    # Create and display 4 new buttons to the right of Main Button 2
    btn1 = tk.Button(window, text="ADD" , command=Field_add_window)
    btn1.place(x=300, y=180)  # Place right of Main Button 2
    popup_buttons.append(btn1)
    
    btn2 = tk.Button(window, text="VIEW" , command=Field_Show_window)
    btn2.place(x=300, y=210)
    popup_buttons.append(btn2)
    
    btn3 = tk.Button(window, text="DELETE" , command=Field_Del_window)
    btn3.place(x=300, y=240)
    popup_buttons.append(btn3)
    
    btn4 = tk.Button(window, text="Edit" , command=Will_Add)
    btn4.place(x=300, y=270)
    popup_buttons.append(btn4)

def show_buttons_3():
    clear_previous_buttons()  # Clear the previous buttons
    
    # Create and display 4 new buttons to the right of Main Button 2
    btn1 = tk.Button(window, text="Fertilizer Spray" , command=FERT_SPRAY)
    btn1.place(x=300, y=180)  # Place right of Main Button 2
    popup_buttons.append(btn1)
    
    btn2 = tk.Button(window, text="button" , command=Will_Add)
    btn2.place(x=300, y=210)
    popup_buttons.append(btn2)
    
    btn3 = tk.Button(window, text="button" , command=Will_Add)
    btn3.place(x=300, y=240)
    popup_buttons.append(btn3)
    
    btn4 = tk.Button(window, text="button" , command=Will_Add)
    btn4.place(x=300, y=270)
    popup_buttons.append(btn4)

def Connect():
    clear_previous_buttons()  # Clear the previous buttons
    Main()



# Left side menu frame
side_menu = tk.Frame(window, bg=BG, width=50, height=5)
side_menu.pack(side="left", fill="y")

# Bottom menu frame
bottom_menu = tk.Frame(window, bg=BG, height=10)
bottom_menu.pack(side="bottom", fill="x")

# Add buttons to the side menu (similar to a menu)
tk.Button(side_menu, text="BITE", font=("Arial", 14), command=show_buttons_1).pack(pady=2, padx=50)
tk.Button(side_menu, text="Field", font=("Arial", 14), command=show_buttons_2).pack(pady=2, padx=50)
tk.Button(side_menu, text="Task", font=("Arial", 14), command=show_buttons_3).pack(pady=2, padx=50)
tk.Button(side_menu, text="Connect", font=("Arial", 14), command=Connect).pack(pady=2, padx=50)
#tk.Button(side_menu, text="Exit", font=("Arial", 14), command=window.quit).pack(pady=10, padx=20)

# Add buttons to the bottom menu
tk.Button(bottom_menu, text="Help", font=("Arial", 14), command=show_help).pack(side="left", padx=20)
tk.Button(bottom_menu, text="About", font=("Arial", 14), command=show_about).pack(side="left", padx=20)
tk.Button(bottom_menu, text="Exit", font=("Arial", 14), command=window.quit).pack(side="left", padx=20)

#=================================================================================

# Run the application
window.mainloop()
