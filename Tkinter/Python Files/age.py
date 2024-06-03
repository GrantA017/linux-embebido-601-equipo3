# import all functions from the tkinter   
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing PIL for image handling

back = "C:/Users/GRANT/OneDrive/Coding & Math/Tkinter/beautiful.png"

# Function for clearing the  
# contents of all text entry boxes
def clearAll() :
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    givenDayField.delete(0, END)
    givenMonthField.delete(0, END)
    givenYearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)
 
# function for checking error
def checkError() :
    if (dayField.get() == "" or monthField.get() == ""
        or yearField.get() == "" or givenDayField.get() == ""
        or givenMonthField.get() == "" or givenYearField.get() == "") :
        messagebox.showerror("Input Error")
        clearAll()
        return -1
 
# function to calculate Age 
def calculateAge() :
    value = checkError()
    if value ==  -1 :
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
 
if __name__ == "__main__" :
    gui = Tk()
    gui.title("Age Calculator")
    gui.geometry("525x260")

    # Load the background image
    image_path = back  # Replace with your image path
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Create a canvas
    canvas = Canvas(gui, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)

    # Set the background image
    canvas.create_image(0, 0, image=photo, anchor="nw")

    # Function to create and place labels and entries on the canvas
    def create_widget(widget, row, column, padx=0, pady=0):
        canvas.create_window((column*100)+50, (row*30)+50, anchor="nw", window=widget)

    dob = Label(gui, text = "Date Of Birth", bg = "blue")
    givenDate = Label(gui, text = "Given Date", bg = "blue")
    day = Label(gui, text = "Day", bg = "light green")
    month = Label(gui, text = "Month", bg = "light green")
    year = Label(gui, text = "Year", bg = "light green")
    givenDay = Label(gui, text = "Given Day", bg = "light green")
    givenMonth = Label(gui, text = "Given Month", bg = "light green")
    givenYear = Label(gui, text = "Given Year", bg = "light green")
    rsltYear = Label(gui, text = "Years", bg = "light green")
    rsltMonth = Label(gui, text = "Months", bg = "light green")
    rsltDay = Label(gui, text = "Days", bg = "light green")

    resultantAge = Button(gui, text = "Resultant Age", fg = "Black", bg = "Red", command = calculateAge)
    clearAllEntry = Button(gui, text = "Clear All", fg = "Black", bg = "Red", command = clearAll)

    dayField = Entry(gui)
    monthField = Entry(gui)
    yearField = Entry(gui)
    givenDayField = Entry(gui)
    givenMonthField = Entry(gui)
    givenYearField = Entry(gui)
    rsltYearField = Entry(gui)
    rsltMonthField = Entry(gui)
    rsltDayField = Entry(gui)

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

    gui.mainloop()
