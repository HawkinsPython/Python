f = open("users.txt", "r")  
lines = f.read().splitlines()
# Fred,38
# Wilma,33
# Pebbles,6
# Betty,29
# Barney,37
# Bambam,6
# Joe,1
for line in lines:  
    name_str, age_str = line.split(",")
f.close()  
print(f"Data: {len(lines)} lines loaded.")
name = input("Filename for output file: ")
print("Writing report to _____")
# math = float(input(f"What is {name}'s grade for math? "))
# sie = float(input(f"What is {name}'s grade for science? "))
# his = float(input(f"What is {name}'s grade for history? "))

# average = (math + sie + his) / 3

# print(f"{name}'s average is {average:.2f}")

# f = open("caculated_average.txt", "w")
# f.write(f"{name}'s average is {average:.2f}.\n")
# f.close()