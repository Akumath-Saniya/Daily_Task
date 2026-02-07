#Examples for Types of Integers
decimal=6593
binary=0b10010
octal=0o2304
hexa_decimal=0x95FC
print(decimal)
print(binary)
print(octal)
print(hexa_decimal)
#converting the values between these numbers
print("Conversion from decimal to binary: ",bin(decimal))
print("conversion from decimal to octal: ",oct(decimal))
print("Conversion from decimal to hexa decimal: ",hex(decimal))
print("Conversion from binary to decimal: ",int(binary))
print("Conversion from binary octal decimal: ",oct(binary))
print("Conversion from binary to hexa decimal: ",hex(binary))
print("Conversion from octal to decimal: ",int(octal))
print("Conversion from octal to binary: ",bin(octal))
print("Conversion from octal to hexa decimal: ",hex(octal))
print("Conversion from hexa decimal to decimal: ",int(hexa_decimal))
print("Conversion from hexa decimal to binary: ",bin(hexa_decimal))
print("Conversion from hexa decimal to octal : ",oct(hexa_decimal))
#displaying the type of each value
print("Type of decimal: ",type(decimal))
print("Type of binary: ",type(binary))
print("Type of octal: ",type(octal))
print("Type of hexa decimal: ",type(hexa_decimal))
#Creating multiple floating point variables
float_num1=0.675
float_num2=0.523
#performing arthematic operations using floating point values
print("Addition of floating point values: ",float_num1+float_num2)
print("Subtraction of floating point values: ",float_num1-float_num2)
print("Multiplication of floating point values: ",float_num1*float_num2)
print("Division of floating point values: ",float_num1/float_num2)
#Demonstrating presision behaviour in floating point values
float_add = 0.1 + 0.2
print("0.1 + 0.2 =", float_add)
print("Is 0.1+0.2 exactly 0.3?", float_add == 0.3)
#Creating comples numbers
#using direct notation
complex1=3+5j
#using complex() function
complex2=complex(4,2)
#Accesing and displaying real and imaginary parts of complex numbers
print("Real part of complex1: ",complex1.real,"imaginary part of complex1: ",complex1.imag)
print("Real part of complex2: ",complex2.real,"imaginary part of complex2: ",complex2.imag)
#performing arthematic operations on complex values
print("Addition of complex values: ",complex1+complex2)
print("Subtraction of complex values: ",complex1-complex2)
print("Multiplication of complex values: ",complex1*complex2)
print("Division of complex values: ",complex1/complex2)

