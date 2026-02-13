#Demostrating DataTypes
#printing value,Type and Unique identifier of int
Integer=5
print("Integer")
print("value: ",Integer)
print("Type: " ,type(Integer))
print("Unique Identifier: ",id(Integer))
print()
#printing value,Type and Unique identifier of float
Floating=8.25
print("Float")
print("value: ",Floating)
print("Type: " ,type(Floating))
print("Unique Identifier: ",id(Floating))
print()
#printing value,Type and Unique identifier of Complex
Complex=5+4j
print("Complex")
print("value: ",Complex)
print("Type: " ,type(Complex))
print("Unique Identifier: ",id(Complex))
print()
#printing value,Type and Unique identifier of List
fruits=["Orange","Apple","Guava","Pomegranate"]
print("List")
print("value: ",fruits)
print("Type: " ,type(fruits))
print("Unique Identifier: ",id(fruits))
#printing value,Type and Unique identifier of float
vowels=("a","e","i","o","u")
print("Tuple")
print("value: ",vowels)
print("Type: " ,type(vowels))
print("Unique Identifier: ",id(vowels))
print()
#printing value,Type and Unique identifier of Set
colors={"Blue","Pink","White","Yellow","Orange"}
print("Set")
print("value: ",colors)
print("Type: " ,type(colors))
print("Unique Identifier: ",id(colors))
print()
#printing value,Type and Unique identifier of frozen set
immutable_colors=frozenset(colors)
print("FrozenSet")
print("value: ",immutable_colors)
print("Type: " ,type(immutable_colors))
print("Unique Identifier: ",id(immutable_colors))
print()