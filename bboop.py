class bloodBank:
    def adminLogin():
        #!python
        import cgi #for importing cgi
        import mysql.connector as con
        db=con.connect(host='localhost',user='root',passwd='',database='adminonly')
        print("Content-type: text/html\r\n\r\n") #specipy content type
        print('<html>') #for html code
        form=cgi.FieldStorage()
        adid=form.getvalue("adid")
        adpasswd=form.getvalue("adpasswd")
        cur=db.cursor()
        sql="select adid,adpasswd from adminid where adid='{}' and adpasswd='{}'".format(adid,adpasswd)
        cur.execute(sql)
        data=cur.fetchall()
        if len(data)>0:
            print("<p><center>Welcome Admin Manager</center></p>")
            print('<head>\
                <title>AdminLogin</title>\
                <style type="text/css">\
                        body{\
                                background-image: linear-gradient(to left, #ffcc66, #ffeecc);\
                \
                        }\
                        div{\
                                 border: 1px solid black;\
                     margin-top: 180px;\
                     margin-bottom: 200px;\
                     margin-right: 250px;\
                     margin-left: 372px;\
                     width: 300px;\
                        }\
                \
                </style>\
                </head>\
                  <body>\
                <div>\
                        <table>\
                        <tr><p><center><h3>Admin Register</h3></center></p></tr>\
                        <tr><p><center>Donor Information:-</center></p></tr><br>\
                        <form method="get" action="/cgi-bin/pythonfile/showinfo.py">\
                        <tr><center><input type="submit" name="Login" value="Show"></center></tr><br>\
                        </form>\
                        <form method="get" action="/cgi-bin/pythonfile/showinfo1.py">\
                        <tr>Donor Id : <input type="text" name="doid" required=""><br></tr>\
                        <tr><center><input type="submit" name="Login" value="Search"></center></tr><br>\
                        </form>\
                        <tr><center><a href="/pythonprogram/donreg.html">Register</center></tr><br>\
                </table>\
                \
        </div>\
        </body>')
            
            
        else:
           print('<head>\
                <title>AdminLogin</title>\
                <style type="text/css">\
                        body{\
                                background-image: linear-gradient(to left, #ffcc66, #ffeecc);\
                \
                        }\
                        div{\
                                 border: 1px solid black;\
                     margin-top: 180px;\
                     margin-bottom: 200px;\
                     margin-right: 250px;\
                     margin-left: 372px;\
                     width: 300px;\
                        }\
                \
                </style>\
                </head>\
                  <body>\
                <div>\
                        <table>\
                        <tr><p><center><h3>Not An Admin,Please use the correct admin ID and Password.</h3></center></p></tr>	</table>\
                \
        </div>\
        </body>')
        print("</body>")
        print("</html>")
        db.close()


    def donorLogin():
        #!python
        import cgi #for importing cgi
        import mysql.connector as con
        db=con.connect(host='localhost',user='root',passwd='',database='donoronly')
        print("Content-type: text/html\r\n\r\n") #specipy content type
        print('<html>') #for html code
        form=cgi.FieldStorage()
        doid=form.getvalue("doid")
        dopasswd=form.getvalue("dopasswd")
        cur=db.cursor()
        sql="select fnmae,passwd from donorid where fnmae='{}' and passwd='{}'".format(doid,dopasswd)
        cur.execute(sql)
        data=cur.fetchall()
        if len(data)>0:
            for i in data:
                print('<center>',i[0],'</center>')
            print("<p><center>Welcome Blood Donor</center></p>")
            print("<p><center>Your availability here is Appreciated. :)</center></p>")
            print('<head>\
                <title>Donor Login</title>\
                <style type="text/css">\
                        body{\
                                background-image: linear-gradient(to left, #ffcc66, #ffeecc);\
                        }\
                        div{\
                                 border: 1px solid black;\
                     margin-top: 80px;\
                     margin-bottom: 200px;\
                     margin-right: 250px;\
                     margin-left: 372px;\
                     width: 300px;\
                        }\
                </style>\
                </head>\
                <body>\
                  \
                  <br>\
                  <br>\
                  <br>\
                  <br>\
                  <div>\
                  <p><center>Donor Information</center></p>\
                  <form method="get" action="/cgi-bin/pythonfile/showinfo1.py">\
                  <tr>Donor Id : <input type="text" name="doid" required=""><br></tr>\
                  <center><input type="submit" name="Login" value="Show"></center><br>\
                </div>\
        </body>')
            
            
            
            
        else:
            print('<head>\
                <title>AdminLogin</title>\
                <style type="text/css">\
                        body{\
                                background-image: linear-gradient(to left, #ffcc66, #ffeecc);\
                \
                        }\
                        div{\
                                 border: 1px solid black;\
                     margin-top: 180px;\
                     margin-bottom: 200px;\
                     margin-right: 250px;\
                     margin-left: 372px;\
                     width: 300px;\
                        }\
                \
                </style>\
                </head>\
                  <body>\
                <div>\
                        <table>\
                        <tr><p><center><h3>Not A Donor,Please use the correct Donor ID and Password.</h3></center></p></tr>	</table>\
                \
        </div>\
        </body>')
        print("</html>")
        db.close()

    
    def donReg():
        #!python
        import cgi #for importing cgi
        import mysql.connector as con
        print("Content-type: text/html\r\n\r\n") #specipy content type
        form=cgi.FieldStorage()
        fname=form.getvalue("fnmae")
        lname=form.getvalue("lnmae")
        emailid=form.getvalue("emailid")
        passwd=form.getvalue("passwd")
        gender=form.getvalue("gender")
        dob=form.getvalue("dob")
        country=form.getvalue("country")
        address=form.getvalue("address")
        bgroup=form.getvalue("bgroup")
        bp=form.getvalue("bp")
        weight=form.getvalue("weight")
        height=form.getvalue("height")
        db=con.connect(host='localhost',user='root',passwd='',database='donoronly')
        sql='INSERT INTO donorid VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(fname,lname,emailid,passwd,gender,dob,country,address,bgroup,bp,weight,height)
        cur=db.cursor()
        cur.execute(sql)
        db.commit()
        print("<html>")
        print('<body bgcolor="#ffdd99">')
        if cur.rowcount>0:
            print("<h1>Thanks For Registration</h1>")
            print("<h1>Please Wait till your Name is called.</h1>")
            print("<h1>We appreciate for your attendance:)</h1>")

        else:
            print("<h1>Sorry Record Not Updated </h1>")
        print("</body>")
        print("</html>")
        db.close()
        

    def showInfo():
        #!python
        import cgi #for importing cgi
        import mysql.connector as con
        db=con.connect(host='localhost',user='root',passwd='',database='donoronly')
        print("Content-type: text/html\r\n\r\n") #specipy content type
        print('<html><body bgcolor="#ffcc66">') #for html code
        cur=db.cursor()
        sql="select * from donorid"
        cur.execute(sql)
        data=cur.fetchall()
        for i in data:
            print('*****************************************************************************************************************<br>')
            print('First Name=',i[0],'<br>')
            print('Last Name=',i[1],'<br>')
            print('Email Id=',i[2],'<br>')
            print('Gender=',i[4],'<br>')
            print('Date Of Birth=',i[5],'<br>')
            print('Country=',i[6],'<br>')
            print('Address=',i[7],'<br>')
            print('Blood Group=',i[8],'<br>')
            print('Blood Pressure=',i[9],'<br>')
            print('Weight=',i[10],'<br>')
            print('Height=',i[11],'<br>')
            print('*****************************************************************************************************************<br>')
            
            
        print("</body>")
        print("</html>")
        db.close()


    def showInfoOne():
        #!python
        import cgi #for importing cgi
        import mysql.connector as con
        db=con.connect(host='localhost',user='root',passwd='',database='donoronly')
        form=cgi.FieldStorage()
        print("Content-type: text/html\r\n\r\n") #specipy content type
        print('<html><body bgcolor="#ffcc66">') #for html code
        cur=db.cursor()
        doid=form.getvalue("doid")
        cur.execute("SELECT * from donorid WHERE fnmae = '%s'" % (doid))
        data=cur.fetchall()
        for i in data:
            print('************************************************************************************************************<br>')
            print('First Name=',i[0],'<br>')
            print('Last Name=',i[1],'<br>')
            print('Email Id=',i[2],'<br>')
            print('Gender=',i[4],'<br>')
            print('Date Of Birth=',i[5],'<br>')
            print('Country=',i[6],'<br>')
            print('Address=',i[7],'<br>')
            print('Blood Group=',i[8],'<br>')
            print('Blood Pressure=',i[9],'<br>')
            print('Weight=',i[10],'<br>')
            print('Height=',i[11],'<br>')
            print('************************************************************************************************************<br>')
            
        print("</body>")
        print("</html>")
        db.close()
        

        
        
        
