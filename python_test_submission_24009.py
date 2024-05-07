## 1
print("My favorite TV show is Star Trek")

## 2
print("My favorite car is a 1970 Chevy Chevelle")

## 3
print("My favorite\ncar is\na 1970\nChevy\nChevelle\n")

## 4
print("Grind some coffee beans.\nPut a coffee filter in the coffee machine.\nNow put the ground beans in the coffee maker.\nLet the hot water flow through the beans.\nEnjoy your hot coffee!")

## 5
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")

## 6
name = "Hello Jane"
print(name)
name = "Hello Jane"
print(name)

## 7
print("D: 12")

## 8
print("B: To store data")

## 9
print("C: input()")

## 10
print("A: copy")

## 11
print("B: Multiply")

## 12
print("D: 27")

## 13
print("C: Exponentiation")

## 14
name = input("please enter your name: ")
print("Hi", name)
food = input("Do you like chocolate cake? ")
if food == "yes":
    print("Oh goody, so do I")
elif food == "no":
    print("That's a shame because I have some to share.")
else:
    print("please enter a correct answer")


## 15
age1 = input("Please enter your age: ")
print("You are", age1, "years old")
print("age1 is the variable, because the input function is storing its data into age1")
print("2: String")

## 16
gift = input("What would you like for your birthday? ")
print(f"I would also like a(n) {gift} for my birthday!")

## 17
print("""
code          answer       explanation
20**5         3200000      20 to the power of 5 
2+6             8          addition of the two numbers
8==8          True         checks if first number is equal to the second number
4=10      syntax Error     Tries to store the value of 10 into a variable of 4, leads to a cannot assign to literal error.
20%80           20         divides first number by the second number, but only gives you the remainder 
""")

## 18
num1 = input("Enter a number between 1 and 100 ")
num2 = input("enter another number between 1 and 100 ")
print("number 1 + number 2 =", num1+num2)
print("The code will combine the variables but will not add them, because you cannot do math with a string")

## 19
num1 = int(input("Enter a number between 1 and 100 "))
num2 = int(input("enter another number between 1 and 100 "))
print("number 1 + number 2 =", num1+num2)
print("The code will add the 2 whole number variables together")


## 20
print("Hello world!")
name = input("What is your name? ")
print(f"Salutations {name}!")
print("Today, We are going to build a basic calculator that adds, subtracts, multiplies, and divides!")
x = float(input("Please give me your first number. "))
y = float(input("Now, give me a second number. "))
add = x + y
subtract = x - y
multiply = x * y
divide = x / y
print(f"The sum of these numbers equal {add}.")
print(f"The difference of these numbers equal {subtract}.")
print(f"The product of these numbers equal {multiply}.")
print(f"The quotient of these numbers equal {divide}.")

