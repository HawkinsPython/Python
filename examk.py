## 1
print('My favorite TV show is "Vinland Saga."')

## 2
print('My favorite car is a 1970 Chevy Chevelle.')

## 3
print('My favorite \ncar is \na 1970 \nChevy \nChevelle.')

## 4
print('1. Get ... grinds.')
print('2. pour...maker.')
print('3. Fill ... filter.')
print('4. Place ... mug.')
print('5. Press ... start.')

## 5
#1st
print("Hello world!")

#2nd
print("Hello world!")

#3rd
print("Hello world!")

#4th
print("Hello world!")

## 6
#a
name = "Hello Jane"
print(name)

#b
name = "Hello Jane"
print(name)

## 7
print("D: 12")

## 8
print("B: To store data.")

## 9
print("C: input()")

## 10
print("A: Copy")

## 11
print("B: Multiply")

## 12
print("D: 27")

## 13
print("C: Exponentiation")

## 14
name = input("Please enter your name:")
print("Hi",name)

food = input("Do you like chocolate cake? ")
if food == "yes":
    print("oh goody, so do I")
elif food == "no":
    print("That's a shame because I've got some to share.")
else:
    print("Please enter a correct answer.")
## 15
#A
print("The variable is 'age1' because it is dependent on the data that is entered by the user. It varies from person to person.")

#B
print("2) String")

## 16
gift = input("What would you like for your birthday? ")
print(f'I would  like a/an {gift} for my birthday, too.')

## 17
print("""
code              answer           explanation
print(20**5)      3200000          the 1st number raised to the power of the 2nd number
print(2+6)        8                addition of 2 numbers
print(8==8)       true             comparing the 1st number to the 2nd number, to see if they match
print(4=10)       syntax error     the computer is attempting to assign "10" to 4, error because its not a variable
print(20%80)      20               The remainder of 20 / 80 is 20, as "%" will show the remainder.
""")

## 18
num1 = input("Enter a number between 1 and 100 ")
num2 = input("Enter another number between 1 and 100 ")

print("Number1+Number2=",num1+num2)
print("The code did not specify that the variables need to be integers 'int()', so the computer views them as strings.")
## 19
num1 = int(input("Enter a number between 1 and 100 "))
num2 = int(input("Enter another number between 1 and 100 "))

print("Number1+Number2=",num1+num2)
print("The code ran as expected. Because the variables were specified as integers, the numbers were actually added to eachother.")
## 20

print('Hello world!')
name = input('What is your name? ')
print(f'Greetings, {name}')
print('Today, we are going to build a basic calculator that adds, subtracts, multiplies, and divides.')
num1 = float(input('First number? '))
num2 = float(input('Second number? '))
sum = num1 + num2
dif = num1 - num2
pro = num1 * num2
quo = num1 / num2
print(f'The sum is {sum}')
print(f'The difference is {dif}')
print(f'The product is {pro}')
print(f'The quotient is {quo}')