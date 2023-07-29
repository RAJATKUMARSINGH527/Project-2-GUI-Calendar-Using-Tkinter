
# Import all methods and classes from the tkinter module
from tkinter import *
# Importing the whole calendar module
from tkcalendar import *

# creating an object of the Tk() class
myCalendar=Tk()

# setting the title for the main window
myCalendar.title("Calendar")

# Setting the size and position of the main window
myCalendar.geometry("400x400")

# setting the background color of main Window
myCalendar.configure(background="gray")

#Add Calendar
MyCalndr = Calendar(myCalendar, selectmode = "day", date_pattern = "DD/MM/YYYY")
MyCalndr.pack(pady=20)

# Function for showing the calendar of the given year
def selected_date():
    date.config(text = "Your Selected Date is :- " + MyCalndr.get_date())

# Add calendar Button by calling the function
calendar_buttom = Button(myCalendar, text ="SELECT A DATE", command = selected_date)

# pack method is used for placing the widgets at respective positions in table like structure
calendar_buttom.pack(pady=20)

# Create a label for showing the content of the calendar
date = Label(myCalendar, text="")

# pack method is used for placing the widgets at respective positions in table like structure
date.pack(pady=20)

#Execute Tkinter
myCalendar.mainloop()