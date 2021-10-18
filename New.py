import sqlite3 as sql
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import *
from tkinter import messagebox as tkMessagebox
import tkinter

Cgi = sql.connect("Cgi.DB")
c = Cgi.cursor()
#create Cgi table if it doesnt exist create one

c.execute("""CREATE TABLE IF NOT EXISTS Cgi
(name text, snumber int, date int, print int, end int)""")

#function to add data to database
def addData():
    name=nameEntry.get()
    snumber=snumberEntry.get()
    date=dateEntry.get()
    print=printEntry.get()
    end=endEntry.get()
    c.execute ("INSERT INTO Cgi VALUES (?,?,?,?,?) ", (name,snumber,date,print,end))
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

"""viewButton = ttk.Button(window, text="View Database", command=seeData)
addButton = ttk.Button(window, text="Add Database", command=addData)"""

nameLabel = ttk.Label(window, text="Name: Panda ")
snumberLabel = ttk.Label(window, text="S-number: 42069")

labelTop = ttk.Label(window, text="Choose a Date",)
comboexample = ttk.Combobox(window,
                            values=["October", "November", "December"], state="readonly")

comboexample.current(1)
print(comboexample.current(), comboexample.get())

submitButton = ttk.Button(window, text="Submit")
viewButton = ttk.Button(window, text="View Calendar")
#add labels and text entry/buttons to GUI
nameLabel.pack()
snumberLabel.pack()
labelTop.pack()
comboexample.pack()
submitButton.pack(side=LEFT)
viewButton.pack(side=RIGHT)

window.mainloop()
Cgi.close()
