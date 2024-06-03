from tkinter import *
from tkinter import ttk
from pathlib import Path

root = Tk()

bg = PhotoImage(file="C:\Users\GRANT\Desktop\Tkinter\images\painting.jpg")

root.title('Setting Image')
root.geometry("1280x720")

my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

my_text = Label(root, text="Welcome!", )
my_text.pack(pady=50)

root.mainloop()
