from tkinter import *
from tkinter import messagebox
import mysql.connector


def issue_db():
    global id
    global StudentName

    bid = id.get()
    bStudentName = StudentName.get()

    db = mysql.connector.connect(host="localhost", user="root", password='vipinkumarsharma', database='db')
    cursor = db.cursor()

    print(bid, end='--')
    print(bStudentName, end='--')
    print("issue")

    try:
        checkavailability = " select * from books where available='YES';"
        print(checkavailability)
        cursor.execute(checkavailability)

        flag = 0

        for i in cursor:
            print(i[0])
            if (i[0] == bid):
                flag = 1
                break;

        if flag == 1:
            updatequery = "update books set available='NO' where bid='" + bid + "';"
            print(updatequery)
            cursor.execute(updatequery)
            db.commit()

            sqlquery = "insert into issue values('" + bid + "','" + bStudentName + "' );"
            print(sqlquery)

            cursor.execute(sqlquery)
            db.commit()

            messagebox.showinfo('Success', "Book issued Successfully")
        else:
            messagebox.showinfo("Error", "Required Book is not available")
    except:
        messagebox.showinfo("Error", "Cannot issue given book ")


def issueBooks():
    global id
    global StudentName

    window = Tk()
    window.title('NTSC Library Management System')

    greet = Label(window, font=('arial', 30, 'bold'), text="Issue Books")
    greet.grid(row=0, columnspan=3)

    # ----------id-------------------

    L = Label(window, font=('arial', 15, 'bold'), text="Enter Book id: ")
    L.grid(row=2, column=1)

    L = Label(window, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=2, column=2)

    id = Entry(window, width=5, font=('arial', 15, 'bold'))
    id.grid(row=2, column=3)

    # ----------StudentName-------------------

    L = Label(window, font=('arial', 15, 'bold'), text="Enter StudentName: ")
    L.grid(row=4, column=1)

    L = Label(window, font=('arial', 15, 'bold'), text="   ")
    L.grid(row=4, column=2)

    StudentName = Entry(window, width=5, font=('arial', 15, 'bold'))
    StudentName.grid(row=4, column=3)

    submitbtn = Button(window, text="Submit", command=issue_db, bg="DodgerBlue2", fg="white",
                       font=('arial', 15, 'bold'))
    submitbtn.grid(row=8, columnspan=3)

    print("issue")
    pass
