f = open("users.txt", "r")
lines = f.read().splitlines()
f.close()
print(f"Data: {len(lines)} lines loaded.")
output_filename = input("Filename for output file: ")
print(f"Writing report to {output_filename}.")
with open(output_filename, "w") as output_file:
    count_old_enough = 0
    for line in lines:
        name_str, age_str = line.split(",")
        age = int(age_str)
        if age >= 23:
            count_old_enough += 1
            output_file.write(f"{name_str} is {age} years old, and is old enough to ride a dinosaur.\n")
        else:
            output_file.write(f"{name_str} is {age} years old, and is NOT old enough to ride a dinosaur.\n")
    output_file.write(f"{count_old_enough} people are old enough to ride a dinosaur.\n")
print("Report Completed.")