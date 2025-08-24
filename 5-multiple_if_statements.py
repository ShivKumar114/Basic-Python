a = int(input("Enter your age: "))

# IF STATEMENT no:1.
if(a%2 == 0):
    print("A is even")

else:
    print("A is odd")
# END OF STATEMENT no:1.

# IF STATEMENT no:2.
if(a>=18):
    print("You are above the age of consent.")
    print("Good for you")

elif(a<0):
    print("You are entering invalid negative age.")

elif(a==0):
    print("YOU ARE ENTERING 0 WHICH IS NOT A VALID AGE.")

else:
    print("Restricted , Leave this site now. \nYou are below the age of consent.")
#END OF IF STATEMENT no:2    
