#Assigning a string to a variable
string1="VJ Innovative Software Solutions"
#First 5 characters
first_5=string1[0:6:1]
#Characters from index 2 to 8
two_to_eight=string1[2:9:1]
#Characters from index 2 to 8
every_2=string1[1:int(len(string1)):2]
#First half of the string
first_half=string1[1:int(len(string1)/2):1]
print("String: ",string1)
print("First five charectors of string: ",first_5)
print("Charectors from index 2 to 8: ",two_to_eight)
print("Every second charector from the string: ",every_2)
print("First half of the string: ",first_half)

#Assigning a list of 10 numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
#Extract first 4 elements
first_4=numbers[0:5:1]
#Extract elements from index 3 to 7
three_to_seven=numbers[3:8:1]
#Extract alternate elements
alternate_ele=numbers[0:int(len(numbers)):2]
#Extract middle 3 elements
middle_3=numbers[(int(len(numbers)/2)-1):int((len(numbers)/2)+2):1]
print("List: ",numbers)
print("First Four elements of the list: ",first_4)
print("elements from index 3 to 7 of the list: ",three_to_seven)
print("Alternate elements of the list: ",alternate_ele);
print("middle 3 elements of the list: ",middle_3)


