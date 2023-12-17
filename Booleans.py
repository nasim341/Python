##
a = 20
b = 30
if a >= b:
    print("True")
else: 
    print("False")

##Evaluate Values and Variables   
x = "Hello"
y = 20
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