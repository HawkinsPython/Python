import random

while True:
        question = input("Ask the magic eight ball a question, or enter 'no' to quit? ")
        if question.lower() in ["NO", "No",'no',"N", "n"]:
            print("Goodbye, See you next time.")
            break
        else:
            answers = ["It is Certain", "Yes", "You may rely on it", "Ask again later",  "You've Got to be kidding", "Reply hazy, try again", "My reply is NO WAY", "My sources say no"]
            print(random.choice(answers))


