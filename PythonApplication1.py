from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import sqlite3


conn  =  sqlite3 . connect ( 'quit.db' )

with sqlite3.connect('quit.db') as db:
    c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Snumber(Snumber n(5), Name char(30), Print char(35), Date decimal(7,2));")
db.commit()
db.close()
print('so far so good')

root = Tk()
root.title('Form')
root.geometry('400x350+300+300')
root.mainloop()