##
a = 20
b = 30
if a > b:
    print("True")
else: 
    print("False")

##Evaluate Values and Variables   
x = "Hello"
y = '20' 
print(bool(x))
print(bool(y))

##Functions can Return a Boolean
def myFunc():
    return True
if myFunc():
    print("Yes")
else:
    print("No")

## isinstance() function
x = "Python Practice"
print(isinstance(x, str))

## Most Values are True
print (bool ('abc'))
print (bool ("123"))
print (bool (["apple", "cherry", "banana"]))

## Most Values are True
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}))

