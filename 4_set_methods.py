#1)- len(set):  --> TELLS ABOUT THE LENGTH OF THE SET
set = {True,2,3,4,5,6,7,23,8,9,"harry","shiv","32.8",False}
x = len(set)
print(x)


#2)- set.remove(x) --> UPDATES THE SET AND REMOVE X FROM SET
set = {True,2,3,4,5,6,7,23,8,9,"harry","shiv","32.8",False}
set.remove(2)
print(set)


#3)- set.pop(): --> REMOVES AN ARBITARY ELEMENT FROM THE SET AMD RETURN THE ELEMENT REMOVED.
set = {True,2,3,4,5,6,7,23,8,9,"harry","shiv","32.8",False}
x = set.pop()
print(x)


#4)- set.clear()  --> EMPTY THE SET.
set = {True,2,3,4,5,6,7,23,8,9,"harry","shiv","32.8",False}
set.clear()


#5)- set.union({x,y}): --> RETURNS A NEW SET WITH BOTH ITEMS THAT ARE BEING WRITTEN. 
set = {True,2,3,4,5,6,7,23,8,9,"harry","shiv","32.8",False}
x = set.union({99,55})
print(x)


#6)- set.intersection({X,Y}) --> RETURN A SET WHICH CONTAIN ONLY ONE ITEM IN BOTH SETS 
set = {True,2,3,4,5,6,7,23,8,9,"harry","shiv","32.8",False}
x = set.intersection({8,11})    
print(x)     # 8 HAI SETS MEIN ISSLIYE 8 RETURN KR RHA 11 NHI HAI ISSLIIYE NHI KR RHA 11 RETURN.


#7)- set1.union(set2) -->  2 SET KA UNION KRTA HAset.remove(2)
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,0}
x = set1.union(set2)
print(x)

