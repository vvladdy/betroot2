print('Task 1')

# Method overloading.

# Create a base class named Animal with a method called talk and then create
# two subclasses: Dog and Cat, and make their own implementation of the
# method talk be different. For instance, Dog’s can be to print ‘woof woof’,
# while Cat’s can be to print ‘meow’.
# Also, create a simple generic function, which takes as input instance of a
# Cat or Dog classes and performs talk method on input parameter.


class Animal:
    def talk(self):
        return 'Animals talking'


class Dog(Animal):
    def talk(self):
        return 'Woof Woof'


class Cat(Animal):
    def talk(self):
        return 'Meow'


def simple(dog, cat):
    return f'Dog talk: {dog.talk()}\nCat talk: {cat.talk()}'


def maine():
    print(simple(Dog(), Cat()))


if __name__ == '__main__':
    maine()


print('Task 2')

# Library
#
# Write a class structure that implements a library.
# Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author(author must be an instance of Authorclass )
# 3) Author - name, country, birthday, books =[]

# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of
#   Book class and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by
#   the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the
#   specified year

# All 3 classes must have a readable __repr__ and __str__ methods.

# Also, the book class should have a class variable which holds the amount of
# all existing books

class Library:
    books = []
    authors = []
    bookdict = {}

    def __init__(self, name, author, year, quant = 0):
        self.name = name
        self.author = author
        self.year = year
        self.quant = quant
        Library.bookdict[self.name] = Library.bookdict.get(self.name,
                                                           self.author)
        Library.books.append(self.name)
        Library.authors.append(self.author)

    def info(self):
        for book in Library.books:
            print(book)

    def infodict(self):
        print(f'My library are {len(Library.bookdict)} books\n'
              f' {Library.bookdict}')

    def group(self, inf):
        for k, v in Library.bookdict.items():
            if v == inf:
                print(f'Author: {v}\n  book: {k}')
            if k == inf:
                print(f'Author: {v}\n  book: {k}')


class Author(Library):

    def allauthors(self):
        return Library.authors

    def allbooks(self):
        return Library.books

    def authbook(self):
        return dict(list(zip(Library.books, Library.authors)))


def main():
    book = Library('Тарас Бульба', 'Гоголь', 1835)
    book = Library('Черный Лебедь', 'Нассим Талеб', 2003)
    book = Library('Мертвые души', 'Гоголь', 1842)
    book = Library('Захар Беркут', 'Франко', 1882)
    # book.info()
    book.infodict()
    book.group('Гоголь')
    auth = Author
    print(auth.allauthors(book))
    print(auth.allbooks(book))
    print(auth.authbook(book))

if __name__ == '__main__':
    main()




print('\nTask 2 second variant')

class Library1:
    instance = []

    @staticmethod
    def add(name, author):
        Library1.instance.append({'name': name, 'author': author})

    @classmethod
    def duplicate(cls):
        duplicates = {}
        for i in cls.instance:
            name = '{} - {}'.format(i['name'], i['author'])
            count = cls.instance.count(i)
            if count >= 2 and not duplicates.get(name, False):
                duplicates[name] = (i, count)

        return duplicates


data = (('Онегин', 'Пушкин'), ('Мцыри', 'Лермонтов'), ('Мцыри', 'Лермонтов'),
        ('Два капитана', 'Каверин'), ('Два капитана', 'Каверин'),
        ('Два капитана', 'Каверин'))

for i in data:
    Library1.add(*i)

duplicates = Library1.duplicate().values()
print(duplicates, len(duplicates), sep='\n')


print('\nTask 3')

# Fraction
# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку
# для дробів(+, -, /, * ) з належною перевіркою й обробкою помилок. Потрібно
# додати магічні методи для математичних операцій та операції порівняння між
# об'єктами класу Fraction


def commonden(num1, num2):
    while num1 % num2 != 0:
        oldm = num1
        oldn = num2
        num1 = oldn
        num2 = oldm % oldn
    return num2

class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('ZERO DIVISION')
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(f'{self.num}/{self.den}')

    def __add__(self, other):
        newnum = self.num*other.den + \
                     self.den*other.num
        newden = self.den * other.den
        common = commonden(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, other):
        newnum = self.num * other.den - \
                 self.den * other.num
        newden = self.den * other.den
        common = commonden(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

x = Fraction(1, 2)
y = Fraction(1, 4)

print('Сложение:', x+y)
print('Вычитание:', x-y)
print('Умножение:', x*y)
print('Деление:', x/y)
