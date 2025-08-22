#Q1)- Write a python program to display a user entered name followed by Good Afternoon using input() function.
name = input("ENTER YOUR NAME; ")
print(f"Good Afternoon {name} ")  

#Q2)- Write a program to fill in a letter template given below with name and date.
letter = '''
        Dear <|Name|>,
        YOU ARE SELECTED
        <|Date|> 
        '''
print(letter.replace("<|Name|>" , "SHIV" ).replace("<|Date|>","24-12-25"))

#Q3)- Write a program to detect double space in a string.
name = (" HE IS GOOD BOY  BUT SAD")
print(name.find("  "))

#Q4)- Write a program to format the following letter using escape sequence characters.
# letter = "Dear Harry, this python course is amazing, Thanks"
letter = "Dear Harry,\n\t this python course is amazing,\nThanks" 
print(letter)
