import re
print(' Task 1' )
# Create a class method named `validate`, which should be called from the
# `__init__` method to validate parameter email, passed to the constructor.
# The logic inside the `validate` method could be to check if the passed
# email  parameter is a valid email string.


class Email:

    def __init__(self, name=''):
        self._name = name

    def email_name(self):
        return f'Your mail is {self.name}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
        if re.match(pattern, value) is not None:
            self._name = value
        else:
            raise ValueError('EMAIL NON VALIDATE')

def main():
    inp = Email()
    inp.name = 'uklk@mail.com'
    print(inp.email_name())
    inp.name = 'ukl@kmail.coM'
    print(inp.name)

if __name__ == '__main__':
    main()


print('\n Task 2' )
# Implement 2 classes, the first one is the Boss and the second is the Worker.

# Worker has a property 'boss', and its value must be an instance of Boss.

# You can reassign this value, but you should check whether the new value  is
# Boss. Each Boss has a list of his own workers. You should implement a
# method  that allows you to add workers to a Boss. You're not allowed to add
# instances of Boss class to workers list directly via access to attribute,
# use getters and setters instead!


class Worker:
    worknames = []
    workers = {}

    def __init__(self, names, specialities):
        self.names = names
        self.special = specialities
        Worker.worknames.append(self.names)

        Worker.workers[self.names] = Worker.workers.get(self.names,
                                                        self.special)

    def __str__(self):
        return f'{self.names} : {self.special}'

    def info(self):
        return Worker.workers


class Boss:

    def __init__(self, checkname, worker: Worker):
        self._checkname = checkname
        self.worker = worker


    @property
    def checkname(self):
        return self._checkname


    @checkname.setter
    def chechname(self, value):
        for i in Worker.worknames:
            if i == value:
                self._checkname = value
                return f'Worker {value}Exist'
            else:
                return 'Non such worker'


    def info(self):
        for work in Worker.worknames:
            if self._checkname == work:
                return f'Worker {self._checkname} Exist'
            else:
                return f'Non such worker {self._checkname}'

def main():

    worker = Worker('John', 'builder')
    worker = Worker('Kollin', 'ingenier')
    worker = Worker('Ivan', 'helper')
    print(worker.info())
    nick = Boss('John', worker)
    print(nick.info())
    print(nick.checkname)

if __name__ == '__main__':
    main()


print('\n Task 3' )
# Write a class TypeDecorators which has several methods for converting
# results of functions to a specified type (if it's possible):
#
# methods:
# to_int
# to_str
# to_bool
# to_float
# Don't forget to use @wraps


class TypeDecorators:
    def __init__(self, element):
        self.element = element

    @staticmethod
    def to_int(func):
        def wrapper(args):
            if isinstance(int(args), int):
                return int(args)
            else:
                raise ValueError('ERROR')
        return wrapper

    @staticmethod
    def to_bool(func):
        def wrapper(args):
            if args == 'True':
                res = True
            elif args == 'False':
                res = False
            return res
        return wrapper

    @staticmethod
    def to_str(func):
        def wrapper(args):
            if isinstance(args, str):
                return str(args)
            else:
                raise ValueError('ERROR')
        return wrapper

    @staticmethod
    def to_float(func):
        def wrapper(args):
            if isinstance(float(args), float):
                return float(args)
            else:
                raise ValueError('ERROR')
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

@TypeDecorators.to_str
def do_string(string: str):
    return string

@TypeDecorators.to_float
def do_float(string: str):
    return string


do_nothing('25')
do_something('True')
do_string('67')
do_float('67.5')

assert do_nothing('25') == 25

assert do_something('True') is True

assert do_string('67') == '67'

assert do_float('67.5') == 67.5