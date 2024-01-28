############ Access Items ############
thislist = ["apple", "banana", "cherry"]
print(thislist[2])

##Negative Indexing
thislist = ["apple", "Banana", "cherry"]
print(thislist[-3])

## Slice Access
thislist = ["apple", "Banana", "Cherry", "Orange", "Melon", "Mango"]
print(thislist[2:4])

##
thislist = ["apple", "Banana", "Cherry", "Orange", "Melon", "Mango"]
print(thislist[:3])

##Negative Indexing with slice
thislist = ["apple", "Banana", "Cherry", "Orange", "Melon", "Mango"]
print(thislist[-3:-2])

## Check Item Exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes,'apple' is in the fruits list")