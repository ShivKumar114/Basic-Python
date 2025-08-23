#1)- list.sort() -> ARRANGES LIST IN ASCENDING ORDER
name = [1,4,5,3,6,7,8,9,54,32]
name.sort()
print(name)

#2)- list.reverse() -> REVERSE THE LIST
name = [1,4,5,3,6,7,8,9,54,32]
name.reverse()
print(name)

#3)- list.append(x) -> LIST KE LAST MEIN K0I V CHIZ ADD KRWA SKTE JAISE HAM X LIKHE HA TOH X ADD HOGA
name = [1,4,5,3,6,7,8,9,54,32]
name.append(999)
print(name)

#4)- list.insert(X,Y) -> YE FUNCTION LIST MEIN X WAKE INDEX JAGAH PAR Y KA  VALUE ADD KRTA HAI 
name = [1,4,5,3,6,7,8,9,54,32]
name.insert(2,69)
print(name)

#5)- list.pop(X) -> VALUE DELETE KRTA HAI X INDEX MEIN
name = [1,4,5,3,6,7,8,9,54,32]
name.pop(2)     #output mein 5 nhi ayyega
print(name)

#6)- list.remove(X) -> X KI VALUE LIST MEIN SE DELETE KR DEGA
name = [1,4,5,3,6,7,8,9,54,32]
name.remove(4)   #output mein 4 nhi ayyega
print(name)

#7)- list.extend() -> 2 LIST KO JORTA HAI  (APPEND KE JAISA NHI HAI , YE PURI LIST ADD KRTA HAI ) 
name = [1,4,5,3,6,]
shiv = [7,8,9,54,32]
name.extend(shiv)
print(name)

#8)- list.clear() -> PURI LIST CLEAR KR DETA HAI , output [] deta hai .
name = [1,4,5,3,6,7,8,9,54,32]
name.clear()
print(name)

#9)- list.index() -> ELEMENT  KA INDEX KO RETURN KRTA HAI ( FIRST OCCOURENCE)
name = [1,4,5,3,6,7,8,9,54,32]
print(name.index(5))

#10)- .list.count() -> LIST KE ANDAR KITNE ELEMENTS HAI WO COUNT KRTA HAI.
name = [1,4,5,3,6,7,8,9,54,32,5,6,7,5]
print(name.count(9))

#11)- list.copy() -> LIST KI EK COPY BANATA HAI (orignal list ko affect nhi krta)
a = [1,2,3]
b =a.copy()   # phle a ko copy kiya fir usme 
b.append(4)     # b ka dala hua value insert kr diya a mein and ek new list ban gya jaha last mein 4 v jur gya
print(b)

#12)- sum() -> LIST KE ANDAR KE ELEMENTS KO SUM KRTA HAI 
name = [ 1,2,3,4,5,6]
x = sum(name)
print(x)