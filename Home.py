from tkinter import *
import mysql.connector

from add import *
from delete import *
from issue import *
from Return import *
from view import *

db = mysql.connector.connect(host="localhost", user="root", password='vipinkumarsharma', database='db')
cursor = db.cursor()

window = Tk()
window.title("NTSC Library Management System")

greet = Label(window, font=('arial', 30, 'bold'), text="Welcome to Library Management System!")
greet.grid(row=0, columnspan=3)

addbtn = Button(window, text="Add Books", command=addBooks, bg="DodgerBlue2", fg="white", font=('arial', 20, 'bold'))
addbtn.grid(row=3, columnspan=3)

deletebtn = Button(window, text="Delete Books", command=deleteBooks, bg="DodgerBlue2", fg="white",
                   font=('arial', 20, 'bold'))
deletebtn.grid(row=5, columnspan=3)

issuebtn = Button(window, text="Issue Books", command=issueBooks, bg="DodgerBlue2", fg="white",
                  font=('arial', 20, 'bold'))
issuebtn.grid(row=7, columnspan=3)

returnbtn = Button(window, text="Return Books", command=returnBooks, bg="DodgerBlue2", fg="white",
                   font=('arial', 20, 'bold'))
returnbtn.grid(row=9, columnspan=3)

viewbtn = Button(window, text="View Books", command=viewBooks, bg="DodgerBlue2", fg="white", font=('arial', 20, 'bold'))
viewbtn.grid(row=11, columnspan=3)

greet = Label(window, font=('arial', 15, 'bold'), text="Thank you")
greet.grid(row=13, columnspan=3)

window.mainloop()