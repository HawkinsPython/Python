## 1
print("My favorite hobby is researching mushrooms")

## 2
print("I am an American soldier. I am a warrior and a member of a team. I serve the people of the United States and live the army values. I will always place the mission first. I will never accept defeat")

## 3
print("I am an American soldier\nI am a warrior and a member of a team\nI serve the people of the United States and live the army values\nI will always place the mission first\nI will never accept defeat")

## 4
print("First turn on your computer.\nThen turn on your monitor.\nEnsure that your KVM is displaying the login screen for the commercial computer.\nEnter the username 'usacys'.\nEnter the password 'UnitedStatesArmyCyberSchool'")

## 5
print("Hello world!")
print("Hello world!")
print("Hello world!")
print("Hello world!")
## 6
name = ("Hello Jane")
print(name)
name = ("Hello Jane")
print(name)
## 7
print("b: variable")

## 8
print("d: boolean")

## 9
print("b: input()")

## 10
print("b: myVariable = 10")

## 11
print("d: equal")

## 12
print("c: 12 + 10")

## 13
print("a: multiply")

## 14
name = input("Please enter your name: ")
print(f"Hi {name}")

food = input("Do you like chocolate cake? ")

if food == "yes":
    print("oh goody, so do I")
elif food == "no":
    print("that's a shame because I've got some to share")
else:
    print("Please enter a correct answer")

## 15
myage = (input("Please enter your age: "))
print(f"you are, {myage} years old")

print("4) string")
## 16
graduationgift = input("What would you like for graduation? ")
print(f"I would like {graduationgift} for graduation too!")

## 17
print("""
calculation    answer         explanation
print(80*5)      89    multiplies the two numbers
print(2+5+3)     40    addition of the three numbers 
print(12==15)   False  12 is equal to 15, which is false
print(4!=10)    True   this means 4 is not equal to 10
print(30==30)   True   this means 30 is equal to 30
""")
## 18
num1 = input("Enter a number between 1 and 100: ")
num2 = input("Enter another number between 1 and 100: ")

print("Number 1 + Number 2=",num1 + num2)
print("When I ran the code it asked me for a number then another number and simply displayed both numbers side by side.")

## 19
num1 = int(input("Enter a number between 1 and 100: "))
num2 = int(input("Enter another number between 1 and 100: "))

print("Number 1 + Number 2 =", num1 + num2)
print("When I ran the code it asked me for a number then another number and gave me the sum of both of those numbers.")

## 20
import random
question = input("Ask the 🎱 a question, or enter no to quit? ")
answers = ["It is Certain", "Yes", "You may rely on it", "Ask again later", "You've Got to be Kidding", "Reply hazy, try again", "My reply is NO WAY", "My sources say no"]
while question.lower() not in ["no", "n"]:
    print(random.choice(answers))
    question = input("Ask the 🎱 a question, or enter no to quit? ")
if question.lower() in ["no", "n"]:
    print("Goodbye, See you next time.")
