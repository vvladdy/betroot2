# TASK 1

# Create a separate asynchronous code to calculate:
# Fibonacci, factorial, squares and cubic for an input number.
# Schedule the execution of this code using asyncio.gather for a list
# of integers from 1 to 10. You need to get four lists of results from
# corresponding functions.

# Rewrite the code to use simple functions to get the same results
# but using a multiprocessing library. Time the execution of both realizations,
# explore the results, what realization is more effective,
# why did you get a result like this.
from math import factorial
import multiprocessing
import asyncio
from time import time
import os

def fibonacci_num_m(num: int):
    print(f'process: {os.getpid()}')
    a, b = 1, 1
    i = 0
    while i < num-2:
        c = a + b
        a = b
        b = c
        i = i + 1
    return f'fibonacci {num} : {b}'

def factor_m(num: int):
    print(f'process: {os.getpid()}')
    return f'factorial {num}:  {factorial(num)}'

def square_m(num: int):
    print(f'process: {os.getpid()}')
    return f'square {num} : {num**2}'

def cube_m(num: int):
    print(f'process: {os.getpid()}')
    return f'cube {num}: {num**3}'

def processing_m(num: int):
    print('Начало расчета: ')
    print(fibonacci_num_m(num))
    print(factor_m(num))
    print(square_m(num))
    print(cube_m(num))


if __name__ == '__main__':
    # tstart = time()
    # pool = multiprocessing.Pool()
    # functions = [fibonacci_num, factor, square, cube]
    # for func in functions:
    #     result = pool.map(func, [100])
    #     print(*result)
    # tstop = time()
    # print(f'Time normal: {tstop-tstart}')

    t1 = time()
    pool = multiprocessing.Pool()
    proc_res = pool.map(processing_m, [10])
    #print(proc_res)
    t2 = time()
    print(f'Time mult: {t2 - t1}')
###########################################################################

async def fibonacci_num(num: int):
    print(f'process: {os.getpid()}')
    a, b = 1, 1
    i = 0
    while i < num-2:
        await asyncio.sleep(0.5)
        c = a + b
        a = b
        b = c
        i = i + 1
    print(f'fibonacci {num} : {b}')


async def factor(num: int):
    await asyncio.sleep(1)
    print(f'process: {os.getpid()}')
    print(f'factorial {num}:  {factorial(num)}')


async def square(num: int):
    await asyncio.sleep(1)
    print(f'process: {os.getpid()}')
    print(f'square {num} : {num**2}')


async def cube(num: int):
    await asyncio.sleep(1)
    print(f'process: {os.getpid()}')
    print(f'cube {num}: {num**3}')


async def processing(num):
    await asyncio.gather(
        fibonacci_num(num),
        factor(num),
        square(num),
        cube(num)
    )
    return 'YES'

async def processing2(num):
    task1 = asyncio.create_task(fibonacci_num(num))
    task2 = asyncio.create_task(factor(num))
    task3 = asyncio.create_task(square(num))
    task4 = asyncio.create_task(cube(num))
    await task1
    await task3
    await task2
    await task4


if __name__ == '__main__':
    tstart = time()
    loop = asyncio.run(processing(10))
    tstop = time()
    #print(loop)
    print(f'Time async: {tstop-tstart}')

    tst = time()
    asyncio.run(processing2(12))
    tend = time()
    print(f'Time async 2: {tend - tst}')

# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')
#     return "YES"
#
#
# if __name__ == "__main__":
#     loop = asyncio.run(main())
#     print(loop)
