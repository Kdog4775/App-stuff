import sqlite3 as sql
from tkinter import ttk
from ttkthemes import ThemedTk

Cgi = sql.connect("Cgi.DB")
c = Cgi.cursor()
#create Cgi table if it doesnt exist create one

c.execute("""CREATE TABLE IF NOT EXISTS Cgi
(name text, snumber int, date int, print int, end int, email int)""")

#function to add data to database
def addData():
    name=nameEntry.get()
    snumber=snumberEntry.get()
    date=dateEntry.get()
    print=printEntry.get()
    end=endEntry.get()
    email=emailEntry.get()
    c.execute ("INSERT INTO Cgi VALUES (?,?,?,?,?,?) ", (name,snumber,date,print,end,email))
    Cgi.commit()

#function to view data
def seeData():
    c.execute("SELECT * FROM Cgi")
    rows = c.fetchall()
    for row in rows:
        print(row)

#create the window for the GUI and add a title
window = ThemedTk(theme="equilux")
window.config(themebg="equilux")
window.title("3D Printer Scheduler")
window.geometry('300x320')

viewButton = ttk.Button(window, text="View Database", command=seeData)
addButton = ttk.Button(window, text="Add Database", command=addData)

nameLabel = ttk.Label(window, text="Enter name: ")
nameEntry = ttk.Entry(window)

snumberLabel = ttk.Label(window, text="Enter snumber: ")   #S-number txt box
snumberEntry = ttk.Entry(window)
dateLabel = ttk.Label(window, text="Enter Date: ")
dateEntry = ttk.Entry(window)
printLabel = ttk.Label(window, text="Enter Print Time: ")
printEntry = ttk.Entry(window)
endLabel = ttk.Label(window, text="Enter Print end time: ")
endEntry = ttk.Entry(window)
emailLabel = ttk.Label(window, text="Enter school email")
emailEntry = ttk.Entry(window)

#add labels and text entry/buttons to GUI

viewButton.pack()
nameLabel.pack()
nameEntry.pack()
snumberLabel.pack()
snumberEntry.pack()
dateLabel.pack()
dateEntry.pack()
printLabel.pack()
printEntry.pack()
endLabel.pack()
endEntry.pack()
emailLabel.pack()
emailEntry.pack()
addButton.pack()

window.mainloop()
Cgi.close()