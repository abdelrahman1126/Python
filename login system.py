print ("sign up")
name1 = input("enter ur name: ")
password1 = input("enter the password: ")
attempts = 0
while attempts < 3:
    print ("sign in")
    name2 = input("enter name: ")
    password2 = input("enter the pass: ")
    if name1 == name2 and password1 == password2:
     print("welcome " +name1)
     break
    else:
     attempts = attempts + 1
     print ("wrong pass")
    if attempts == 3:
     print ("go away hackkkerrrrr")
