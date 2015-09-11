class FiloList:
    """
    Implements first in last out list class
    """

    lista = []

    def add(self, value):
        """
        Adds a new value to the list and removes the last one
        :param value:
        :return:
        """
        self.lista.insert(0, value)
        self.lista.pop()

    def populate(self, values):
        """
        Populates the list with a give list of elements
        :param values:
        :return:
        """
        self.lista.extend(values)

    def __str__(self):
        return str(self.lista)