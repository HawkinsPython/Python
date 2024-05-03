f = open("{something_very_unique_file.txt}", "w", encoding="utf-8")
instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
                  ["Joel", 28, 3], ["Tate", 67, 5]]
print("Here is my instructor data:")
for instructor in instructors:
    name, age, yearsExp = instructor
    print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")
output = input("Filename for output file: ")
f = open("something_very_unique_file.txt", "r")  
lines = f.read().splitlines()  
f.close()  
print(f"Data: {len(lines)} lines loaded.")
print(f"Writing report to {output}.")
# with open(output, "w") as output:
#     count_old = 0
#     for line in lines:
#         name_str, age_str = line.split(",")
#         age = int(age_str)
#         if age >= 30:
#             count_old += 1
#             output.write(f"{name_str} is {age} years old, and is old enough to ride a dinosaur.\n")
#         else:
#             output.write(f"{name_str} is {age} years old, and is NOT old enough to ride a dinosaur.\n")
#     output.write(f"{count_old} people are old enough to ride a dinosaur.\n")
# f = open("something_very_unique_file.txt", "r")  
# lines = f.read().splitlines()  
# f.close()  
# print(f"Data: {len(lines)} lines loaded.")
# lines = f.read().splitlines()
# f.close()
# print(f"Data: {len(lines)} lines loaded.")
# output = input("Filename for output file: ")
# instructors = [["Maria", 38, 7], ["Walton", 47, 22], ["Martin", 52, 18],
#                   ["Joel", 28, 3], ["Tate", 67, 5]]
# print("Here is my instructor data:")
# for name, age, yearsExp in instructors:
#     print(f"The instructor {name} is {age} years old and has {yearsExp} years of experience.")