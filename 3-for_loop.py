# iteration = i ka value.
# # FOR LOOP HAM STRING , TUPLE , LIST  SBME LAGA SKTE.

#1)- List 
l = [1,2,3,4,5,6,7,8,9,0]
for i in l:    
    print(i)      #here i means list ke har ek character ko i mein store krna.

#2)- Tuple
t = (9,8,7,6,5,4,3,2,1)
for i in t:     #here i means list ke har ek character ko t mein store krna.
    print(i)

#3)- String
s = "Harry"
for i in s:
    print(i)



#40-  FOR LOOP WITH ELSE.
# Python me for loop ke saath ek else block likh sakte h.
# ye loop tbtk chalta rhega jbtk isko value milta rhega.and jab for loop ko value milna band ho jayega tb wo
#  else loop ko execute kr dega.
# for loop ke sath else ka use tb krte hai jab for loop exhaust ho jata hai .

# EXAMPLE
l = ["A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"]

for item in l:
    print(item)

else:
    print("done")
