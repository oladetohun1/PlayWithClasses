#!/usr/bin/python3
"""A person module with name attrbute and a greet method"""
class Person:
    """A person class"""
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello, my name is', self.name)

p = Person('korede')
p.greet()
# The previous 2 lines can also be written as
# Person('Swaroop').greet()