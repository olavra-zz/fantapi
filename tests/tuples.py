"""
A tuple consists of a number of values separated by commas
They may be input with or without surrounding parentheses.
It is not possible to assign to the individual items of a tuple
It is possible to create tuples which contain mutable objects, such as lists.
Tuples are immutable, and usually contain an heterogeneous sequence of
elements that are accessed via unpacking or indexing
"""

a = 12, 34, 54, 65,
b = (123, 3123,)
c = ()
d = (1, )
print a, b, c, d

a1, a2, a3, a4 = a
print a1, a2, a3, a4


"""
SETS
"""
frutas = ['oranges', 'apples', 'oranges', 'bananas', 'apples']

frutas_unicas = set(frutas)

print frutas_unicas



exit()
