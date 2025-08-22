#we can write strings in 3 ways
# single quote ke andar v strings bana skte hai example - 'shiv'
# double quote ke andar v strings bana skte hai exampe - "shiv"
# triple quotes ke andar v strings bana skte hai example - '''shiv'''

# String ek data types hai python mein 

# STRING SLICING - A STRING IN PYTHON CAN BE SLICED FOR GETTING A PART OF THE STRINGS 
# STRING IS IMMUTABLE = MATLAB KI AGAR EK BARR STRING BAN GYI FIR HAM STRING KO CHANGE NHI KR SKTE HAI
# EK EXISTINIG STRING KO CHANGE NHI KR SKTE HAI

# (  Programminng languages mein ginti 0 se shuru hoti hai )
# EXAMPLE = SHIV (S = 0th character ,  H = 1st character , I = 2nd character , V = 4th character ) 

# and agar piche se counting kre toh -1 se ginti shuru hota hai 
# EXAMPLE = SHIV ( V = -1st character , I = -2nd character , H = -3rd character S = -4th character )

# STRING LENGTH = NO OF CHARACTER IN STRING 
# EXAMPLE = "SHIV" = 4 CHARACTERS. 

# KISI V STRING KI LENGTH KO PRINT KRNE KE LIYE 
# len(name) use kr skte 

# IN ORDER TO SLICE A STRING WE USE THE FOLLOWING SYNTAX
# index means value jo input mein dalenge jaise ki name = " shiv kumar" likhe usme s h i v k u m a r sb  characters hai and s ki value 0 h  ki value 1 jisko index bolte
# slicing index = name [ ind_start:ind_end ] 
# ind_start = index_start   ( it will inclued in output )
# ind_end = index_end ( it will not included in output )

# EXAMPLE OF SLICING INDEX OF STRING.
name = "shiv kumar"
print (name[0:3])  # ISME AB 0 SE 3 TK INCLUDE KIYE TOH S H I  OUTPUT AYYA 

# NEGATIVE SLICING
name = "shiv"
print (name[-4:-2])   

# NEGATIVE INDICES KO CORRESPONDING POSITIVE INDICES MEIN CONVERT KRENGE TOH OUTPUT SAME AYYEGA   
# EXAMPLE AGAR 
name = "virat"
print (name[-4:-1])  
print(name[1:4]) 


# AGAR KOI AIISA FUNCTION AYYE JISME ind_start MEIN KOI VALUE NA DIYA HO TOH WAHA PE USKO 0 CONSIDER KIYA JATA HAI.
# EXAMPLE 
name = "shiv"
print(name[:3]) #AB YAHA PAR STARTING INDEX MEIN KUCH NHI HAI MTLB 0 HAI 
# iska outpput ayyega SHI

# AGAR KOI AIISA FUNCTIOIN AYYE JISME ind_end MEIN KOI VALUE NA DIYA HO TB WAHA PE USKO -1 CONSIDER KRTE HAI.
# EXAMPLE
name = "shiv"
print(name[1:]) #AB YAHA PAR END INDEX MEIN KUCH NHI LIKHA MTLB -1 HAI 
# END INDEX MEIN KOI VALUE NHI DIYA GYA HAI TOH OUTPUT BY DEFAULT END OF STRING TK JATA HAI STARTING INDEX VALUE SE.
# iska output ayyega  HIV


# PYTHON STRING SLICING MEIN 
# START INDEX IS INCLUDED
# END INDEX IS NOT INCLUDED
# AUR AGAR END INDEX NHI DIYA TOH BY DEFAULT OUTPUT VALUE END OF STRING TK JATA HAI STARTING VALUE SE.


# SLICING WITH SKIP VALUE

# WE CAN PROVIDE A SKIP VALUE MTLB HAM KOI NORMAL PROGRAM LIKHE USKO FIR SLICING KIYE FIR HAM USME USKE OUTPUT KO SKIP KR SKTE.
# EXAMPLE 
word = "beautiful"
print(word[1:7]) #ISSE SLICING WALA VALUE AYYEGA 
# AB ISME SKIP WALA PART ADD KRNE KE LIYE HAME EK AUR COMMAND LIKHNA HOGA JO KI AIISA DIKHEGA 

# EXAMPLE
word= "beautiful"
print(word[1:7:2]) #ISKA MTLB HOGA KI 1 SE 7 TK SLICING HOGA FIR JO OUTPUT AYYEGA USME SKIP HOGA 2 
# ISKA OPUTPUT HOGA SLICING KE BADD eautif AND AFTER SKIP KRNE KA MTLB HAI KI OUTPUT MEIN PEHLA LETTER e LIKHAYEGA FIR 2 WORD SKIP HOKR JO PEHLA WORD HAI WO V INCLUDE HOGA (e) SKIP WALE GINTI MEIN FIR JO  VALUE HAI WO LIKHAYEGA JAISE u AND FIR i LIKHAYEGA
# iska final output hoga after slicing and after skip EUI

# EXAMPLE 
word = "education"
print(word[0:8:3]) # 0 se 8 tk ka slicing hai and fir us output value mein 3 ka skip hai 
# ISKA FINAL OUTPUT HOGA eci

# EXAMPLE
word = "thunderbolt"
print(word[1:10:4]) # 1 se 10 tk ka slicing hai fir us output mein 4 ka skip value hai
# ISKA FINAL OUTPUT HOGA hel 



# LIST OF STRINGS HAMESA SINGLE QUOTE MEIN SHOW HOTA HAI ,  # OUTPUT SQUARE BRACKET KE ANDAAR AYYGEA [ ]
   
   #EXAMPLE
# AGAR MERE PASS KOI STRING HAI
name = ("SHIV KUMAR SWARNKAR")  # KA TOH STRING KE ANDAR ELEMENTS HAI 'SHIV' 'KUMAR' 'SWARNKAR'
index = name.split()    # agar ham ye command dete hai toph hame string ke andar ke sare elements show ho jayenge 
print(index)                  #  ' ' single quotes ke andar