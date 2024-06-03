import tkinter as tk
import tkinter as ttk
from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk

root = Tk()

class App(Frame):
    
    def __init__(self, master, *args, **kwargs) -> None: # Initializes Self.
        Frame.__init__(self, master, *args, **kwargs)
        self.master: Tk = master
        self.init_gui()

    def init_gui(self,) -> None: # GUI configuration.
        self.master.title = 'Welcome'
        self.master.geometry('1200x800')
        #Background
        self.background_image = Image.open('[1870-07-01] Herman Herzog - Alpine Landscape.jpg')
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.canvas = tk.Canvas(self, width=self.background_photo.width(), height=self.background_photo.height())
        self.canvas.pack(fill='both', expand=True)

        # Set the background image on the canvas
        self.canvas.create_image(0, 0, image=self.background_photo, anchor='nw')

# Main to run GUI.
if __name__ == '__main__':
    app = App(root)
    root.mainloop()