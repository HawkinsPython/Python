# from dataclasses import dataclass
# @dataclass
# class Dog:
#     name: str
#     age: int
#     breed: str
# d1 = Dog("Tucker", 4, "Cocker Spaniel")
# d2 = Dog("Henry", 8, "Bassett Hound")
# print(d1.name)

# print(f"The dog named {d1.name} is {d1.age} years old. His/Her breed is {d1.breed}.")

# from dataclasses import dataclass
# @dataclass
# class Car:
#     make: str
#     model: str
#     year: int
# c1 = Car("Audi", "A6", 2020)
# c2 = Car("Tesla", "model 3", 2021)
# print(c2.make)
# print(f"The {c2.make} {c2.model} is an electric car. It was built in {c2.year}.")

# from dataclasses import dataclass
# @dataclass
# class Dog:
#     name: str
#     age: int
#     breed: str
# dogs = [
#     Dog("Tucker", 4, "Cocker Spaniel"),
#     Dog("Henry", 8, "Bassett Hound")
#     ]
# print("The first item of our dogs list:")
# print(dogs[0])
# print("The name of the first dog:")
# print(dogs[0].name)

# from dataclasses import dataclass
# @dataclass
# class Instructor:
#     name: str
#     age: int
#     yearsExp: int
# instructors = [
#     Instructor("Maria", 38, 7),
#     Instructor("Walton", 47, 22),
#     Instructor("Martin", 52, 18),
#     Instructor("Joel", 28, 3),
#     Instructor("Tate", 67, 5)
# ]
# print("Here is my instructor data:")
# for person in instructors:
#     print(f"The instructor {person.name} is {person.age} years old and has {person.yearsExp} years of experience.")

# from pydantic import BaseModel

# class Dog(BaseModel):
#     name: str
#     age: int
#     breed: str
   
# d1 = Dog(name="Tucker", age=4, breed="Cocker Spaniel")
# d2 = Dog(name="Henry", age=8, breed="Bassett Hound")

# print(d1.name)

