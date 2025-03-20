import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to dynamically add names and status
def add_item():
    name = name_entry.get()
    status = status_var.get()  # Gets the selected status ("Green" or "Red")
    
    if name:  # Only add if name is not empty
        tk.Label(side_menu, text=f"{name}: {status}", font=("Arial", 12), bg="darkgray", fg="white").pack(pady=5, padx=10)

    # Clear input fields
    name_entry.delete(0, tk.END)
    status_var.set("")

# Function to update time and date
def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")  # Get current time (24-hour format)
    current_date = datetime.now().strftime("%Y-%m-%d")  # Get current date (Year-Month-Day)
    
    time_label.config(text=current_time)  # Update the time label
    date_label.config(text=current_date)  # Update the date label
    
    # Call this function again after 1000 ms (1 second)
    window.after(1000, update_time)

# Main window
window = tk.Tk()
window.geometry("800x480")  # Set the resolution to fit the 800x480 screen
window.title("Dynamic Menu with User Input")
window.configure(bg="lightgray")

# Left side menu frame
side_menu = tk.Frame(window, bg="darkgray", width=200)
side_menu.pack(side="left", fill="y")

# Add user input fields
name_entry = tk.Entry(side_menu, font=("Arial", 14))
name_entry.pack(pady=10, padx=10,)

status_var = tk.StringVar()

status_green = tk.Radiobutton(side_menu, text="Green", variable=status_var, value="Green", font=("Arial", 12), bg="darkgray", fg="white", selectcolor="darkgray")
status_green.pack(pady=5)

status_red = tk.Radiobutton(side_menu, text="Red", variable=status_var, value="Red", font=("Arial", 12), bg="darkgray", fg="white", selectcolor="darkgray")
status_red.pack(pady=5)

# Button to add name and status
tk.Button(side_menu, text="Add", font=("Arial", 14), command=add_item).pack(pady=10, padx=10)

# Create time and date labels
time_label = tk.Label(window, font=("Arial", 40), bg="lightgray", fg="black")
time_label.pack(pady=50)

date_label = tk.Label(window, font=("Arial", 30), bg="lightgray", fg="black")
date_label.pack(pady=20)

# Initial call to update the time
update_time()

# Run the application
window.mainloop()
