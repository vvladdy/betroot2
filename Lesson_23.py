class Enumerate:

    def __init__(self, items: list[str], start: int = 0):
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

    NEWLIST: list = []

    def __init__(self, itemstring: str, start: int = 0):
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
