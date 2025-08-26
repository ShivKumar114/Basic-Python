# iteration = i ka value.

 #1) - BREAK STATEMENT.- LOOP KO HI EXIT KR DETA HAI .
 # IT INSTRUCT THE PROGRAM TO BREAK THE LOOP AT A GIVEN POINT.

for i in range (100):
  print(i)   # output hoga 1 se 99.


#2)- AGAR HAMKO APNE LOOP KO KISI POINT PAR BREAK KARWANA HAI MEANS WHI PAR STOP KRWA DENA HAI TOH BREAK USE HOTA.
    #EXAMPLE:
for i in range (100):
  if(i==50):
    break   # output 49 tkk hi rhega.
  print(i)  



#2)- CONTINUE STATEMENT - ITERATION KO SKIP KRTA HAI , AUR BADD BAKI KO EXECUTE KRTA HAI .
# CONTINUE IS USED TO STOP THE CURRENT LITERATION OF THE LOOP AND CONTINUE WITHTHE NEXT ONE. IT INSTRUCTS
# THE PROGRAM TO "SKIP THIS PROGRAM".

#EXAMPLE-
for i in range (100):
  if(i==51):
    continue    #output 0 se 99 tk diya sirf 51 ko skip kr diya.
  print(i)


#3)- PASS STATEMENT - NULL STATEMENT IN PYTHON.
# IT INSTRUCTS TO DO NOTHING.

#EXAMPLE-
for i in range(100):
                    #because error kyunki yaha par space khali hai 
                    #issi ko fix krne ke liye pass statement ayya

i = 0 
while(i<55):
  print(i)
  i +=1      # error dega yeh code

  # AB AGAR HAM CHAHTE HAI KI WO SPACE HAM ABHI KAHLI CHOR DE USKE LLIYE PASS STATEMENT HAI.
    #EXAMPLE-
for i in range (100):
  print(i)
pass



i = 0
while(i<55):
  print(i)
  i +=1