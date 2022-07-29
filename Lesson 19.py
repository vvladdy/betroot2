print('Task 1')

# Create your own implementation of a built-in function enumerate, named
# `with_index`, which takes two parameters: `iterable` and `start`, default
# is  0. Tips: see the documentation for the enumerate function


class Enumerate:

    def __init__(self, items, start=0):
        self.items = items
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.items:
            raise StopIteration
        item = self.items[0]
        self.start += 1
        del self.items[0]
        return f'{self.start} - {item}'


class Enumeratestring:

    NEWLIST = []

    def __init__(self, itemstring, start=0):
        self.itemstring = itemstring
        self.start = start
        for i in itemstring:
            Enumeratestring.NEWLIST.append(i)

    def __iter__(self):
        return self

    def __next__(self):
        if not Enumeratestring.NEWLIST:
            raise StopIteration
        itstring = Enumeratestring.NEWLIST[0]
        self.start += 1
        del Enumeratestring.NEWLIST[0]
        return [self.start, itstring]

def main():

    examplist = Enumerate(['a', 'b', 'c', 'g', '5'], 0)
    print('Iterator list:')
    for i in examplist:
        print(i)

    exampliststring = Enumeratestring('abcde', 0)
    print('Iterator string:')
    for i in exampliststring:
        print(i)


if __name__ == '__main__':
    main()


print('\nTask 2')
#
# Create your own implementation of a built-in function range, named
# in_range(), which takes three parameters: `start`, `end`, and optional
# step.  Tips: See the documentation for `range` function

class IteratorRange:

    def __init__(self, startnum=0, stopnum=0, step=0.0):
        self.startnum = startnum
        self.stopnum = stopnum
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.startnum <= self.stopnum:
            self.startnum = self.startnum + self.step
            return round(self.startnum, 3)
        else:
            raise StopIteration


def main():
    it = IteratorRange(0, 11, 1.7)
    for i in it:
        print(i)


if __name__ == '__main__':
    main()


print('\nTask 3')

# Create your own implementation of an iterable, which could be used inside
# for-in loop. Also, add logic for retrieving elements using square brackets
# syntax.

class String:

    NEWLIST = []

    def __init__(self, itemstring, start=0):
        self.itemstring = itemstring
        self.start = start
        for i in itemstring:
            String.NEWLIST.append(i)

    def __iter__(self):
        return self

    def __next__(self):
        if not String.NEWLIST:
            raise StopIteration
        itstring = String.NEWLIST[0]
        self.start += 1
        del String.NEWLIST[0]
        return [itstring]

def main():
    let = String('Hello, Python')
    for i in let:
        print(i, end=' ')


if __name__ == '__main__':
    main()