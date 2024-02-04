"""
this is a multiple line comment
in python scripting langage
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ask(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old ! ")

hatix = Person("Hatix", 19)
hatix.ask()
