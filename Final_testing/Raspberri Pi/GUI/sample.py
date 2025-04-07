import tkinter as tk

# Global variable to store the current pop-up buttons
popup_buttons = []

def clear_previous_buttons():
    # Destroy any existing buttons in the popup_buttons list
    global popup_buttons
    for button in popup_buttons:
        button.destroy()
    popup_buttons = []  # Clear the list

def show_buttons_1():
    clear_previous_buttons()  # Clear the previous buttons
    
    # Create and display 4 new buttons to the right of Main Button 1
    btn1 = tk.Button(window, text="Popup 1A")
    btn1.place(x=200, y=50)  # Place right of Main Button 1
    popup_buttons.append(btn1)
    
    btn2 = tk.Button(window, text="Popup 1B")
    btn2.place(x=200, y=80)
    popup_buttons.append(btn2)
    
    btn3 = tk.Button(window, text="Popup 1C")
    btn3.place(x=200, y=110)
    popup_buttons.append(btn3)
    
    btn4 = tk.Button(window, text="Popup 1D")
    btn4.place(x=200, y=140)
    popup_buttons.append(btn4)

def show_buttons_2():
    clear_previous_buttons()  # Clear the previous buttons
    
    # Create and display 4 new buttons to the right of Main Button 2
    btn1 = tk.Button(window, text="Popup 2A")
    btn1.place(x=200, y=180)  # Place right of Main Button 2
    popup_buttons.append(btn1)
    
    btn2 = tk.Button(window, text="Popup 2B")
    btn2.place(x=200, y=210)
    popup_buttons.append(btn2)
    
    btn3 = tk.Button(window, text="Popup 2C")
    btn3.place(x=200, y=240)
    popup_buttons.append(btn3)
    
    btn4 = tk.Button(window, text="Popup 2D")
    btn4.place(x=200, y=270)
    popup_buttons.append(btn4)

def show_buttons_3():
    clear_previous_buttons()  # Clear the previous buttons
    
    # Create and display 4 new buttons to the right of Main Button 3
    btn1 = tk.Button(window, text="Popup 3A")
    btn1.place(x=200, y=310)  # Place right of Main Button 3
    popup_buttons.append(btn1)
    
    btn2 = tk.Button(window, text="Popup 3B")
    btn2.place(x=200, y=340)
    popup_buttons.append(btn2)
    
    btn3 = tk.Button(window, text="Popup 3C")
    btn3.place(x=200, y=370)
    popup_buttons.append(btn3)
    
    btn4 = tk.Button(window, text="Popup 3D")
    btn4.place(x=200, y=400)
    popup_buttons.append(btn4)

# Main window
window = tk.Tk()
window.geometry("400x500")
window.title("Main Buttons Down, Pop-up Buttons to the Right")

# Main buttons to trigger the different sets of pop-up buttons
main_button_1 = tk.Button(window, text="Main Button 1", command=show_buttons_1)
main_button_1.place(x=50, y=50)  # Place Main Button 1 downwards

main_button_2 = tk.Button(window, text="Main Button 2", command=show_buttons_2)
main_button_2.place(x=50, y=180)  # Place Main Button 2 downwards

main_button_3 = tk.Button(window, text="Main Button 3", command=show_buttons_3)
main_button_3.place(x=50, y=310)  # Place Main Button 3 downwards

# Run the application
window.mainloop()
