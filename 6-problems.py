#Q1)- Write a program to find the greatest of four numbers entered by the user.
a1 = int(input("Enter your number: "))
a2 = int(input("Enter your number: "))
a3 = int(input("Enter your number: "))
a4 = int(input("Enter your number: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:",a2)
elif(a3>a2 and a3>a1 and a3>a4):
    print("Greatest number is a3:",a3)
elif(a4>a2 and a4>a3 and a4>a2):
    print("Greatest number is a4:",a4)



#Q2)- Write a program to find out whether a student has passed or failed if it requires a total of 40% and at 
    #  least 33% in each subject to pass.Assume 3 subjects and take marks as an input from the user.
marks1  = int(input("Enter your marks 1: "))
marks2  = int(input("Enter your marks 2: "))
marks3  = int(input("Enter your marks 3: "))

total_percentage = (100*(marks1 + marks2 + marks3))/300   #assuming full marks of per subject 100.

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ):
    print("You are passed" , total_percentage)

else:
    print("You failed , try again" ,   total_percentage)



#Q3)- A spam comment is defined as a text containing following keywords:
     # "Make a lot of money" , "buy now" , "subscribe this" , "click this" . write a program to detect this spam.
p1 ="make a lot of money" 
p2 = "buy now" 
p3 ="subscribe this" 
p4 ="click this"

message = input("Enter your commment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("THIS IS A SPAM MESSAGE")
else:
    print("THIS IS NOT A SPAM MESSAGE.")



#Q4)- Write a program to find whether a given username contain less than 10 characters or not.
username = input("Enter username: ")

if(len(username)<=10):
    print("Success")
else:
    print("Username must be below 10 characters.")




#Q5)- Write a program which finds out whether a given name is present in a list or not.
l = [ "Shiv kumar" , "Rohan Singh" , "Jassi" , "Harry Bhai"]

name = input("Enter your name : ")

if(name in l ):
    print("Your name is in the list.")

else:
    print("Your name is not in the list.")

