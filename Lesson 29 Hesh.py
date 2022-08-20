import random
print('Task 1')

# Implement binary search using recursion.

def bsearch(alist, begin, end, el):
    if el > alist[-1]:
        return "Such element does not esist"
    if (end < begin):
        return "Such element does not esist"
    else:
        middle = begin + ((end - begin) // 2)

        if alist[middle] > el:
            return bsearch(alist, begin, middle - 1, el)
        elif alist[middle] < el:
            return bsearch(alist, middle + 1, end, el)
        else:
            return middle

alist = [8, 11, 24, 56, 88, 131]
print('Index: ', bsearch(alist, 0, len(alist), 24))
print('Index: ', bsearch(alist, 0, len(alist), 8))

# Бинарный поиск говорит, что список должен быть отсортирован

def binserch(alist, el):
    begin = 0
    end = len(alist) - 1
    while begin <= end:
        middle = ((begin + end) // 2)
        elexist = alist[middle]
        #print(f' mid pos {middle}, el {elexist}, mid el {alist[middle]}')
        if elexist == el:
            return middle
        if elexist > el:
            end = middle - 1
            #print(f'Ind {end} - end')
        else:
            begin = middle + 1
            #print(f'Ind {begin} - begin')
    return 'Such el does non esist'

alist1 = [random.randint(0, 15) for i in range(10)]
#alist1 = [8, 11, 24, 56, 78, 88, 98, 120, 131]
print(alist1)
print(binserch(alist1, 1))


print('Task 2')

# Read about the Fibonacci search and implement it using python.  Explore its
# complexity and compare it to sequential, binary searches.

def fibonacci_search(lst, target):
    start = -1

    f0 = 0
    f1 = 1
    f2 = 1
    while (f2 < len(lst)):
        f0 = f1
        f1 = f2
        f2 = f1 + f0

    while (f2 > 1):
        index = min(start + f0, len(lst) - 1)
        if lst[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif lst[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (lst[len(lst) - 1] == target):
        return len(lst) - 1
    return 'Such el does non esist'

alist = [8, 11, 24, 56, 88, 131]
print('Index Fib Search: ', fibonacci_search(alist, 24))
print('Index Fib Search: ', fibonacci_search(alist, 8))