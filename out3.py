filename = input("Filename for output file: ")
# Writing data to file
with open(filename, "w", encoding="utf-8") as f:
    instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18], ["Joel", 28, 3], ["Tate", 67, 5]]
    print("Here is my instructor data:")
    for instructor in instructors:
        name, age, yearsExp = instructor
        print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")
        f.write(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.\n")

# Reading data from file
output = input("Filename for output file: ")
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"Data: {len(lines)} lines loaded.")
    print(f"Writing report to {output}.")
