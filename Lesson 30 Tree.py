class BinaryTree:

    def __init__(self, node):
        self.node = node
        self.right_child = None
        self.left_child = None

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

print(a_node.node)
print(b_node.node)
print(c_node.node)
print(d_node.node)
print(e_node.node)
print(f_node.node)




print('Task 1')


import operator
from typing import Generic, TypeVar, List

from typing import Optional


class BinaryTree:

    def __init__(self, root_obj) -> None:
        self.key: str = str(root_obj)
        self.left_child: Optional[BinaryTree] = None
        self.right_child: Optional[BinaryTree] = None

    def insert_left(self, new_node) -> None:
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node) -> None:
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t: BinaryTree = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj) -> None:
        self.key = obj

    def get_root_val(self) -> str:
        return self.key

    def __repr__(self) -> str:
        return f"BinaryTree: {self.key}"

    def pre_order(self) -> None:
        print(self.key)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self) -> None:
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.key)

    def in_order(self) -> None:
        if self.left_child:
            self.left_child.in_order()
        print(self.get_root_val())
        if self.right_child:
            self.right_child.in_order()


T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens_list = math_exp.split()
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for i in tokens_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i == ')':
            current_tree = stack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                current_tree.set_root_val(int(i))
                parent = stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return tree


def evaluate(parse_tree):
    operates = {'+': operator.add, '-': operator.sub,  '*': operator.mul,
                '/': operator.truediv}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child())+')'
    return s_val


if __name__ == "__main__":
    pt: BinaryTree = build_parse_tree("( ( 10 + 5 ) * 3 )")
    print(evaluate(pt))
    # print()
    # pt.pre_order()
    # print()
    # pt.post_order()
    # print()
    # pt.in_order()
    # print("__")
    print(print_exp(pt))





class BinaryTree:

    def __init__(self, node):
        self.node = node
        self.right_child = None
        self.left_child = None

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

print(a_node.node)
print(b_node.node)
print(c_node.node)
print(d_node.node)
print(e_node.node)
print(f_node.node)



class Expression:
    pass


class Multiplication(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + '*' + str(self.right)

    def eval(self, variable):
        return self.left.eval(variable) * self.right.eval(variable)


class Addition(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + '+' + str(self.right) + ')'

    def eval(self, variable):
        return self.left.eval(variable) + self.right.eval(variable)


class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def eval(self, variable):
        return self.value


class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def eval(self, variable):
        return variable[self.name]


variable = {
    'x': 2,
    'y': 4
}

expression_1 = Multiplication(Constant(3), Addition(Variable('y'), Variable(
    'x')))
expression_2 = Addition(Variable('x'), Multiplication(Constant(3), Variable(
    'y')))

print(expression_1)
print(expression_2)

print(expression_1.eval(variable))
print(expression_2.eval(variable))