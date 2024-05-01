def convert_number(number):
    binary = bin(number)[2:]
    octal = oct(number)[2:]
    hexadecimal = hex(number)[2:]
    return binary, octal, hexadecimal
first_integer = int(input("Give me an integer. "))
second_integer = int(input("Give me a second integer. "))
first_binary, first_octal, first_hexadecimal = convert_number(first_integer)
second_binary,second_octal, second_hexadecimal = convert_number(second_integer)
print()
print(f"Your first number in binary is {first_binary}.")
print(f"Your first number in octal is {first_octal}.")
print(f"Your first number in hexadecimal is {first_hexadecimal}.")
print()
print(f"Your second number in binary is {second_binary}.")
print(f"Your second number in octal is {second_octal}.")
print(f"Your second number in hexadecimal is {second_hexadecimal}.")
print()
sum_decimal = first_integer + second_integer
sum_binary, sum_octal, sum_hexadecimal = convert_number(sum_decimal)
print(f"The sum of your two numbers in decimal is {sum_decimal}.")
print(f"The sum of your two numbers in binary is {sum_binary}.")
print(f"The sum of your two numbers in octal is {sum_octal}.")
print(f"The sum of your two numbers in hexadecimal is {sum_hexadecimal}.")
