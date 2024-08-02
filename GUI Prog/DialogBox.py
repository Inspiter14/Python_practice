# Import the required library
from tkinter import *
from tkinter import ttk
#from tkinter import messagebox

# Create an instance of tkinter frame
win=Tk()

# Set the geometry
win.geometry("700x250")

# Define a button to show the popup message box
def on_click():
   messagebox.showinfo("Message", "Hey folks!")

# Add a Label widget
Label(win, text="Click the button to open a popup", font=('Georgia 13'))

# Create a button to open the popup dialog
ttk.Button(win, text="Open Popup", command=on_click).pack(pady=30)
