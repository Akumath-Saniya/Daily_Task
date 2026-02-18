#Python program to print your name, qualification, and goal in three separate lines.
print("Akumath Saniya")
print("B.Tech")
print("My goal is to become a good python developer")
#printing a sentence using single quotes and double quotes
print("\'VJ Innovative Software Solutions PVT LTD\'")
print("\"VJ Innovative Software Solutions PVT LTD\"")
#printing the result of 10 + 20 inside the print() function.
print(10+20)
#Creating variables to store my name, age, and city and Printing them in a single output statement.
name="Akumath Saniya"
age=20
city="Madanapalle"
print("name: ",name,"Age: ",age,"city: ",city)
#3 valid variable names
Student="Saniya"
Student_Name="Akumath Saniya"
Student123="Sanu"
print("Valid variable name are: ")
print("Student: ",Student)
print("Student_Name: ",Student_Name)
print("Student123: ",Student123)
#3 invalid variable names
print("Invalid Variable names: ")
#This is invalid because the variable name should not start with numbers
#1Student="Saniya"
#This is invalid because space is a special charector only underscore and dollor are valis in variable names
#Student name="Akumath Saniya"
#This is invalid because only charectors and numbers are allowed in variable names
#@Student="Sanu"
print("1Student Error:"," 1Student=\"Saniya\" SyntaxError: invalid decimal literal")
print("Student name error: ","Student name=\"Akumath Saniya\" SyntaxError: invalid syntax")
print("@Student Error: ","@Student\Sanu\"SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?")
#Reassigning a new value to an existing variable and printing the updated value.
age=21
print("Updated value for age: " ,age)
#Creating one example each for int, float, str, and boolean checking the data type using type function.
integer=5
floating=5.4
string="Saniya"
boolean=50>-50
print(integer)
print(type(integer))
print(floating)
print(type(floating))
print(string)
print(type(string))
print(boolean)
print(type(boolean))
#Converting an integer into a float and printing the result.
con_to_float=float(integer)
print("Coverted an integer to floating point: ",con_to_float)
# a string “PYTHONPROGRAM”
string1="PYTHONPROGRAM"
#Printing the first character using indexing.
print("First value using indexing: ",string1[0])
#Printing the last character using negative indexing.
print("Last charector using negative indexing: ",string1[-1])
#slicing first 6 charectors of String
substring=string1[0:6:1]
print("Sliced first 6 charectors of string(PYTHONPROGRAM: ",substring)


