#!python
#or
#! (whole path)
import cgi #for importing cgi
print("Content-type: text/html\r\n\r\n") #specify content type
print("<html><body style='background-color: lightgreen'") #for html code
form=cgi.FieldStorage()
num1=form.getvalue("num1")
num2=form.getvalue("num2")
n1=int(num1)
n2=int(num2)
num3=n1+n2
print("<p>The addition of the numbers={}</p>".format(num3))

print("</body></html>")

