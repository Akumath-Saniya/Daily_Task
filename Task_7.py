#String Operations 
Name="Akumath Saniya"
substring1=Name[0:4]#First 4 charectors of the Name
substring2=Name[-1:-5:-1]#Last 4 charectors of the Name
substring3=Name[0::2]#Alternate charectors of the Name
Reverse_Name=Name[-1::-1]#Reversing the Name
print("Name: ",Name)
print("First four charectors of my Name: ",substring1)
print("Last four charectors of my Name: ",substring2)
print("Alternate charectors of my Name: ",substring3)
print("Reversing my name using slicing: ",Reverse_Name)
#List Operations
Numbers=[5,10,15,20,25,30,35,40,45,50]
sublist1=Numbers[0:5]#First 5 elements of the list
sublist2=Numbers[-1:-4:]#Last 3 elements using negative indexing
Reverse_Numbers=Numbers[::-1]#reversing the list
mid=len(Numbers)//2
sublist3=Numbers[mid-2:mid+2]#middle 4 elements of the list
print("List: ",Numbers)
print("First 5 elements of the list: ",sublist1)
print("Last 3 elements using Negative slicing: ",sublist2)
print("Middle 4 elements of the list: ",sublist3)
print("Reverse list: ",Reverse_Numbers)
#Tuple Challenge
Tuple=(20,"Laptop",40,"Bag","Charger",55,60,"Chair")
subtuple1=Tuple[-5]#single element of the tuple
subtuple2=Tuple[2:-1]#positive start and negetive stop for tuple
reverse_tuple=Tuple[-1:-8:-1]#reversing the tuple
print("Tuple: ",Tuple)
print("Single element using negative indexing: ",subtuple1)
print("Combination of positive start and negetive stop: ",subtuple2)
print("Reverse of tuple: ",reverse_tuple)
print("Is the tuple a palindrome? ",Tuple==reverse_tuple)

