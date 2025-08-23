#Q1)- Write a program to store seven fruits in a list entered by the user.

fruits = []

f1 = input("Enter Fruit name: ")
fruits.append(f1)
f2 = input("Enter Fruit name: ")
fruits.append(f1)
f3 = input("Enter Fruit name: ")
fruits.append(f1)
f4 = input("Enter Fruit name: ")
fruits.append(f1)
f5 = input("Enter Fruit name: ")
fruits.append(f1)
f6 = input("Enter Fruit name: ")
fruits.append(f1)
f7 = input("Enter Fruit name: ")
fruits.append(f1)



#Q2)- Write a program to accept 6marks of 6 students and display them in a sorted manner.

marks = []

m1 = input("Enter your marks: ")
marks.append(m1)
m2 = input("Enter your marks: ")
marks.append(m2)
m3 = input("Enter your marks: ")
marks.append(m3)
m4 = input("Enter your marks: ")
marks.append(m4)
m5 = input("Enter your marks: ")
marks.append(m5)
m6 = input("Enter your marks: ")
marks.append(m6)

marks.sort()
print(marks)


#Q3)- Check that a tuple type cannot be change in python.

name = [ 1,2,3,4,5,6,7,8]
x = name.append(3)  # append can't be done therefore tuple cannot be change in python
print(x)


#Q4)- Write a program to sum a list of 4 numbers.

name = [1,2,3,4]
x = sum(name)
print(x)


#Q5)- Write a program to count the number of zeros in the followoing tuple.
a = ( 7,0,8,0,0,9)
x = a.count(0)
print(x)