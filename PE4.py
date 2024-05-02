name = input ("What is the students name? ")
math = float (input(f"What is {name}'s grade for math? "))
science = float (input(f"What is {name}'s grade for science? "))
history = float (input(f"What is {name}'s grade for history? "))
average = (math + science + history)/3
print (f"{name}'s average is {average:.2f}. ")
f = open("calculated_average.txt", "w")
f.write(f"{name}'s average is {average:.2f}.\n")
f.close()

