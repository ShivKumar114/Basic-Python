# 1)- len function - tells about the length of the function 

# EXAMPLE
name = "SHIV SWARNKAR"
print(len(name))   # YE FUNCTION KI LENGTH KO BATATA HAI 

    

# 2)- string.endswith("kar")- THIS FUNCTION TELLS WHETHER THE VARIABLE STRING ENDS WITH THE STRING "KAR" OR NOT .
    # IF STRING "SHIV SWARNKAR" ' IT RETURNS TRUE FOR "KAR" SINCE "SHIV SWARNKAR" ENDS WITH "KAR"

    # EXAMPLE
Mystring = "SHIV SWARNKAR"
Mystring.endswith("KAR")
print(Mystring.endswith("KAR"))  # OUTPUT TRUE AYYEEGA 
print(Mystring.startswith("shiv"))  # OUTPUT FALSE AYYEGA BECAUSE STRING CAPITAL LETTER MEIN HAI AND YAHA PAR HAM SMALL LETTERS MEIN LIKHE HAI.
print(Mystring.startswith("SHIV"))  # OUTPUT TRUE AYYA



# 3)- string.capitalize - String ke 1st letter ko capitalize krne ke liye program

   # EXAMPLE
name = "shiv swarnkar"
print(name.capitalize())



# 4)- string.find(word) - String ke word ko find krne mein helpm krta hai  
  # ISS WALE MEIN AIISA HAI KI ISKO JO WORD KHHOJNE BOLOGE AGAR ISKO EK BARR WO WORD MIL GYA 
    # USKE BADD YE WORD NHI KHOJEGA EK BARR MILNE KE BADD VALUE DE DEGA JAISE (SHIV SWARNKAR HE IS THE PLAYER )
    #  MEIN ISKO 8 PE R MIL GYA TOH AGGE WALA R KO ISNE INCLUDE NHI KIYA AND OUTPUT 8 DE DIYA

   #EXAMPLE
name = "SHIV SWARNKAR HE IS THE PLAYER"
index = name.find("R")
print(index)



# 5)- string.count("x") - iT COUUNTS THE TOTAL NUMBER OF OCCURRENCES OF ANY CHARACTER

   #EXAMPLE
name =  "SHIV SWARNKAR" 
index = name.count("S")
print(index)



# 6) - string.replace( "old word" , "new word" ) -  IT REPLACE THE OLD WORD WITH NEW WORD IN STRING

  #EXAMPLE
name = "SHIV SWARNKAR"  
index = name.replace("SWARNKAR", "KUMAR")
print(index)



# 7) - string.lower("xyz")  - CONVERTS ALL CHARACTERS TO LOWERCASE

  #EXAMPLE
name = "SHIV SWARNKAR" 
index = name.lower()    #ISME KOI CALL NHI LAGTA MTLB YEH COMMAND PURE STRING KO LOWER CASE MEIN CHANGE KR DETA HAI
print(index)              #ISME BRACKET KE ANDAR KUCH LIKHNA NHI HOTA


# 8) - AGAR KISI SPECIFIC WORD KO REPLACE KRNA HAI LOWER CASE KE SATH TOH HAM USE KRENGE 
   # index = name.replace("old word" , "new word").lower

     #EXAMPLE
name = "SHIV SWARNKAR"
index = name.replace("SWARNKAR" , "KUMAR").lower()
print(index)



# 9) - string.upper() - CONVERTS ALL CHARACTERS TO UPPERCASE
   
    #EXAMPLE
name = "shiv swarnkar"
index = name.upper()    #ISME V VALUE DALNI NHI HOTI HAI ISME V DIRECT SIRF BRACKET LAGANA HOTA HAI 
print(index)               #YE PUURE WORD KO CAPITALIZE KRKE DE DEGA



# 10) - string.title() - capitalizes the first letter of every word of the string
 
  #EXAMPLE
name = "shiv swarnkar he is the player"
index = name.title()
print(index)



# 11) - string.strip() - REMOVE LEADING AND TRAILING WHITESPACES
      # YE STRING KE LEFT AUR RIGHT SE SPACES KO HATATA HAI

  #EXAMPLE
name = ("   SHIV SWARNKAR   ")
index = name.strip()           # SPACES GAPS KO HATATA HAI YEH COMMAND
print(index)



# 12) - string.lstrip() - STRING KE LEFT SIDE KE SPACE KO HATATA HAI 

  #EXAMPLE
name = ("    SHIV SWARNKAR")
print(name)        # ABHI AGAR PRINT KRENGE TOH SPACE KE SATH PRINT HO RHA HAI AGAR LEFT SIDE WALE SPACE KO HATANA HAI TOH


name = ("      SHIV SWARNKAR")
index = name.lstrip()           # AB lstrip() USE KIYE HAI TOH LEFT SIDE KE SPACES HAT GYE HAI
print(index)



