print("Hello!")
name = input("please enter your name. ")
print(f"Greetings, {name}.")
print("This is a basic calculator that adds, subtracts, multiplies, and divides.")
a = float(input("Please enter a number. "))
b = float(input("Please enter a second number. "))
c = a + b
d = a - b
e = a * b
f = a / b

print(f"The sum is {c}.")
print(f"The difference is {d}.")
print(f"The product is {e}.")
print(f"The quotient is {f:.4f}.")
print("Now we are going to convert distance from km to m.")
k = float(input("Input a number in kilometers. "))
g = k * 1000
print(f"In meters, that would be {g}m.")
print("Have a good day!")
