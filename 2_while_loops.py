# iteration = i ka value.
# # While loop tb hi execute hota hai jab condition true ho.

# while(condition): 
 
# IN WHILE LOOP THE CONDITION IS CHECKED FIRST . IF IT EVALUATES TO TRUE , THE BODY OF THE LOOP IS EXECUTED 
     # OTHERWISE NOT.

# IF THE LOOP IS ENTERED, THE PROCESS OF (CONDITION CHECK & EXECUTION) IS CONTINUED UNTIL THE CONDITION BECOME
     #  FALSE.
  



# WHILE LOOP EK BARR CONDITION KO CHECK KREGA ANDAR KA CONDITION EXECUTE KREGA , DUBARA CONDITION KO CHECK KREGA.
  #AGAR TRUE HUA TOH FIR CHECK KREGA AUR TBTK KRTA RHEGA JABTK CONDITION FALSE NA HO JAYE.

# EXAMPLE
i = 1

while(i<6):
     print(i)
     i +=1   # i ka value ko 1+ kr do. , without ye likhe output mein sirf 1,1,1,1,1,1, atta jayega.


#Q1)- Write a program to print 1 to 50 using a while loop.
i = 1
 
while(i<51):
   print(i)
   i +=1


#Q2)- Write a program to print the content of a list using while loop.
l = [ 1 , "Harry" , False , "This" , "ROhan" , "Shubham" , " Shiv"]

i = 0

while(i<len(l)):
    print(l[i])
    i +=1