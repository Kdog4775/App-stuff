import sqlite3 as sql
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
window = tkinter.Tk()
window.title("3D Printer Scheduler")
viewButton = tkinter.Button(window, text="View Database", command=seeData)
addButton = tkinter.Button(window, text="Add Database", command=addData)

nameLabel = tkinter.Label(window, text="Enter name: ")
nameEntry = tkinter.Entry(window)

snumberLabel = tkinter.Label(window, text="Enter snumber: ")
snumberEntry = tkinter.Entry(window)
dateLabel = tkinter.Label(window, text="Enter Date: ")
dateEntry = tkinter.Entry(window)
printLabel = tkinter.Label(window, text="Enter Print Time: ")
printEntry = tkinter.Entry(window)
endLabel = tkinter.Label(window, text="Enter Print end time: ")
endEntry = tkinter.Entry(window)

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
addButton.pack()

window.mainloop()
Cgi.Close()
