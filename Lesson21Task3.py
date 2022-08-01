
print('\nTask 3')

# Pytest fixtures with context manager
#
# Create a simple function, which performs any logic of your choice with text
# data, which it obtains from a file object, passed to this function  (
# def test(file_obj) ).
#
# Create a test case for this function using pytest  library (Full pytest
# documentation).
#
# Create pytest fixture, which uses your implementation of the context
# manager to return a file object, which could be used inside your function.

newfile = 'example.txt'


def fileobj(newf):
    newstr = []
    my_dict = {}
    with open(newf, 'r+') as file:
        out = file.read()
        for i in out:
            newstr.append(i)
        for k in out.strip():
            my_dict[k] = my_dict.get(k, 0)+1
        #print(out.strip().split(' '))
        return len(newstr)#, len(out.strip().split(' ')), my_dict


with open(newfile, 'w') as file:
    file.write(" Hello")
    file.write(' World World ')

print('Количество букв в файле:', fileobj(newfile))


def test_lenght_string():
    assert fileobj(newfile) == 19
