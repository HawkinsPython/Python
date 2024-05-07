import time
from termcolor import colored

def delay_print(s):
    for c in s:
        print(colored(c, "green", "on_black"), end="", flush=True)
        time.sleep(0.01)
    
delay_print("Welcome to the WOPR calculator")

print()

delay_print("Type in a number: ")
a = int(input())
delay_print("Type in a number: ")
b = int(input())
c = bin(a)
d = oct(a)
d2 = hex(a)
print()
e = bin(b)
f = oct(b)
g = hex(b)
h =  a + b
i = bin(h)
j = oct(h)
k = hex(h)
delay_print(f"{a} in binary, {c}")
print()
delay_print(f"{a} in octal, {d}")
print()
delay_print(f"{a} in hexadecimal, {d2}")
print()
delay_print(f"{b} in binary, {e}")
print()
delay_print(f"{b} in octal, {f}")
print()
delay_print(f"{b} in hexadecimal, {g}")
print()
delay_print(f"The sum of {a} and {b} in decimal, {h} ")
print()
delay_print(f"The sum of {a} and {b} in binary, {i} ")
print()
delay_print(f"The sum of {a} and {b} in octal, {j}")
print()
delay_print(f"The sum of {a} and {b} in hexadecimal, {k}")
print()



