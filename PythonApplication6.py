import  sqlite3


conn  =  sqlite3 . connect ( 'mydatabase.db' )
cursor  =  conn.cursor ()
#create the table 
#DONT MESS WITH THE INPUT CODE
#inputs
s_id = input('Snumber:')
s_name = input('Name:')
s_print = input('Print:')
s_date = input('Date:')
#Adding to the table after a user does an input
cursor.execute("""
INSERT INTO CGI(Snumber, Name, Print, Date)
VALUES (?,?,?,?)
""", (s_id, s_name, s_print, s_date))
conn.commit ()
print ( 'Data entered successfully.' )
#telling you if it done correctly
conn . close ()
if (conn):
  conn.close()
  print("\nThe SQLite connection is closed.")
#saying it done
