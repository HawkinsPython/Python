## 1
print("One of my favorite hobbies is snowboarding")

## 2
print("I'm an American soldier.\n" "I am a warrior and member of a team.\n" "I serve the people of the United States and live the Army values.\n" "I will always place the mission first.\n" "I will never accept defeat.\n")

## 3
print("I'm an American soldier.\n" "I am a warrior and member of a team.\n" "I serve the people of the United States and live the Army values.\n" "I will always place the mission first.\n" "I will never accept defeat.\n")

## 4
print("You must turn on your monitor so that it displays the login screen")
print("Now type 'usacys' for the username")
print("Press enter")
print("Type 'UnitedStatesArmyCyberSchool' for the password")
print("hit enter")

## 5
# 1st
print("Hello world!")
#2nd
print("Hello world!")
#3rd
print("Hello World!")
#4th
print("Hello world!")



## 6
# a 
name = "Hello Jane"
print (name)
# b 
nme = "Hello Jane"
print(nme)
## 7
print("b: Variable")

## 8
print("b: To represent truth")

## 9
print("b: input()")

## 10
print("b: myVariable = 10")
## 11
print("d: equal")

## 12
print("d: 22")

## 13
print("a: multiply")

## 14

name = input("Please enter your name:")
print(f"Hi {name}")

food = input("Do you like chocolate cake?: ")
if food == "yes":
    print("oh goody, so do I")
elif food == "no":
    print("Thats a shame because I've got some to share")
else:
    print("please enter a correct answer")
## 15
myage = input("Please enter your age: ")
print("you are", myage, "years old")
# Part A
print("The variable is 'myage'. I was able to identify that because an input is required from the user to fill it in")
# Part B
print("4:String")
## 16
graduationgift = input("What would you like for graduation?: ")
print(f"I would like {graduationgift} for for Graduation too.")

## 17
print("""
Calculation    Answer           Explanation
80*5           400              Multiplication of two numbers
2+5+3          10               Addition of three numbers
12==15         false            12 does not equal 15 so it is false
4!=10          true             4 does not equal 10 so this is true
30==30         true             30 is equal to 30
""")


## 18
num1 = input("Enter a number between 1 and 100")
num2 = input("Enter another number between 1 and 100")

print("Number 1 + Number 2=", num1 + num2)
print("Since the numbers are being treated as strings and not integers they end up just mashing togther. As an example 20 plus 10 in this code would equal 2010.")
# 19
num1 = int(input("Enter a number between 1 and 100:"))
num2 = int(input("Enter another number between 1 and 100:"))

print("Number 1 + Number 2=", num1+num2)           
print("The numbers get added when I ran the code")
# 20
import random 
things = ["It is Certain", "Yes", "You may rely on it", "Ask again later", "You've Got to be Kidding", "Reply hazy, try again", "My reply is NO WAY", "My sources say no"]
question = input("Ask the 🎱 a question, or enter 'no' to quit: ")
while question.lower() not in ["no", "n"]:
    print(random.choice(things))
    question = input("Ask the 🎱 a question? or enter 'no' to quit: ")
print("Have a good day!")


