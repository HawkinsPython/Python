# # # #Test
## 1
print("My favorite food is Grilled salmon.")

## 2
print("It has been such a lovely day today because school was closed and I saw all my friends")
## 3
print("It has been ")
print("such a lovely day today ")
print("because school")
print("was closed and I ")
print("saw all my friends")
## 4
print("To make a cup of tea you must first procure a cup")
print("Then you must full the cup you find with water")
print("After that you've got to get the tea packet and put it in the cup")
print("Then you'll slam that bad boy in the microwave and nuke it for 1:30 seconds")
print("Final step: Enjoy!")
## 5
print("Answer: The first print doesnt have () to box it in. The second print doesnt have quotation marks before and after Hello world!. The third print has Print instead of print which isnt a function. The final print left out the quotation marks after world!.")
## 6
print("Answer: The first one left out the quotation marks after Jane. The second one left out the parenthesis after name.")
## 7
print("b: 8")
## 8
print("a: To store data")
## 9
print("b: input()")
## 10
print("b: change directory")
## 11
print("d: not equal")
## 12
print("d: 15")
## 13
print("d: Exponentiation")
## 14
name = input("Please enter your name: ")
print("Hi {name}")

food = input("Do you like chocolate cake?" )
if food == "yes":
    print("oh goody, so do I")
elif food == "no":
    print("That's a shame because I've got some to share")
else:
    print("please enter a correct answer")
## 15
print("It holds a String, The variable is box1 because its an input the user puts in/can change")
##16
present = input("What would you like for Christmas? ")
print(f"Well whaddya know, I also want a {present} for Christmas!")
## 17
print(f"""
calculation		answer		explanation
40**5			{40**5}		Exponentiation
2+5+3			{2+5+3}		Adds the three numbers
4 == 8			{4==8}		Checking if the first number = the second number
3!=10			{3!=10}		Checking if the first number doesnt = the second number
40%80			{40%80}		"Modulus" or finding the remainder
""")
## 18
num1 = input("Enter a number between 1 and 100")
num2 = input("Enter another number between 1 and 100")

print("Number 1 + Number 2=",num1+num2)

print("it added the numbers as if they were strings instead of integers")
## 19
num1 = int(input("Enter a number between 1 and 100"))
num2 = int(input("Enter another number between 1 and 100"))

print("Number 1 + Number 2=",num1+num2)

print("This time the program added the two numbers as desired because they were correctly labeled as Integers instead of Strings.")
##20
Numby1 = int(input("Gimme a number to convert to binary"))
Numby2 = int(input("Gimme another number to convert to binary"))
Bingle = (Numby1 + Numby2)
print(f"Your first Number in binary is {Numby1:b}, and your second one is {Numby2:b}.")
print(f"The sum of your two Binary numbers is {Bingle:b}")