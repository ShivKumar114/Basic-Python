# RANGE FUNCTION 0 SE LEKR (N-1) TK NUMBERS GENERATE KRKE DETA HAI . N = NATURAL NUMBER.
# STEP SIZE -  JAISE STRING SLICING MEIN HOTA THA WAISE RANGE MEIN V HOTA HAI. 
# RANGE FUNCTION  REPRESENTED BY ().
# agar ham range likhte hai RANGE(1,N) isme range jata hai 1 se n-1 tk.

   # EXAMPLE.

# range(start, stop, step)
# start → kahan se shuru karna hai (default = 0)              
# stop → kahan tak chalana hai (ye number include nahi hota)
# step → kitna jump karna hai (default = 1)

# Start (✅ include hota hai)
# Sequence start number se shuru hota hai.

# Stop (❌ include nahi hota hai)
# Sequence stop number tak jaata hai, lekin usse chhota last number tak rukta hai.

# Step (✅ lagta hai har baar jump karne ke liye)
# Har number ke baad step ka jump lagta hai.







#1)- 
range(1 , 10 , 2)
print(range)     # OUTPUT RANGE AYYEGA.

#2)- 
r = range(1 ,10 , 2)
print(r)      # OUTPUT =range(1 ,10 , 2)

#3)- 
r =  range(1 ,10 , 2)
print(list(r))    # list(r) likhne se output slice hokr ayya phle 1 se 10 tk count uske badd 2-2 ka gap chorkar output
# output ayyega (1,3,5,7,9)


#4)- Basic use numbers print krne ke liye
for i in range(5):
    print(i)    #DEFAULT 0 SE SHURU HOTA HAI TOH OUTPUT 0,1,2,3,4, AYYEGA.

#5)-
for i in range(2, 7):
    print(i)
#OUTPUT 2,3,4,5,6


#6)- Reverse Counting(negative step).
for i in range(10, 0, -2):
    print(i)
#OUTPUT 10,8,6,4,2 AYYEGA
