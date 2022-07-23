print('Task 1')


# School
# Make a class structure in python representing people at school. Make a
# base class called Person, a class called Student, and another one called
# Teacher. Try to find as many methods and attributes as you can, which belong
# to different classes, and keep in mind which are common and which are not.
# For example, the name should be a Person attribute, while salary should
# only  be available to the teacher.


class Person:
    gender = ['Man', 'Woman']

    def __init__(self, firstname, secondname):
        self.firstname = firstname
        self.secondname = secondname

    def getup(self):
        print(f'{self.firstname} {self.secondname} проснулся')

    def breakfast(self):
        print(f'{self.firstname} {self.secondname} завтракает')

    def go_to_active(self):
        print(f'{self.firstname} {self.secondname} вышел из дома')

    def gender_man(self):
        print(self.gender[0])

    def gender_woman(self):
        print(self.gender[1])


class Student(Person):
    def __init__(self, firstname, secondname, age):
        super().__init__(firstname, secondname)
        self.age = age

    def agest(self):
        if 7 <= self.age < 18:
            print(f'{self.firstname} {self.secondname} школьник {self.age} '
                  f'лет')

    def go_to_school(self):
        print(f'{self.firstname} {self.secondname} ходит в школу учиться')

    def do_homework(self):
        print(f'{self.firstname} {self.secondname} делает домашние задания')


class Teacher(Person):
    def __init__(self, firstname, secondname, age):
        super(Teacher, self).__init__(firstname, secondname)
        self.age = age

    def agest(self):
        if 18 <= self.age < 78:
            print(f'{self.firstname} {self.secondname} учитель {self.age} лет')

    def go_to_school(self):
        print(f'{self.firstname} {self.secondname} ходит в школу работать')

    def do_homework(self):
        print(f'{self.firstname} {self.secondname} проверяет домашние задания')

    def salary(self):
        print(f'{self.firstname} {self.secondname} получает зарплату')


def main():
    max = Teacher('Max', 'Ezgov', 25)
    max.getup()
    max.breakfast()
    max.go_to_active()
    max.gender_man()
    print(max.firstname)
    max.go_to_active()
    max.go_to_school()
    max.agest()
    max.do_homework()
    max.salary()


if __name__ == '__main__':
    main()

print('\nTask 2')


# Mathematician
#
# Implement a class Mathematician which is a helper class for doing math
# operations on lists. The class doesn't take any attributes and only has
# methods:
# - square_nums (takes a list of integers and returns the list of squares)
# - remove_positives (takes a list of integers and returns it without positive
#   numbers
# - filter_leaps (takes a list of dates (integers) and removes those that are
#   not 'leap years


class Mathematician:

    def square_nums(self, a):
        outlist = list(map(lambda x: x ** 2, a))
        return outlist

    def remove_positives(self, a):
        outlist = list(filter(lambda x: x < 0, a))
        return outlist

    def filter_leaps(self, a):
        outlist = list(filter(lambda x: x % 4 == 0, a))
        return outlist


def main():
    m = Mathematician()
    print(m.square_nums([7, 11, 5, 4]))
    print(m.remove_positives([26, -11, -8, 13, -90]))
    print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


if __name__ == '__main__':
    main()

print('\nTask 3')


# Product Store
#
# Write a class Product that has three attributes:
# - type
# - name
# - price
# Then create a class ProductStore, which will have some Products and will
# operate with all products in the store. All methods, in case they can’t
# perform its action, should raise ValueError with appropriate error information

# Tips: Use aggregation/composition concepts while implementing the
# ProductStore class. You can also implement additional classes to operate on
# a certain type of product, etc.

# Also, the ProductStore class must have the following methods:
# - add(product, amount) - adds a specified quantity of a single product with
#   a predefined price premium for your store(30 percent)
# - set_discount(identifier, percent, identifier_type=’name’) - adds a
#   discount for all products specified by input identifiers (type or name).
#   discount must be specified in percentage
# - sell_product(product_name, amount) - removes a particular amount of
#   products from the store if available, in other case raises an error. It
#   also increments income if the sell_product method succeeds.
# - get_income() - returns amount of many earned by ProductStore instance.
# - get_all_products() - returns information about all available products in
#   the store.
# - get_product_info(product_name) - returns a tuple with product name and
#   amount of items in the store.


class Product:
    def __init__(self, type_: str, name, price):
        self.type = type_
        self.name = name
        self.price = price
        self.amount = None

    def info(self):
        print(f'Type product: {self.type}\nName: {self.name.split()}\nPrice'
              f': {self.price}')


class ProductStore:
    def __init__(self, *args: Product):
        self.income = 0
        self.all_prod = []
        for product in args:
            self.prod = product
            self.prod.amount = 1
            self.all_prod.append(product)

    def add_product(self, product, amount, price_premium = 0.3):
        if product in self.all_prod:
            product.amount += amount
        else:
            self.all_prod.append(product)
            product.price *= (1 + price_premium)
            product.amount = amount

    def set_discount(self, identifier, percent, identifier_type = 'name'):
        if identifier_type == 'name':
            for prod in self.all_prod:
                if prod.name == identifier:
                    prod.price *= (1 - percent / 100)
        elif identifier_type == 'type':
            for prod in self.all_prod:
                if prod.type == identifier:
                    prod.price *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        for prod in self.all_prod:
            if prod.name == product_name and prod.amount >= amount:
                prod.amount -= amount
                self.income += prod.price * amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        for prod in self.all_prod:
            print(prod.name, prod.type, prod.price, prod.amount)

    def get_prod_info(self, product_name):
        print([prod.__dict__ for prod in self.all_prod if prod.name ==
               product_name])
        # check = ''
        # for prod in self.all_prod:
        #     if prod.name == product_name:
        #         check += 'something'
        #         return prod.name, prod.amount
        # if not check:
        #     raise ValueError('Such prod doe not exist')


p1 = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
p3 = Product('Sport', 'Skirts', 1)

print(p1.info())
s = ProductStore()
s.add_product(p1, 10)
s.add_product(p2, 300)

s.sell_product('Ramen', 10)
print(s.get_all_products())

assert s.get_prod_info('Ramen') == ('Ramen', 290)


print('\nTask 4')

# Create your custom exception named `CustomException`, you can inherit from
# base Exception class, but extend its functionality to log every error
# message to a file named `logs.txt`. Tips: Use __init__ method to extend
# functionality for saving messages to file


class CustomException(Exception):

    def __init__(self, msg):
        super().__init__(msg)
        with open('logs.txt', 'a') as file:
            file.write(msg + '\n')


raise CustomException('Hello world!!!')

