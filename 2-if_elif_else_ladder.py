# ELIF ->  elif IN  PYTHON MEANS ELSE IF , YANI AGAR PEHLA if FALSE NIKLA TOH AGLI CONDITION CHECK HOGA 
           # EK PROGRAM MEIN MULTIPLE TIMES elif USE KR SKTE.
    # AGAR if TRUE HO GYA TOH elif CHECK NHI HOGA.

#1)- IF ELIF ELSE LADDER.
a = int(input("Enter your age: "))

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering invalid negative age.")

elif(a==0):
    print("YOU ARE ENTERING 0 WHICH IS NOT A VALID AGE.")

else:
    print("Restricted , Leave this site now. \nYou are below the age of consent.")
    
