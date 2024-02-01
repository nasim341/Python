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