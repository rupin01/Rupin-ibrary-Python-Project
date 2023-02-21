from tkinter import *
from tkinter import messagebox
import mysql.connector


def return_db():
    global id

    bid = id.get()

    db = mysql.connector.connect(host="localhost", user="root", password='vipinkumarsharma', database='db')
    cursor = db.cursor()

    print(bid, end='--')
    print("return")

    try:
        checkavailability = " select * from books where available='NO';"
        print(checkavailability)
        cursor.execute(checkavailability)

        flag = 0

        for i in cursor:
            print(i[0])
            if (i[0] == bid):
                flag = 1
                break;

        if flag == 1:
            updatequery = "update books set available='YES' where bid='" + bid + "';"
            print(updatequery)
            cursor.execute(updatequery)
            db.commit()

            sqlquery = "delete from issue where bid='" + bid + "';"
            print(sqlquery)

            cursor.execute(sqlquery)
            db.commit()

            messagebox.showinfo('Success', "Book returned Successfully")
        else:
            messagebox.showinfo("Error", "Invalid Book id")
    except:
        messagebox.showinfo("Error", "Cannot return given book ")


def returnBooks():
    global id

    window = Tk()
    window.title('ProjectGurukul Library Management System')

    greet = Label(window, font=('arial', 30, 'bold'), text="Return Books")
    greet.grid(row=0, columnspan=3)

    L = Label(window, font=('arial', 15, 'bold'), text="Enter Book id: ")
    L.grid(row=2, column=1)

    L = Label(window, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=2, column=2)

    id = Entry(window, width=5, font=('arial', 15, 'bold'))
    id.grid(row=2, column=3)

    submitbtn = Button(window, text="Submit", command=return_db, bg="DodgerBlue2", fg="white",
                       font=('arial', 15, 'bold'))
    submitbtn.grid(row=8, columnspan=3)

    print("return")
    pass
