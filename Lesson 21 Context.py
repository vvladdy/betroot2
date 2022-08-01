import os
import unittest

print('Task 1')
# File Context Manager class
# Create your own class, which can behave like a built-in function `open`.
# Also, you need to extend its functionality with counter and logging. Pay
# special attention to the implementation of `__exit__` method, which has to
# cover all the requirements to context managers.

newfile = 'example.txt'

class ContextOpenFile:

    counter = 0

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        #input('Before change file enter your name: ')
        ContextOpenFile.counter += 1
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'File closed')
        self.file.close()
        print(f'Was opened {ContextOpenFile.counter} times', )


with ContextOpenFile(newfile, 'w') as file:
    file.write('privet')#f"{input('Enter text: ')}")

print(os.path.abspath(__file__))

print('\nTask 2')
# Writing tests for context manager

# Take your implementation of the context manager class from Task 1 and write
# tests for it. Try to cover as many use cases as you can, positive ones when
# a file exists and everything works as designed. And also, write tests when
# your class raises errors or you have errors in the runtime context suite.

class TestContextFile(unittest.TestCase):

    def test_correct_open_file(self):
        self.assertEqual(os.path.exists(newfile), True)

    def test_counter(self):
        count = ContextOpenFile.counter
        self.assertEqual(count, 1)

    def test_file_close(self):
        self.assertEqual(file.closed, True)


if __name__ == '__main__':
    unittest.main()




