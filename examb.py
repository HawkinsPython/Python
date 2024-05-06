## 1
print('My favortie hobby is rowing!')

## 2
print('''I am an American Soldier.
I am a warrior and a member of a team.
I serve the people of the United States, and live the Army Values.
I will always place the mission first.
I will never accept defeat.''')

## 3
print('''I am an American Soldier.

I am a warrior and a member of a team.

I serve the people of the United States, and live the Army Values.

I will always place the mission first.

I will never accept defeat.''')

## 4
print('''Hello there user!

I will guide you on how to login.

The first step is to turn on monitor & PC unit.

The following step is to enter the username: usacys

The last step would be to write out the meaning of each letter in the user all together each word capitalized.''')

## 5
print("Hello world!")
print("Hello world!")
print("Hello World!")
print("Hello world!")

## 6
name = "Hello Jane"
print(name)
name = "Hello Jane"
print(name)

## 7
print("B: variable")

## 8
print("B: To represent truth")

## 9
print("B: input()")

## 10
print("B: myVariable = 10")

## 11
print("D: equal")

## 12
print("D: 22")

## 13
print("A: Multiply")

## 14
name = input('Please enter your name: ')
print(f'Hi {name}')

food = input('Do you like chocolate cake? ')

if food == 'yes':
    print('Oh goody, so do I!')
elif food == 'no':
    print('That\'s a shame because I\'ve got some to share.')
else:
    print('Please print a correct answer.')

## 15
myAge = input('Please enter your age: ')
print('You are', myAge, 'years old.')

print("D: String")

## 16
graduationGift = input('What would you like as a gift for graduation? ')
print(f'I would like {graduationGift} for graduation too.')

## 17
print(f'''
calulcation     answer      explanation
80*5            {80*5}      addition of 80 by 5
2+5+3           {2+5+3}     addition of 2 with 5 & 3
12==15          {12==15}    Truth check of 12 being equal to 15
4!=10           {4!=10}     Is False check of 4 not being equal to 10
30==30          {30==30}    Truth check of 30 being equal to 30''')

## 18
num1 = input('Enter a number between 1 and 100: ')
num2 = input('Enter another another number between 1 and 100: ')

print('Number 1 + Number 2= ', num1+num2)
# print('The two inputs only take string, so math operations merely places string together when there's no conversion to int or float.')

## 19
num1 = int(input('Enter a number between 1 and 100: '))
num2 = int(input('Enter another another number between 1 and 100: '))

print('Number 1 + Number 2= ', num1+num2)
# print('The input numbers actually operated with math operations, which means they register as integers instead of string values.')

## 20
import random
chances = ["It is Certain", "Yes", "You may rely on it", "Ask again later", "You've Got to be Kidding", "Reply hazy, try again", "My reply is NO WAY", "My sources say no"]
one_choice = random.choice(chances)
prompt = input('Ask the 8ball a question, or enter \'no\' to quit? ')
while prompt.lower() != 'no':
    print(f'{one_choice}')
    one_choice = random.choice(chances)
    prompt = input('Ask the 8ball a question, or enter \'no\' to quit? ')
print("Have a good day!")