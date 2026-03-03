#PART1
import math
#integer
integer=500
print(integer)
print(type(integer))
print("Add 500: ",integer+1000)
#floating
floating=89.4
print(floating)
print(type(floating))
floor_float=math.floor(floating)
ceil_float=math.ceil(floating)
print("Floor value: ",floor_float)
print("Ceil value: ",ceil_float)
#complex
complex_num=5 + 3j
complex_real=complex_num.real
print(complex_num)
print(type(complex))
print("Real part: ",complex_real)
#boolean
boolean1=False
boolean2=True
print(boolean1," and ",boolean2)
print(type(boolean1))
print("And operation: ",boolean1 and boolean2)
#string
course="IntermediatePython"
substring=course[12::]
print(course)
print(type(course))
print("Name of course: ",substring)
#list
list1=[10, 20, 30, 40, 50]
ele_of_list=list1[4]
print(list1)
print(type(list1))
print("An element of list: ",ele_of_list)
#tuple
tuple1=(1, 2, 3, 4)
alt_tuple=tuple1[0:4:2]
print(tuple1)
print(type(tuple1))
print("Alterate elements of tuple: ",alt_tuple)
#range
range1=range(1, 15)
print(range1)
print(type(range1))
print(range1[13:0:-1])
#set
set1={11, 22, 33}
total=sum(set1)
print(set1)
print(type(set1))
print("Total of set elements: ",total)
#frozenset
frozenset1=frozenset({7, 8, 9})
print(frozenset1)
print(type(frozenset1))
total1=sum(frozenset1)
print("Total of frozenset elements: ",total1)
#dictionary
dict1={"name": "John", "course": "Python"}
print(dict1)
print(type(dict1))
Name=dict1["name"]
print("Name: ",Name)
#bytes
bytes1=b"Hello"
print(bytes1)
print(type(bytes1))
sub_byte=bytes1[0]
print("H in Hello in bytes: ",sub_byte)
#bytearray
bytearray1=bytearray(5)
print(bytearray1)
print(type(bytearray1))
print("bytearray: ",bytearray1)
#none
None_type=None
print(None_type)
print(type(None_type))
print("None type value is ",None_type)

#list to tuple conversion
list_to_tuple=tuple(list1)
print("list to tuple: ",list_to_tuple)
#tuple to list conversion
tuple_to_list=list(tuple1)
print("tuple to list: ",tuple_to_list)
#set to list conversion
set_to_list=list(set1)
print("set to list: ",set_to_list)

#PART2 
number1=45
binary=bin(number1)
octal=oct(number1)
hexa_decimal=hex(number1)
print("decimal to binary: ",binary)
print("decimal to octal: ",octal)
print("decimal to hexadecimal:",hexa_decimal)

binary_string="0b101101"
octal_string="0o57"
hex_string="0x2A"
#binary string to int conversion
binary_to_int=int(binary_string,2)
#octal string to int conversion
octal_to_int=int(octal_string,8)
#hexa decimal string to int conversion
hexa_to_int=int(hex_string,16)
print("binary to int: ",binary_to_int)
print("octal to int: ",octal_to_int)
print("hexa to int: ",hexa_to_int)

floating1=67.98
#floating to int conversion
float_to_int=int(floating1)
print("float to int: ",float_to_int)
integer1=100
#int to float conversion
int_to_float=float(integer1)
print("int to float: ",int_to_float)
num_string="197223"
#number string to int conversion
print("numeric string to integer: ",int(num_string))

#PART3
#indexing and slicing on a string
string1="DataAnalytics"
print(string1)
length=len(string1)
print("first charector: ",string1[0]) 

print("first five charec: ",string1[0:5])

print("Last Charector: ",string1[length-1])

print("Even index charec: ",string1[2::2])

print("Odd index charec:",string1[1::2])

print("reverse string: ",string1[::-1])

print("slicing from 3 to 10: ",string1[3:11])
#indexing and slicing on a list
list2=[5, 10, 15, 20, 25, 30, 35, 40]

print(list2)

print("first 4 elements: ",list2[0:4])

print("last 3 elements: ",list2[5:8])

print("alternate elements: ",list2[0::2])

print("reverse the list: ",list2[::-1])

#PART4
num1=25
num2=4
#performing arthemetic operations using arthematic operators
print("Number1: ",num1)
print("Number2: ",num2)
print("Addition: ",num1+num2)
print("Subtraction: ",num1-num2)
print("Multiplication: ",num1*num2)
print("Division: ",num1/num2)
print("Floor Division: ",num1//num2)
print("Modulous: ",num1%num2)
print("Exponent: ",num1**num2)
num3=50
print("Number: ",num3)
#performing assignments using all types of assignment operators
num3+=5
print("after Adding 5 in assignment: ",num3)
num3-=3
print("after subtracting 3 in assignment: ",num3)
num3*=2
print("after multiplying by 2 in assignment: ",num3)
num3/=3
print("after dividing by 3 in assignment: ",num3)
num3%=5
print("after modulus by 5 in assignment: ",num3)
num3//=4
print("after floor division by 4 in assigment: ",num3)
num3**=2
print("after exponent by 2 in assigment: ",num3)

#PART5
#performing comparision using comparision operators
print("comparision with double equals 50==50: ",50==50)
print("comparision with double equals 30==50: ",30==50)
print("comparision with not equals 25!=78: ",25!=78)
print("comparision with not equals 50!=50: ",50!=50)
print("comparision with less than 30<50: ",30<50)
print("comparision with less than 50<50: ",50<50)
print("comparision with greater than 50>25: ",50>25)
print("comparision with greater than 50>50: ",50>50)
print("comparision with less than or equals 25<=25: ",25<=25)
print("comparision with less than or equals 50<=26: ",50<=26)
print("comparision with greater than or equals 50>=25: ",50>=25)
print("comparision with greater thanor equals 50>=100: ",50>=100)
#comparing two strings
comp_string1="Learning"
comp_string2="Education"
print("String1: ",comp_string1)
print("String2: ",comp_string2)
print("string1<string2: ",comp_string1<comp_string2)
print("string1== string2: ",comp_string1==comp_string2)
#comparing two lists
comp_list1=["apple","guava","mango"]
comp_list2=["apple","guava","mango"]
print("list1: ",comp_list1)
print("list2: ",comp_list2)
print("List1 equal to list 2: ",comp_list1==comp_list2)
comp_list3=[50,78,20]
comp_list4=[50,6,45]
print("list3: ",comp_list3)
print("list4: ",comp_list4)
print("List3 greater than list 4: ",comp_list3>comp_list4)









