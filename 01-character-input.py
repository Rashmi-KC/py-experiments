# Question 1
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input('Enter your name: ')
current_age = int(input('Ener your age: '))
age = 100 - current_age
print(f'{name}, You\'ll turn 100 years in {age} years old')
