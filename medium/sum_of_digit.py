# Write a program that calculates the sum of the digits in a given integer.
class Person:
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def greet(self):
        print(f"hello {self.name} and age {self.age}")


alice = Person("alice", 12)

alice.greet()