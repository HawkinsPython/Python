## 1
print ("My favortie food is pasta!")

## 2
print ("It has been such a lovely day today because school was closed and i saw all my friends.")

## 3
print("\nIt has been \nsuch a lovely day \ntoday because school \nwas closed and \nI saw all my friends.")
## 4
print("First... cup.")
print("Fill... water.")
print("Place... water.")
print("Let... while.")
print("Enjoy... tea.")


## 5
# 1
print("Hello World!")
# 2
print("Hello World!")
# 3
print("Hello World!")
# 4
print("Hello World!")


## 6
#a
name = "Hello Jane"
print(name)
#b
name = "Hello Jane"
print(name)

## 7
print("B: 8")

## 8
print("A: To store data")

## 9
print("B: input()")

## 10
print("B: change directory")

## 11
print("D: not equal")

## 12
print("D: 15")

## 13
print("D: Exponentiation")

## 14

name=input("Please enter your name ")
print("Hi", name)

food=input("Do you like chocolate cake? ")
if food == "yes":
    print("oh goody, so do I")
elif food == "no":
    print("That's a shame because I've got some to share")
else:
    print("Please enter a correct answer")


## 15
#a
box1=input("Please enter your age: ")
print("you are", box1, "years old")
print("box1 is your variable because you are assigning it a age during your input then it is printing it later.")
#b
print("2: String")


## 16
present = input("What would you like for Christmas? ")
print(f"I had wanted {present} for Christmas too.")

## 17

print("""
calculation     answer     explanation  
40**5          102400000   It is 40 to the 5th power   
2+5+3          10          addition of the three numbers      
4==8           False       Is asking does 4 equal 8
3!=10          True        Is saying 3 does not equal 10
40%80          40          Is saying the remainder of 40/80 
""")



## 18
num1=input("Enter a number between 1 and 100: ")
num2=input("Enter another number between 1 and 100: ")
print("Number 1 + Number 2 =", num1+num2)

print("Instead of adding the numbers together it just printed the numbers together because int wasn't used.")

## 19
num1=int(input("Enter a number between 1 and 100: "))
num2=int(input("Enter another number between 1 and 100: "))
print("Number 1 + Number 2 =", num1+num2)

print("This time it added the numbers because int was used.")


## 20
num1 = int(input("Give me a number: "))
num2 = int(input("Give me another number: "))
bnum1 = bin(num1)
bnum2 = bin(num2)
print(f"Your first number in binary would be {bnum1}")
print(f"Your second number in binary would be {bnum2}")
sum = num1 + num2
bsum = bin(sum)
print(f"The sum of your two numbers in binary would be {bsum}")
