## 1
print("My favorite TV show is Law and Order SVU.")
## 2
print("My favorite car is a 1970 Chevy Chevlle")

## 3
print("My favorite")
print("car is") 
print("a 1970") 
print("Chevy")
print("Chevlle")

## 4
print("First step is to prep Keurig")
print("Second step is to grab desired coffee flavor") 
print("Third step is to put coffee cup in Keurig") 
print("Fourth step is to wait until coffe is made")
print("Fifth step is to drink coffee")

## 5
print("Hello World!") 
print("Hello world!")
print("Hello world!")
print("Hello world!")

## 6
name = ("Hello Jane")
print(name)

name1 = ("Hello John")
print(name1)

## 7
print("d: The operation being done is multiplication becasue of the multiplication symbol")

## 8
print("b: Variables are a representaion of a value or set of values")

## 9
print("c: this answer has the correct capitilization and uses parenthesis")

## 10
print("a: the linux command means to copy")

## 11
print("b: That is the multiplication symbol according to math and python")

## 12
print("d: The operation being done is addition, 20 + 7 = 27")

## 13
print("c: this is exponentitation according to python coing language")


## 14
k = input("Please enter your name:")
print(f"Hi {k}")
food = input("Do you like chocolate cake?")
if food == "yes":
    print("oh goody, so do I")
elif food == "no":
    print("That's a shame because I've got some to share")
else:
    print("Please enter a correct answer")
## 15
age1 = input("Please enter your age:") #age1 is the variable beacuse it holds the value for the input
print(f"You are {age1} years old") 
# print("2: the variable holds a string beacuse it is a cumlminantion of data ")

## 16
gift = input("What would you like for your birthday?")
print(f"I would like a {gift} for my birthday as well!")

## 17
print(20**5)       #3200000       The operation was exponential operation"
print("2+6")       #12             The operation being perfored is addition
print("8==8")       #8              The double equal sign is validating 8
print("4=10")    #("syntax error") ("This is an equal operation that cannot take place because 4 does not equal 10")
print("20%80")      #("16")          ("The operation taking place is  the calculation 20 percent of 80")
## 18
num1 = input("Enter a number between 1 and 100:")
num2 = input("Enter a number between 1 and 100:")
num3 = print(f"Number 1 + Number 2 =", num1+num2)
print("The code ran but addition did not occur, the operation concatenate the numbers ")
## 19
num3 = int(input("Enter a number between 1 and 100:"))
num4 = int(input("Enter a number between 1 and 100:"))
print("Number 3 + Number 4=", num3+num4)
print("This function runs successfully and also perfroms the adds the numbers because of the int in front of the inputs")

## 20
a = input("What is your name")
print(f"Hello world and {a}. Today we are going to build a basic calculator that will add, subtract, multiply, and divide!")
y = float (input(f"First Number?"))
z = float (input(f"Second Number?"))
operation = ["add", "subtract", "multiply", "divide"]
d = input(f"Pick an operation?")
if d == "add":
    print(f"The sum is {y + z}")
if d == "subtract":
    print(f"The difference is {y-z}")
if d == "multiply":
    print(f"The product is {y * z}")
if d == "divide":
    print(f"The quotient is {y / z}")
