def register():
    print("chooses to register")
    db = open("database.txt","r")
    email = input("enter your email use @:")
    password= input("enter your password:")
    password1= input("confirm your password:")
   
    if password != password1:
        print("enter correct password")
        register()
        
    else:
        if len(password)>8   <16:
            print("your password is week,give strong password")
            register()
        elif email in db:
            print("This email is already exists")
            register()
        else:
           db = open("database.txt","a")
           db.write(email+","+password+"\n")
           print("successful")
register()
    


