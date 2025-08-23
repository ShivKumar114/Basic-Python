# 1)- world.items():  -> RETURNS A LIST OF (KEY,VALUE)TUPLES.
world = {
          "key": "value", 
          "name": "shiv",     
          "marks":"100",
          "city": "Bhagalpur",
          "list": "80843,60104"
        }
print(world.items())


#2)- world.keys():  -> GIVE THE LIST OF KEYS (LEFT HAND SIDE VALUES).
world = {
          "key": "value", 
          "name": "shiv",     
          "marks":"100",
          "city": "Bhagalpur",
          "list": "80843,60104"
        }
print(world.keys())


#3)- world.values()  -> GIVE THE LIST OF VALUES ( RIGHT HAND SIDE VALUES).
world = {
          "key": "value", 
          "name": "shiv",     
          "marks":"100",
          "city": "Bhagalpur",
          "list": "80843,60104"
        }
print(world.values())


#4)- world.update()  -> DICTIONARY KO UPDATE KR SKTE.
world = {
          "key": "value",
          "name": "shiv",     
          "marks":"100",
          "city": "Bhagalpur",
          "list": "80843,60104"     
        }                           
world.update({"marks":99 })    # AB YAHA PAR HAM APNE MARKS KO DICTIONARY MEIN UPDATE KRKE 99 LIKH RHEH HAI
print(world)

#CASE 1 ---> AGR DICTIONARY MEIN HAM WORD UPDATE KR RHEH HAI AND AIISA WORD UPDATE KR DIYE KEY AND VALUE DONO JO DIC MEIN NHI HAI TOH OUTPUT 
            #  MEIN WO V SHOW HOGA
world = {
          "key": "value", 
          "name": "shiv",     
          "marks":"100",
          "city": "Bhagalpur",
          "list": "80843,60104"
        }
world.update({"marks":99 , "GOD":"HANUMAN JI"})
print(world)


#5) ->  world.get("x") -> DICTIONARY KA EK METHOD HAI JO KEY KA VALUE SAFELY RETURN KRTA HAI
world = {
          "key": "value", 
          "name": "shiv",     
          "marks":"100",
          "city": "Bhagalpur",
          "list": "80843,60104"
        }
print(world.get("key"))
print(world.get("marks"))
print(world.get("city"))
print(world.get("list"))
print(world.get("name"))


#6)- world.items() -  key , value pairs deta hai 
world = {
          "key": "value", 
          "name": "shiv",     
          "marks":"100",
          "city": "Bhagalpur",
          "list": "80843,60104"
        }
world.items()
print(world)


#7)- world.pop() -> KEY VALUE DELETE KRKE VALUE RETURN KREGA
world = {
          "key": "value", 
          "name": "shiv",     
          "marks":"100",
          "city": "Bhagalpur",
          "list": "80843,60104"
        }
world.pop("city")     # CITY KO DELETE KREGA
print(world)


#8)- world.popitem()  -> LAST INSERTED ITEM HATA DETA HAI 
world = {
          "key": "value", 
          "name": "shiv",     
          "marks":"100",
          "city": "Bhagalpur",
          "list": "80843,60104"
        }
world.popitem()
print(world)


#9)- world.clear() -> DICTIONARY KHALI KR DETA HAI , output {} ayyega.
world = {
          "key": "value", 
          "name": "shiv",     
          "marks":"100",
          "city": "Bhagalpur",
          "list": "80843,60104"
        }
world.clear()
print(world)


#10)- world.copy()  -> DICTIONARY KA DUPLICATE SHOW KRTA HAI 
world = {
          "key": "value", 
          "name": "shiv",     
          "marks":"100",
          "city": "Bhagalpur",
          "list": "80843,60104"
        }
world.copy()
print(world)


#11)- dict.fromkeys(keys,value)  --> NAYA DICTIONARY BANATA HAI 
