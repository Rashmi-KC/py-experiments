# Question 5
# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 21]

c = []

for i in b:
    if i in a:

        c.append(i)

print(c)
