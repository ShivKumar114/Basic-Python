# List - Containers to store a set of values of any data type , it can store any datatype
# LIST KE LIYE HAMESA [ ] DOUBLE BRACKET USE HOTA HAI.
# List are mutuable which means we can make changes on strings.
friends = ["Apple","Mango",4,3.21,False,"Akash","Rohan"]
print(friends[0])
friends[0] = "grapes"
print(friends[0])

# LIST SLICING V HOTA HAI JO BILKUL SAME HOTA HAI STRING SLICING SE
friends = ["Apple","Mango",4,3.21,False,"Akash","Rohan"]
print(friends[1:4])

# STRING MEIN STRING SLICING NEW STRING DETA THA BUT LIST SLICING MEIN USI LIST MEIN CHANGE KRKE DETA HAI
# LIST CAN BE INDEXED JUST LIKE A STRING ( STRING KE JAISE HI GINTI HOTA HAI LIST KA)
name = ("SHIV" , "KUMAR" , 12 , 14.5 , True , )
print(name[0:3])