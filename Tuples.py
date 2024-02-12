##########Tuples##########
NewTuples = (1,2,3,4,"Hello", False, )
print(NewTuples[-1])

##Slice with Tuples
NewTuples = (1,2,3,4,5,6,7,8)
print(NewTuples[2:4])
 
########### Update Tuples ###########
thisTuple = ("Python", "Programming", "Language")
a = list(thisTuple)
a.append("practice")
thisTuple = tuple(a)
print(thisTuple)

########### Unpack Tuples ############
fruits = ("apple", "banana", "cherry", "Mango")
(a, b, *c) = fruits
print(c)

########## Tuples Loop ############

thisTuple = ("apple", "banana", "cherry", "mango")
for i in thisTuple:
    print(i)

### For Loop
for x in range(len(thisTuple)):
    print (thisTuple[x]) 
 
### While Loop
i = 1
while i < len(thisTuple):
    print(thisTuple[ i])
    i+= 1    

### Join Tuples
num1 = (1,2,3,4,5)
num2 = (6,7,8,9,10)
num3 = num1 + num2
print(num3)

### Multiple Join Tuples
num = (1,2,3,4)
print(num *2)

### Tuples Methods
player = ("Mash","Shakib","Mushi","Taskin", "Shakib")
count = player.count("Shakib")
print(count)