# import all functions from the tkinter   
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing PIL for image handling
import pygame # Pygame or sounds.
pygame.mixer.init()
# Assets
back = "Assets/beautiful.png"
texture = "Assets/purple.jpg"
button_sound = "Assets/Los Tigres del Norte - La Granja.mp3"

def clearAll(): # Function for clearing the contents of all text entry boxes
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    givenDayField.delete(0, END)
    givenMonthField.delete(0, END)
    givenYearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)
 
def checkError(): # function for checking error
    if (dayField.get() == "" or monthField.get() == ""
        or yearField.get() == "" or givenDayField.get() == ""
        or givenMonthField.get() == "" or givenYearField.get() == "") :
        messagebox.showerror("Input Error")
        clearAll()
        return -1
 
def calculateAge(): # function to calculate age 
    value = checkError()
    if value ==  -1: 
        return
    else :
        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())
 
        given_day = int(givenDayField.get())
        given_month = int(givenMonthField.get())
        given_year = int(givenYearField.get())
         
        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (birth_day > given_day):
            given_month = given_month - 1
            given_day = given_day + month[birth_month-1] 
        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12
        calculated_day = given_day - birth_day; 
        calculated_month = given_month - birth_month; 
        calculated_year = given_year - birth_year;
         
        rsltDayField.insert(10, str(calculated_day))
        rsltMonthField.insert(10, str(calculated_month))
        rsltYearField.insert(10, str(calculated_year))
        
def play_sound(): # Play sound function.
    pygame.mixer.music.load(button_sound)
    pygame.mixer.music.play()
 
if __name__ == "__main__" :
    root = Tk()
    root.title("Age Calculator")
    root.geometry("620x400")

    # Load the background image
    image_path = back
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Load button images
    resultant_age_img = Image.open(texture).resize((50, 20))
    resultant_age_photo = ImageTk.PhotoImage(resultant_age_img)
    clear_all_img = Image.open(texture).resize((50, 20))
    clear_all_photo = ImageTk.PhotoImage(clear_all_img)

    # Load label images
    dob_img = Image.open(texture).resize((50, 20))
    dob_photo = ImageTk.PhotoImage(dob_img)
    given_date_img = Image.open(texture).resize((50, 20))
    given_date_photo = ImageTk.PhotoImage(given_date_img)
    day_img = Image.open(texture).resize((50, 20))
    day_photo = ImageTk.PhotoImage(day_img)
    month_img = Image.open(texture).resize((50, 20))
    month_photo = ImageTk.PhotoImage(month_img)
    year_img = Image.open(texture).resize((50, 20))
    year_photo = ImageTk.PhotoImage(year_img)
    given_day_img = Image.open(texture).resize((50, 20))
    given_day_photo = ImageTk.PhotoImage(given_day_img)
    given_month_img = Image.open(texture).resize((50, 20))
    given_month_photo = ImageTk.PhotoImage(given_month_img)
    given_year_img = Image.open(texture).resize((50, 20))
    given_year_photo = ImageTk.PhotoImage(given_year_img)
    rslt_year_img = Image.open(texture).resize((50, 20))
    rslt_year_photo = ImageTk.PhotoImage(rslt_year_img)
    rslt_month_img = Image.open(texture).resize((50, 20))
    rslt_month_photo = ImageTk.PhotoImage(rslt_month_img)
    rslt_day_img = Image.open(texture).resize((50, 20))
    rslt_day_photo = ImageTk.PhotoImage(rslt_day_img)

    # Create a canvas
    canvas = Canvas(root, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)

    # Set the background image
    canvas.create_image(0, 0, image=photo, anchor="nw")

    # Function to create and place labels and entries on the canvas
    def create_widget(widget, row, column, padx=0, pady=0):
        canvas.create_window((column*100)+50, (row*30)+50, anchor="nw", window=widget)

    # Create labels with images and text
    dob = Label(root, image=dob_photo, text="Date Of Birth", compound="center", fg="white")
    givenDate = Label(root, image=given_date_photo, text="Given Date", compound="center", fg="white")
    day = Label(root, image=day_photo, text="Day", compound="center", fg="white")
    month = Label(root, image=month_photo, text="Month", compound="center", fg="white")
    year = Label(root, image=year_photo, text="Year", compound="center", fg="white")
    givenDay = Label(root, image=given_day_photo, text="Given Day", compound="center", fg="white")
    givenMonth = Label(root, image=given_month_photo, text="Given Month", compound="center", fg="white")
    givenYear = Label(root, image=given_year_photo, text="Given Year", compound="center", fg="white")
    rsltYear = Label(root, image=rslt_year_photo, text="Years", compound="center", fg="white")
    rsltMonth = Label(root, image=rslt_month_photo, text="Months", compound="center", fg="white")
    rsltDay = Label(root, image=rslt_day_photo, text="Days", compound="center", fg="white")

    # Create buttons with images and text
    resultantAge = Button(root, image=resultant_age_photo, text="Resultant Age", compound="center", fg="white", command=lambda: [calculateAge(), play_sound()], borderwidth=0)
    clearAllEntry = Button(root, image=clear_all_photo, text="Clear All", compound="center", fg="white", command=lambda: [clearAll(), play_sound()], borderwidth=0)

    dayField = Entry(root)
    monthField = Entry(root)
    yearField = Entry(root)
    givenDayField = Entry(root)
    givenMonthField = Entry(root)
    givenYearField = Entry(root)
    rsltYearField = Entry(root)
    rsltMonthField = Entry(root)
    rsltDayField = Entry(root)

    create_widget(dob, 0, 1)
    create_widget(day, 1, 0)
    create_widget(dayField, 1, 1)
    create_widget(month, 2, 0)
    create_widget(monthField, 2, 1)
    create_widget(year, 3, 0)
    create_widget(yearField, 3, 1)
    create_widget(givenDate, 0, 4)
    create_widget(givenDay, 1, 3)
    create_widget(givenDayField, 1, 4)
    create_widget(givenMonth, 2, 3)
    create_widget(givenMonthField, 2, 4)
    create_widget(givenYear, 3, 3)
    create_widget(givenYearField, 3, 4)
    create_widget(resultantAge, 4, 2)
    create_widget(rsltYear, 5, 2)
    create_widget(rsltYearField, 6, 2)
    create_widget(rsltMonth, 7, 2)
    create_widget(rsltMonthField, 8, 2)
    create_widget(rsltDay, 9, 2)
    create_widget(rsltDayField, 10, 2)
    create_widget(clearAllEntry, 12, 2)

    root.mainloop()