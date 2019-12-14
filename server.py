import socket
import collector
import string
from selenium import webdriver


sock=socket.socket()
sock.bind(('',9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

a=1
while a==1:
    data = conn.recv(1024)
    print("Data:",data)
    if data:
        a=0
    conn.send(data)

infonew = data.decode('utf-8')


a = infonew.split()  
os=a[0]
memory=a[1]
uname=a[2]

sop="""
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>DATA</title>
</head>
<body>
<table border="1" width="50%">
"""

scl="""
    </body>
</html>
"""

tab1="<tr> <td>OS</td> <td>" + str(os) + "</td> </tr>"
tab2="<tr> <td>Memory</td> <td>" + str(memory) + "</td> </tr>"
tab3="<tr> <td>Username</td> <td>" + str(uname) + "</td> </tr>"

out = open(r'C:\xampp\htdocs\E\index.html', 'w')
out.write(sop)
out.write(tab1)
out.write(tab2)
out.write(tab3)
out.write(scl)
out.close()

driver=webdriver.Chrome()
driver.get("http://localhost/e/index.html")