# 13) - string.rstrip() - STRING KE LEFT SIDE KE SPACES KO HATA DETA HAI

   #EXAMPLE
name = (" SHIV SWARNKAR             ")
print(name)         # AB AGAR ISKO PRINT KRENGE TOH RIGHT SIDE WALA SPACE V PRINT HOGA ISKO HATANE KE LIYE


name = (" SHIV SWARNKAR              ")
index = name.rstrip()
print(index)



# 14) - string.split() - SPILTS STRINGS INTO LIST  (hamesa string ka list single quote ke andr show hoga) 
         # OUTPUT SQUARE BRACKET KE ANDAAR AYYGEA [ ]
   
    #EXAMPLE
name = "SHIV KUMAR SWARNKAR"   
index = name.split()       # YE STRINGS KE ANDR KE ELEMENT KO SINGLE QUOTE MEIN SHOW KREGA
print(index)

name = "SHIV, KUMAR, SWARNKAR"   
index = name.split(", ")         #YE JO DOUBLE QUOTE KE BADD COMMA LAGAYE HAI YE INDICATE KR RHA KI COMMA KE 
print(index)                   # BADD SE ELEMENT KO LIST KRNA HAI 



# 15) - seprator.join()  - JOINT ELEMENT OF LIST INTO STRING
        
  #EXAMPLE
name = " shiv , kumar, hey , hello "
index = "".join(name)
print(index)



# 16) - string.find(substring) - YE FUNCTION CHECK KRTA HAI KI SUBSTRING PHLI BARR KAHA MIL RHI STRING MEIN

    #EXAMPLE
name = " SHIV , SWARNKAR , HEY , IS THIS ,"
print(name.find("SWARNKAR"))



# 17) - string.index(substring) - YE FUNCTION string.find(substring) KE JAISA HI HAI BUS FARQ ITNA HAI KI 
                                  # AGAR SUBSTRING NHI MILA TOH ERROR AYYEGA SHOW.

   #EXAMPLE
name = " SHIV , SWARNKAR , HEY , IS THIS "
print(name.find("PYTHON"))             #ERROR AYYEGA TOH -1 SHOW HOGA



# 18) - string.count(substring) - YE BATATA HAI KI SUBSTRING KITNI BARR REPEAT HUA HAI STRING MEIN

  #EXAMPLE
name = "LOLLIPOP"
print(name.count("L"))



# 19) - string.endswith() - YE BATATA HAI KI STRING ENDS HOGI YA NHI ISKI VALUE TRUE FALSE MEIN HOGI

  #EXAMPLE
name = ("HE IS THE LOCAL MINISTER")
print(name.endswith("MINISTER"))



# 20) - string.isalpha() - YE STRING MEIN ALPHABAET CHECK KRNE KE LIYE HOTA HAI KI STRING MEIN APHABET HI 
                          # HAI SIRF YA NUMBER V HAI AGAR SIEF ALPHABET RHEGA TOH TRUE DEGA OUTPUT WRNA FALSE.
                           #ISME STRING KE ELEMENT KE BICH SPACE NHI HONA CHAIYE WRNA OUTPUT FALSE AYYEGA
  #EXAMPLE
name = (" HE  IS THE GOD OR NO 123")
# print(name.isalpha())      # output false ayyega kyunki string mein number v hai
 
name = (" HE  IS THE GOD OR NO ")
print(name.isalpha())       #OUTPUT FALSE AYYEGA KYUNKI STRING KE ELEMENT KE ANDAR SPACE HAI 

name = ("EDUCATIONsystemINindiaISaSCAM")
print(name.isalpha())     #OUTPUT TRUE HOGA AB KYUNKI KOI GAP NHI HAI BICH MEIN AB



# 21) - string,isdigit() - TRUE RETURN KREGA AGAR STRING MEIN SIRF NUMBERS HAI (0-9).

  #EXAMPLE
name = (" 02 , 34, 45")
print(name.isdigit())   #OUTPUT FALSE AYYA BECAUSE YAHA PR NUMBERS KKE BICH MEIN DISTANCE HAI

name = ("1234567890")
print(name.isdigit())



# 22) - string.isalnum() - TRUE RETURN KREGA AGAR STRING MEIN SIRF ALPHABETS + NUMBERS HO
                          #KOI SPECIAL CHARACTER ALLOWED NHI  HAI LIKE @#$%^&*

  #EXAMPLE
name = (" #hello1guysare@")
print(name.isalnum())       #OUTPUT FALSE AYYEGA BECAUSE OF SPECIAL CHARACTER

name = ("Hello123")
print(name.isalnum())


# 22) - string.isspace() - TRUE RETURN KREGA AGAR STRING MEIN SIRF SPACES HI HO

  #EXAMPLE
name = ("        1")
print(name.isspace())  #OUTPUT FALSE AYYEGA BECAUSE LAST MEIN 1 LIKHA HUA HAI

name = ("         ")
print(name.isspace())