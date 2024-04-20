# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 09:47:01 2024

@author: ocanh
"""

class Dog:
    # Instance Variables
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    # Method 1
    def get_name(self):
        return self.name

    # Method 2
    def get_breed(self):
        return self.breed

    # Method 3
    def get_age(self):
        return self.age

    # Method 4
    def get_color(self):
        return self.color

    # Method to create a message
    def message(self):
        return f"Hi, my name is {self.get_name()}."

# Create objects (similar to main function)
tuffy = Dog("Tuffy", "Papillon", 5, "white")
max = Dog("Max", "Great Dane", 7, "black")

# Print the message
print(tuffy.message())
print(max.message())
