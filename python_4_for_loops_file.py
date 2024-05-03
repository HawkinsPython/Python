f = open("users.txt", "r")  
lines = f.read().splitlines()  
f.close()  
print(f"Data: {len(lines)} lines loaded.")

print("Writing report to _____")
print(f"Filename for output file: ")