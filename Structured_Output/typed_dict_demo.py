from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

person_1: Person = {'name':'Alice', 'age': 25}

print(person_1)

person_2: Person = {'name':'Bob', 'age':'35'}

print(person_2)