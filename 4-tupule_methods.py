#1)- tuple.count(x) -> TUPULE MEIN X KITNI BARR AYYA HAI WO COUNT KRTA HAI.
name =(1,2,3,True,False,"Shiv",)
x = name.count(2)
print(x)

#2)- tuple.index(x) -> TUPULE MEIN X ELEMENT KA FIRST OCCOURENCE INDEX DETA HAI 
name =(1,2,3,True,False,"Shiv",)
x = name.index(3)
print(x)

#3)- tuple._len_() -> TUPULE KI LENGTH BATATA HAI KI KITNE ELEMENTS HAI.
name =(1,2,3,True,False,"Shiv",)
x = name.__len__()
print(x)

#4)- tuple.max() -> TUPULE MEIN MAXIMUM VALUE KO SHOW KRTA HAI
name = (1,2,3,4,5,6,7,8,9)
print(max(name))

#5)- tuple.min -> TUPULE MEIN MINIMUM VALUE KO SHOW KRTA HAI 
name = (1,2,3,4,5,6,7,8,9)
print(min(name))

#6)- tuple.sum -> TUPULE KE SARE ELEMENTS KO SUM KR DETA HAI 
name = (1,2,3,4,5,6,7,8,9)
print(sum(name))

#7)- sorted() -> TUPULE KE NUMBER KO ASCENDING ORDER MEIN SORT KRTA HAI 
name = (12,4,54,345,24,23,11,54,75,8,55,98)
x = sorted(name)
print(x)

#8) - tuple() -> STRING , LIST ,SET KO TUPULE MEIN CONVERT KR DETA HAI 
name = [1,2,3,True,False,"Shiv"]
x = tuple(name)     # list ko tupule mein change kr diya
print(x)

#9)- # Tuple Unpacking -> JAB EK TUPLLE KE ELEMENTS KO ALAG ALAG VARIABLES MEIN DIRECTLY ASSIGN KR DETE
                         # HAI TB USKO TUPLE UNPACKING BOLTE HAI 
person = ( "Shiv", 19 , "INDIA" )
name, age , country = person
print(name)
print(age)
print(country)

#10) - Tuple concatination -> MULTIPLE TUPLE KO ADD KRTA HAI.
t1 = ( 1,2,3,4)
t2 = ( 4,5,6,7)
t3 = t1+t2
print(t3)