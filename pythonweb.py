#!C:/Users/pramo/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.12/python
print("content-type:text/html")
print()
import cgi

print("<h1>welcome</h1>") 

form=cgi.FieldStorage()
name=form.getvalue("fullname")
dob=form.getvalue("dob")
email=form.getvalue("email")
phone=form.getvalue("phone")
address=form.getvalue("address")
arrival=form.getvalue("arrival")
explore=form.getvalue("explore")
members=form.getvalue("members")
pall=form.getvalue("pall") 
Temples=form.getvalue("Temples")
Beaches=form.getvalue("Beaches")
Boating=form.getvalue("Boating")
Sanctuary=form.getvalue("Sanctuary")
Musuem=form.getvalue("Musuem")
Accommodation=form.getvalue("Accommodation")
vehicle=form.getvalue("vehicle")
aadhar=form.getvalue("aadhar")
Upload=form.getvalue("Upload")  

import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='',database='tourist')
print(conn)
cur=conn.cursor()


cur.execute("insert into register values({},'{}','{}',{},'{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')",(name,dob,email,phone,address,arrival,explore,members,pall,Temples,Beaches,Boating,Sanctuary,Musuem,Accommodation,vehicle,aadhar,Upload))
conn.commit()
cur.close()
conn.close()
print("Insert successfully")
print("<a href='index.html'>go back</a>")
