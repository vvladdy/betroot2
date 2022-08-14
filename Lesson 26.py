print('Task 1 ')
# Write a program that reads in a sequence of characters and prints them  in
# reverse order, using your implementation of Stack.

def steck_reverse(s: str) -> str:
    arr = []
    arr.extend(s)
    while len(arr) != 0:
        for i in range(len(arr)):
            print(arr[-1])
            arr.pop()
    return 'Stack is Empty'

print(steck_reverse('abcdef'))


print('\nTask 1 var2')
from queue import LifoQueue
my_stack = LifoQueue(maxsize=5)
print(my_stack.qsize())

my_stack.put('x')
my_stack.put('y')
my_stack.put('z')

print("Stack is Full: ", my_stack.full())
print("Size of Stack: ", my_stack.qsize())

print('Elements poped from the my_stack')
print(my_stack.get())
print(my_stack.get())
print(my_stack.get())

print("\nStack is Empty: ", my_stack.empty())


print('\nTask 2')

# Write a program that reads in a sequence of characters, and determines
# whether it's parentheses, braces, and curly brackets are "balanced."

def valid_parentheses(st: str) -> str:
    count, count1, count2 = 0, 0, 0
    for i in st:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    for i in st:
        if i == "[":
            count1 += 1
        elif i == "]":
            count1 -= 1
    for i in st:
        if i == "{":
            count2 += 1
        elif i == "}":
            count2 -= 1
    if count == 0:
        print('() - Balanced')
    else:
        print('() - Not Balanced')
    if count2 == 0:
        print('{} - Balanced')
    else:
        print('{} - Not Balanced')
    if count1 == 0:
        return '[] - Balanced'
    else:
        return '[] - Not Balanced'

print(valid_parentheses('((())))((([[]]{{{}'))

print('\nTask 2 var')
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

def valid_parenth_class(symbol_string):
    stack = Stack()
    for char in symbol_string:
        if char == "(":
            stack.push("(")
        elif char == ")":
            if stack.is_empty():
                return 'Not Balanced'
            else:
                stack.pop()

    if not stack.is_empty():
        return 'Not Balanced'
    else:
        return 'Balanced'

print(valid_parenth_class('()()()()'))


print('\nTask 3')

# Extend the Stack to include a method called get_from_stack that searches
# and returns an element e from a stack. Any other element must remain on
# the stack respecting their order. Consider the case in which the element
# is not found - raise ValueError with proper info Message


class MyStack:

    def __init__(self):
        self.mystack = []

    def push(self, it):
        return self.mystack.append(it)

    def pop(self):
        return self.mystack.pop()

    def seek(self, it):
        for el in range(len(self.mystack)):
            if it == self.mystack[el]:
                print(f'Element <{it}> insist')
                return 'Index position {}'.format(el)
        else:
            raise ValueError('Such element does not exist')

    def __repr__(self):
        return 'Our steck {} quantity of elements {}'.format(self.mystack,
                                                 len(self.mystack))

el = MyStack()
el.push(4)
el.push(5)
el.push(6)
el.push('klo')
print(el.seek(6))

print(el)
el.pop()
print(el)