#Q1)- Write a program to create a dictionary of hindi words with values as their english translation.provide user
    #   with an option to look out.
words = {
       "madad":"Help",
       "kursi":"Chair",
       "Billi":"Cat",
       "kutta":"Dog"
}
word = input("ENTER THE WORD YOU WANT MEANING OF : ")
print(words[word])


# #Q2)- Write a program to input eight numbers from the user and display the unique numbers(once).
s = set()
n = input("Enter nummber; ")
s.add(int(n))  
n = input("Enter nummber; ")
s.add(int(n)) 
n = input("Enter nummber; ")
s.add(int(n)) 
n = input("Enter nummber; ")
s.add(int(n)) 
n = input("Enter nummber; ")
s.add(int(n)) 
n = input("Enter nummber; ")
s.add(int(n)) 
n = input("Enter nummber; ")
s.add(int(n)) 
n = input("Enter nummber; ")
s.add(int(n)) 
print(s)


# #Q3)- Can we have a set of 18(int) and '18'(str) as a value in it.
s = {18,'18'}
print(s)


# #Q4)- What will be the length of following set s.
s =set()
s.add(20)
s.add(20.0)  # 20.0 and 20 dono same hi consider hoga
s.add('20')  
print(len(s))


# #Q5)- Create an empty dictionary. allow 4 friends to enter their faviourate language as value and use key 
#     #   as their names . Assume thst the name aree unique.
d = {}
name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name:lang})


# #Q6)- Can we change the values inside a list which is contained in set S ?
s = {8,7,12,"Harry", [1,2]}
# LIST IS NOT HASABLE WE CAN'T CHANGE THE VALUES