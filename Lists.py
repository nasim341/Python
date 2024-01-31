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


#################### Remove List#############

## Remove List
thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)

## Remove Specified index
thislist = ["apple", "mango", "Cherry"]
thislist.pop(0)
print(thislist)

## Remove the last item
thislist = ["apple","mango", "cherry"]
thislist.pop()
print(thislist)

## Delete first item
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

## Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#################Loop Lists##############

## Loop List
thislist = ["apple","banana", "cherry"]
for x in thislist:
    print(x)

##Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

## Using a While Loop
thislist = ["apple", "cherry", "banana"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1

 ##Looping Using List Comprehension{short syntax}
    thislist = ["apple", "banana", "cherry"]
    [print(x) for x in thislist]

############## Sort List ###########
    
thislist = ["orange", "mango","kiwi"]
thislist.sort() 
print(thislist)  

## Numerically Sort

thislist = [40, 50, 30, 70, 80, 60]
thislist.sort()
print(thislist)

## Descending Sort
thislist = ["orange", "banana", "mango","kiwi"]
thislist.sort(reverse=True)
print(thislist)

## Customize Sort
def myfun (n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfun)
print(thislist)

## insensitive Sort
thislist = ["banana", "oranghe", "kiwi", "cherrry"]
thislist.sort(key = str.lower)
print(thislist)