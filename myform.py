import cgi
import sqlite3
print("Content-type:text/html\r\n\r\n")
form=cgi.FieldStorage()
name=form.getvalue('sname')
rollno=form.getvalue('rollno')
branch=form.getvalue('branch')
print(name,rollno,branch)
con=sqlite3.connect('myform.sqlite')
cur=con.cursor()

cur.execute("create table if not exists myfom(Name text,Rollno integer,Branch text)")

rs=cur.execute("insert into myform values(?,?,?)",(name,rollno,branch))
#print("one record inserted successfully")
con.commit()
if(rs):
    print("<script>alert('login succss'):,/script.")
    print("<script window.locatin.href='http://localhost:8000/login.html;:</script>")
else:
    print("sorry,Please try again")
cur.close()
con.close()



