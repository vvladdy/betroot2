print('Task 1')

# Extend UnorderedList

# Implement append, index, pop, insert methods for UnorderedList. Also
# implement a slice method, which will take two parameters `start` and
# `stop`, and return a copy of the list starting at the position and going up
# to but not including the stop position.

class UnoderedList:

    def __init__(self):
        self.unordlist = []
        self._pos = 0

    def addel(self, el):
        return self.unordlist.insert(self._pos, el)

    def indexel(self, el):
        if self.unordlist == []:
            raise ValueError('List is empty')
        if el not in self.unordlist:
            raise ValueError('Element not in List')
        for i in enumerate(self.unordlist):
            if el == i[1]:
                return 'The index of seek element:  {}'.format(i[0])

    def insertel(self, el, pos):
        return self.unordlist.insert(pos, el)

    def popel(self):
        if self.unordlist == []:
            raise ValueError('List is empty')
        else:
            return self.unordlist.pop()

    def __str__(self):
        return 'List {}'.format(self.unordlist)

arr = UnoderedList()
arr.addel(5)
arr.addel('6')
arr.addel('glo')
print(arr.indexel('6'))
print(arr)
arr.insertel('logos', 4)
print(arr)
print(arr.popel())
print(arr)

print('\nUnordered list Lecture')


print('Task 2')
# Implement a stack using a singly linked list.

class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next

    def __str__(self):
        return 'List {}'.format(self._data)

class UnorderedList:

    def __init__(self):
        self._head = Node(None)

    def is_empty(self):
        return self._head is None

    def add(self, item):
        if self._head.get_data():
            temp = Node(item)
            temp.set_next(self._head)
            self._head = temp
        else:
            self._head = Node(item)

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current: Node = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        if self._head.get_data():
            current = self._head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(Node(item))
        else:
            self._head = Node(item)

    def index(self, index):
        current = self._head
        count = 0
        while count < index:
            count += 1
            current = current.get_next()
        return current

    def pop(self, index):
        current = self._head
        previous = None
        count = 0
        while count < index:
            count += 1
            previous = current
            current = current.get_next()
        previous.set_next(current.get_next())

    def incert(self, index, it):
        current = self._head
        previous = None
        count = 0
        while count < index:
            count += 1
            previous = current
            current = current.get_next()
        new = Node(it)
        previous.set_next(new)
        new.set_next(current)

    def slice(self, start, stop):
        current = self._head
        count = 0
        while count < start:
            count += 1
            current = current.get_next()
        slise = UnorderedList()
        slise.add(current)
        while count < stop - 1:
            count += 1
            current = current.get_next()
            slise.append(current)
        return slise

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))

    print(f'List Size: ', my_list.size())
    my_list.remove(54)
    print(f'List Size after remove 1: ', my_list.size())
    my_list.remove(93)
    print(f'List Size after remove 2: ', my_list.size())
    my_list.remove(31)
    print(f'List Size after remove 3: ', my_list.size())
    print(f'Search number : ', my_list.search(93))



print('\nTask 3')
# Implement a queue using a singly linked list.

class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next

class OrderedList:

    def __init__(self):
        self._head = None

    def search(self, item):
        current = self._head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self._head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self._head)
            self._head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def is_empty(self):
        return self._head is None

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

    def __repr__(self):
        representation = "<OrderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = OrderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list.search(93))
    print(my_list.search(100))
    print(my_list)
