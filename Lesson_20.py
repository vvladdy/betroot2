import re

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
#
#
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

#
def main():
    m = Mathematician()
    print(m.square_nums([7, 11, 5, 4]))
    print(m.remove_positives([-11, -8, 13, -90]))
    print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


if __name__ == '__main__':
    main()


# Create a class method named `validate`, which should be called from the
# `__init__` method to validate parameter email, passed to the constructor.
# The logic inside the `validate` method could be to check if the passed
# email  parameter is a valid email string.

class Email:

    def __init__(self, name=''):
        self._name = name

    def email_name(self):
        return f'Your mail is {self.name}'

    def name1(self, value):
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
        if re.match(pattern, value) is not None:
            self._name = value
        else:
            raise ValueError('EMAIL NON VALIDATE')

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
    print(inp.name1('uklk@mail.com'))
    print(inp.email_name())
    inp.name = 'ukl@kmail.coM'
    print(inp.name)

if __name__ == '__main__':
    main()

def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}
