# Question 2
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# https: // www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

num = int(input('Enter a number: '))
if num % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')
