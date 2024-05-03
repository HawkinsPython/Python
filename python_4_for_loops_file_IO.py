f = open("users.txt", "r")
lines = f.read().splitlines()
f.close()
print(f"Data: {len(lines)} lines loaded.")
output = input("Filename for output file: ")
print(f"Writing report to {output}.")
with open(output, "w") as output:
    count_old = 0
    for line in lines:
        name_str, age_str = line.split(",")
        age = int(age_str)
        if age >= 23:
            count_old += 1
            output.write(f"{name_str} is {age} years old, and is old enough to ride a dinosaur.\n")
        else:
            output.write(f"{name_str} is {age} years old, and is NOT old enough to ride a dinosaur.\n")
    output.write(f"{count_old} people are old enough to ride a dinosaur.\n")
print("Report Completed.")