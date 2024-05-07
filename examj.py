## 1
print("My favorite...The mandalorian")

## 2
print("My favorite...Chevy Chevelle")

## 3
print("Hello World")
print("My favorites")
print("Tv show")
print("The mandolorian")
print("Chevy Chevelle")

## 4
print("Step 1...Pick your coffee")
print("Step 2...place it in")
print("Step 3...Put a cup under the spout")
print("Step 4...Add water to the tank")
print("Step 5...pick your cup size")

## 5
print("Hello world!")
print("Hello world!")
print("Hello World!")
print("Hello world")

## 6
name = "Hello Jane"
print(name)
name = "Hello Jane"
print(name)
## 7
print("D: 12")

## 8
print("B: Store Data")

## 9
print("C: input()")

## 10
print("A: copy")

## 11
print("B: Multiply")

## 12
print("D: 27")

## 13
print("C: Exponent")

## 14
name = input("please enter your name: ")
print("Hi", name)

food = input("Do you like chocolate cake? ")

if food == "yes":
    print("Oh goody, so do I")
elif food == "no":
    print("that's a shame because I have some to share.")
else:
    print("please enter a correct answer")

## 15
age1 = input("Please enter your age: ")
print("You are", age1, "years old")


print("age1 is the variable, because the input function is storing its info into age1")
print("2: String")

## 16
gift = input("What would you like for your birthday? ")
print(f"I also want a(n) {gift} for my birthday!")

## 17
print("""
calculation  answer      explanation
20**5         3200     20 to the power of 5 
2+6            8       addition of the two numbers
8==8          True     checks if first number is equal to the second number
4=10    syntax Error    Tries to store the value of 10 into a variable of 4, leads to a cannot assign to literal error.
20%80           20     divides first number by the second number, but only gives you the remainder 
""")

## 18
num1 = input("Enter a number between 1 and 100 ")
num2 = input("enter another number between 1 and 100 ")
print("number 1 + number 2 =", num1+num2)

print("code will give an error, because you cannot do any math to a string")

## 19
num1 = int(input("Enter a number between 1 and 100 "))
num2 = int(input("enter another number between 1 and 100 "))
print("number 1 + number 2 =", num1+num2)

print("code will add the 2 inputed whole numbers together")

## 20

print("Hello world!")
name = input("What is your name? ")
print(f"Greetings {name}!")
print("This is a basic calculator that adds, subtracts, multiplies, and divides.")
x = float(input("Please input your first number. "))
y = float(input("Please input your second number. "))
sum = x + y
dif = x - y
pro = x * y
quo = x / y
print(f"The sum is {sum}.")
print(f"The difference is {dif}.")
print(f"The product is {pro}.")
print(f"The quotient is {quo}.")
