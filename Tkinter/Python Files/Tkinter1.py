import tkinter as tk
import tkinter as ttk
from tkinter import *
from tkinter import Tk
from winsound import *
from tkinter import messagebox
root = Tk() # Initializes Tkinter.

img = PhotoImage(file='C:/Users/GRANT/OneDrive/Coding & Math/Tkinter/world.png')
bg = PhotoImage(file='C:/Users/GRANT/OneDrive/Coding & Math/Tkinter/beautiful.png')

class App(Frame):
    
    def __init__(self, master, *args, **kwargs) -> None: # Initializes Self.
        Frame.__init__(self, master, *args, **kwargs)
        self.master: Tk = master
        # Crear objetos del GUI.
        self.boton1: Button = self.create_button()
        self.boton2: Button = self.create_button()
        self.init_gui()

    def init_gui(self,) -> None: # GUI configuration.
        self.master.title = 'Welcome'
        self.master.geometry('1280x720')
        root.iconphoto(False, img)
        #Background
        canvas1 = Canvas(root, width=400, height=400)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image(0,0, image=bg, anchor = "nw")
        self.pack(fill='both', expand = True)
        # Row 0
        self.boton1.grid(row=0, column=3)
        self.boton2.grid(row=3, column=4)
        
    def create_button(self) -> Button:
        return Button(self,text='Boton')

# Main to run GUI.
if __name__ == '__main__':
    app = App(root)
    root.mainloop()