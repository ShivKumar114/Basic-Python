# ESCAPE SEQUENCE CHARACTERS - ( \n , \t , \; , \\ )

# 1)-  \n  -> REPRESENT NEW LINE
name = ("HELLO\nWORLD")
print(name)


#2)-  \t -> TAB SPACE (horizontal tab ek space ka gap de deta hai 2 word ke bich)
name = ("HELLO\tWORLD")
print(name)


#3)-  \'  -> STRING MEIN SINGLE QUOTE PRINT KRNE KE LIYE
name = ("HE\'s GOOD")
print(name)


#4)- \"  -> STRING MEIN ANDR MEIN DOUBLE QUOTE PRINT KRNE KE LIYE.
name = ("HE IS GOOD BUT \" SHIV IS GREAT\" ")
print(name)


#5)- \r -> REWRITE KRTA HAI OUTPUT KO
name = ("HELLO\rWORLD")   
print(name)     # YAHA PAR HELLO MEIN V 5 WORD H AND WORLD MEIN V TOH WORLD NE HELLO KE 5 WORD KO REPLACE KR DIYA.

name = ("EDUCATION\rPYTHON")
print(name)   # YAHA PAR AB EDUCATION MEIN PYTHON OVERWRITE HOGA MTLB EDUCAT KE JAGAH PYTHON AA JAYEGA
              

#6)- \b -> BACKSPACE DETA HAI INPUT MEIN JAISE HAM SHIV LIKHKE shiv\b toh output hoga shi
name = ("HELLO\bWORLD") 
print(name)             


#7)- \\ xyz\\  -> \xyz\ AIISA OUTPUT DETA HAI
name = ("HELLO\\WORLD\\")
print(name)    #output hoga HELLO \world\


#8)- f  -> ISKA MTLB HAI KI STRING KE ANDAR CURLY BRACES {} USE KRKE VARIABLES , EXPRESSIONS LIKH SKTE
name = input("ENTER YOUR NAME: ")
print(f"Good Afternoon {name}")