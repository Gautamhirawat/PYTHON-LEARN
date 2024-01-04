import tkinter as tk
from tkinter import messagebox

# creating some dummy functions for now 
def create_form():
    label.config(text="Creating Google Form...")

def monitor_progress():
    label.config(text="Monitoring progress...")

def click_button():
    label.config(text="Button clicked!")

def about():
    messagebox.showinfo("About", "Google Forms App")

def dummy_function():
    label.config(text="This is a dummy function.")

def exit_application():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

root = tk.Tk()
root.title("Google Forms App")
root.minsize(300, 200)

# linking those dunmmy function with butoon 
def menu_command(action):
    if action == "New Form":
        create_form()
    elif action == "Monitor Progress":
        monitor_progress()
    elif action == "Click Me":
        click_button()
    elif action == "Dummy Function":
        dummy_function()
    elif action == "Exit":
        exit_application()
    elif action == "About":
        about()

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New Form", command=lambda: menu_command("New Form"))
file_menu.add_command(label="Monitor Progress", command=lambda: menu_command("Monitor Progress"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=lambda: menu_command("Exit"))
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Click Me", command=lambda: menu_command("Click Me"))
edit_menu.add_command(label="Dummy Function", command=lambda: menu_command("Dummy Function"))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: menu_command("About"))
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

label = tk.Label(root, text="Welcome to Google Forms App!", padx=10, pady=10)
label.pack()

root.mainloop()
