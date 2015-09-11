lista = [1, 2, 3, 4]
lista2 = [6, 7, 8]
lista.append(5)  # add an element to the list
lista.extend(lista2)  # adds a list at the end of the current one
lista.insert(len(lista), 9)  # adds an element in a given position of the list
lista.remove(3)  # removes the first element of the list which value is X
lista.pop(2)  # removes the element in the index position x (defaul -1)
lista.count(4)  # counts the number of times that the value x appears in the list
lista.reverse()
lista.sort()

del lista[1:3]


import class_fifo_list

ex = FiloList()
ex.populate(range(7))
for a in range(10):
    ex.add(a+65)
    print ex



class Dog:

    def bark(self):
        """
        Dog speaks in its dialect
        :return:
        """
        print "Guau!"


perro = Dog()
perro.bark()
exit()
