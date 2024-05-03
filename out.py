# f = open("{something_very_unique_file.txt}", "w", encoding="utf-8")
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")
# for instructor in instructors:
#     name, yearsExp, age = instructor
#     print(f"The instructor {name} has {yearsExp} years of experience and is {age} years old.")
# output = input("Filename for output file: ")
# f = open("something_very_unique_file.txt", "r")  
# lines = f.read().splitlines()  
# f.close()  
# print(f"Data: {len(lines)} lines loaded.")
# print(f"Writing report to {output}.")
# with open(output, "w") as output:
#     count_old = 0
#     for line in lines:
#         name_str, yearsExp, age_str = line.split(",")
#         name = str(name_str)
#         years = int(yearsExp)
#         age = int(age_str)
#         if age >= 50:
#             count_old += 1
#             output.write(f"{name_str} is retired, having taught for {years}, and is currently {age} years old.\n")
#         else:
#             output.write(f"{name_str} is curently teaching for {years} and is {age_str} years old, .\n")
#     output.write(f"{count_old} are retired.\n")
#     print("Report completed.")


filename = "something_very_unique_file.txt"

# Writing data to file
with open(filename, "w", encoding="utf-8") as f:
    instructors = [["Maria", 7, 38], ["Walton", 22, 47], ["Martin", 18, 52], ["Joel", 3, 28], ["Tate", 5, 67]]
    print("Here is my instructor data:")
    for instructor in instructors:
        name, yearsExp, age = instructor
        print(f"The instructor {name} has {yearsExp} years of experience and is {age} years old.")
        f.write(f"{name},{yearsExp},{age}\n")

# Reading data from file
output = input("Filename for output file: ")
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"Data: {len(lines)} lines loaded.")
    print(f"Writing report to {output}.")
    with open(output, "w") as output_file:
        count_old = 0
        for line in lines:
            name_str, yearsExp, age_str = line.strip().split(",")
            name = str(name_str)
            years = int(yearsExp)
            age = int(age_str)
            if age >= 50:
                count_old += 1
                output_file.write(f"{name_str} is retired, having taught for {years} years, and is currently {age} years old.\n")
            else:
                output_file.write(f"{name_str} is currently teaching for {years} years and is {age_str} years old.\n")
        output_file.write(f"{count_old} are retired.\n")
    print("Report completed.")
