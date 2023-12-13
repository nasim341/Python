#### A variable outside of a function ###

name = "Nasim Ahmed"
def myfunc():
    print("My Name is " + name)
myfunc()


#### A function with global variable ###

university = "BUBT"
def myfunc():
    dept = "CSE"
    print("My Department " + dept)
myfunc()
print("My University Name " + university)    


#####Global variable###########
city = "Khulna"
def myfunc():
    global city
    city = "Dhaka"
myfunc()
print("My Campus Location " + city ) # count variable second declaration