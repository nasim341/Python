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

############ Change List Items #############

thislist = ["apple", "banana", "cherry"]
thislist[2] = "mango"
print(thislist)

## Change a range item with slice
thislist = ["apple", "banana", "cherry", "orange", "watermelon"]
thislist[2:3] = ["kiwi", "blackcurrant"]
print(thislist)

## Insert Item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "mango")
print(thislist)

################Add List Items############
## Append Items

thislist = ["apple", "banana", "cherry"]
thislist.append("mango")
print(thislist)

## Extend List
thislist = ["apple", "banana", "cherry"]
otherlist = ["mango", "pineapple", "papaya"]
thislist.extend(otherlist)
print(thislist)