## Looping Through a String
for a in "bulbul":
    print(a)

## String Length

a = "Hello World"
print(len(a))

## Strings are Arrays
a = "Python"
print(a[5])

## Check Str
a = "Python"
print("Python" is a)

## str
txt = "python"
if "Python" not in txt:
  print("No")

## Slicing
uv = "w3school"
print(uv[2:4])

## Slice From the Start
test = "Python"
print(test[:4])

## Slice To the End
test1 = 'practice'
print(test1[2:])

## Negative Indexing
test2 = "Hello, World"
print(test2[-4:-2])

## String Concatenation
a = "Python"
b = "Practice"
c = a + " " + b
print(c)

##String Format
a = 10
b =  25
c = 10.5
d = "I have {} pieces of item {} for {} Taka."
print(d.format(a, b, c))