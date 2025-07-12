from email.message import Message
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pyqrcode
import png
from PIL import Image
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkImage
import customtkinter as ttk
global get_image

root = ttk.CTk()
root.geometry("600x600")
# root.config(bg="gray")
ttk.set_appearance_mode('system')
ttk.set_default_color_theme('blue')

def create_code():
    # File dialog
    input_path = filedialog.asksaveasfilename(title="Save Image",
    filetypes= (("PNG File", ".png"), ("All Files", "*.*")))
    if input_path:
        if input_path.endswith(".png"):
            # Create QR Code from entry box
            get_code = pyqrcode.create(entry_one.get())
            # Save as PNG File
            get_code.png(input_path,scale=200, module_color=(104, 17, 193), background=(0,0,0))
        else:
            # Add that .png to the end of the file name
            input_path = f'{input_path}.png'
            # Create QR Code from entry box
            get_code = pyqrcode.create(entry_one.get())
            # Save as PNG File
            get_code.png(input_path, scale=200, module_color=(104,17,193), background=(0,0,0))

        # Put QR Code on screen
        global get_image
        get_image = ttk.CTkImage(Image.open(input_path),size=(250,250))
        # Add image to label
        my_label.configure(image=get_image)
        # Delete entry box
        entry_one.delete(0, END)
        # Flash up a finish message
        entry_one.insert(0, "Finished!")


def clear_all():
    entry_one.delete(0,END)
    my_label.configure(text="")

# GUI
instruction_label = CTkLabel(root, text="Enter the information you want to encode below",font=("Comic Sans", 18), justify='center')
instruction_label.pack()
entry_one = CTkEntry(root, font=("Comic Sans", 18), justify='center',width=300)
entry_one.pack(pady=20)

button_1 = CTkButton(root, text="Create QR Code", command=create_code,font=("Comic Sans", 18))
button_1.pack(pady=20)

button_2 = CTkButton(root, text="Clear", font=("Comic Sans", 18), command=clear_all)
button_2.pack(pady=20)

my_label = CTkLabel(root, text='')
my_label.pack(pady=20)

root.bind('<Return>', lambda event=None: button_1.invoke())
root.mainloop()
