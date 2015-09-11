# -*- coding: utf-8 -*-
import tuples
import lists



""" operators """

# sum
print "Sum: ", 5 + 4

# subtract
print "Subtract: ", 5 - 3

# multiply
print "Multiply: ", 5 * 12

# division
print "Division: ", 10 / 2

# floor division (only with float)
print "Floor division: ", 10 // 3

# division module
print "Module: ", 10 % 4

# power
print "Squared power: ",  5 ** 2

# operation grouping
print "Operation grouping: ", (10 - 5) * (2 + 3) / 5 - (10 % 5)

# variables
x = 10          # integer
y = 20.34       # float
cool = True     # boolean
text = "hola"   # string

v1, v2 = 34, 45 + 3  #  multiple assignation, expressions are evaluated right hand first



# strings
print 'This is text bewteen simple quotes'
print "You use \\ to escape special characters like \""
print r"Adding 'r' before the string means its a raw string, no character will be escaped with \" or so"
print "--------------------"
print '''\
You can use " " " to write multi line code
Writing the \\ character before the end of the line will prevent the new line
'''
print "--------------------"
print 3 * "pam " + "!, your are dead"
print "Con" "ca" "te" "na" "ted"
print "--------------------"
text = ('you can break long strings '
        'by using parenthesis '
        'and adding multiples strings '
        'separated by comas')
print text

print "--------------------"
word = u"pentameron"
print word
print word[0], word[2], word[-2]  # p n o
print word[2:5]  # nta
print word[:3]
print word[3:]
print len(word)

"""
LISTS
-------
Lists can be written as coma separated values between square brackets.
List may contain items of different types, but usually the items have
all the same type
"""
squares = [1, 4, 9, 16, 25]

"""
Like the strings, lists can be indexed and sliced
"""
squares[0]  # first item of the list
squares[-1]  # last item of the list
squares[-3:]  # slicing returns a NEW list

squares = squares + [36, 49, 64, 81, 100]
squares[1] = 23
squares.append(31)

len(squares)  # return the length of the list

squares[2:5] = [45, 23, 12]  # replace part of the list
squares[5:7] = []  # remove part of the list
squares[:] = []  # wipe the list content

"""
its possible to nest lists
"""

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
coords = [letters, numbers]

print coords[1][0]

"""
if statements
"""
x = 34
if x < 0:
    x = 0
    print "Negative changed to zero"
elif x == 0:
    print "Zero"
else:
    print "More"

"""
for statement
-------------------------
"""
animals = ["cat", "dog", "sparrow", "lizard", "snake"]

for a in animals:
    print a, len(a)

'''
if the iteration needs to modify the list, its recommended to create a copy
to iterate
'''
for a in animals[:]:
    if a == 'sparrow':
        animals.insert(0, 'dragon')
    elif a == 'cat':
        animals.insert(0, 'komodo')
    else:
        animals.insert(0, 'predator')

''' range '''
range(3)  # [0, 1, 2]
range(5, 9)  # [5, 6, 7, 8]
range(5, 15, 3)  # [5, 8, 11, 14]

for a in range(len(animals)):
    print a + 1, animals[a], "(" + str(len(animals[a])) + ")"

'''
break, continue, else
'''
numbers = range(100)
for a in numbers:
    if a % 2 == 0:
        print a, " is a even number"
        continue
    elif a == 45:
        break
    print a, " is an odd number"


"""
while statement
"""
b = 0
while b < 100:
    b += 1


'''
functions
'''


def fib(n):
    """
    the comments are written inside the funcion
    :param n:
    :return:
    """
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a + b
    print ""

fib(334)


def suma(x, y=2):
    return x + y

print suma(3, 4)
print suma(x=13, y=123)


def prueba(argument1, *names, **keywords):

    print argument1

    print "*" * 34

    for a in names:
        print a

    print "*" * 34

    for key in keywords:
        print key, " = ", keywords[key]


prueba("perro", "uno de enero", "dos de febrero", can="cor", lei="post")

""" unpacking arguments """
range(3, 4)

args = [3, 4]
range(*args)

p = lambda n, b: n + b
print p(*[1, 2])