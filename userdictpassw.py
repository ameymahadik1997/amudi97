#Func to check the global dictionary username and password
user={'amaymahadik1997':9769421}
def checked(usname,passw):
    print(usname,' ',passw)
    for key,value in user.items():
        if key==usname and value==passw:
            print('Match')
        else:
            print('Unmatch')

checked('amaymahadik1997',345345)
checked('amaymahadik1997',9769421)
checked('amaymahadik1998',9769421)
