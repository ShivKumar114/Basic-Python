#Q1)- Write a program to print multiplication table of a given number using for loop.
n = int(input("Enter your number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")


#2)- Write a program to greet all the person names stored in the list "l" and which starts with S.
# l = ["Harry","Soham","Sachin","Rahul"].

l = ["Harry","Soham","Sachin","Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")


#3)- Write a program to print multiplication table of a given number usinhg while loop.
n = int(input("Enter your number: "))

i = 1

while(i<11):
    print(f"{n} X {i} = {n*i}")
    i +=1


#4)- Write a program to find whether a given number is prime or not.
n = int(input("Enter your number = "))

i = 1 
for i in range(2,n):
    if(n%1) == 0:
        print("Number is not prime") 
        break
else:
    print("Number is prime")


#5)- Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter your number: "))
i = 0
sum = 0
while(i<=n):    #jo number enter krenge loop utna chalega means 5 likhe toh output ayyega 1+2+3+4+5 = 15
    sum +=i      # 15 issiliye output aa rha bcoz while wale mein i<=n likha hua hai.
    i +=1
print(sum)


#6)- Write a program to calculate the factorial of a given number using for loop.
# 5! = 1 x 2 x 3 x 4 x 5    
n = int(input("Enter your number: "))
product = 1 
for i in range(1,n+1):
    product = product * i
print(f"The factorial of {n} is {product}")


#7)- Write a program to print the following star pattern.
    #  *
#    * * * 
#  * * * * *  for n = 3. 
