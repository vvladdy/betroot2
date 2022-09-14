
# TASK 1

# We have the following input list of numbers, some of them are prime.
# You need to create a utility function that takes as input a number and
# returns a bool, whether it is prime or not.

# Use ThreadPoolExecutor and ProcessPoolExecutor to create different
# concurrent implementations for filtering NUMBERS

import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from pprint import  pprint

NUMBERS = [
    2,  # prime
    5,
    6, 7, 9
    # 1099726899285419,
    # 1570341764013157,  # prime
    # 1637027521802551,  # prime
    # 1880450821379411,  # prime
    # 1893530391196711,  # prime
    # 2447109360961063,  # prime
    # 3,  # prime
    # 2772290760589219,  # prime
    # 3033700317376073,  # prime
    # 4350190374376723,
    # 4350190491008389,  # prime
    # 4350190491008390,
    # 4350222956688319,
    # 2447120421950803,
    # 5,  # prime
]

def prime(el):
    count = 0
    for i in range(2, el//2 + 1):
        if (el % i == 0):
            count = count + 1
    if (count <= 0):
        return ("{} - Число простое".format(el))
    else:
        return ("{} - Число не является простым".format(el))

if __name__ == '__main__':
    print('Task 1')
    pool = multiprocessing.Pool()
    res = pool.map(prime, NUMBERS)
    pprint(res)

# TASK 2

import requests

# Download all comments from a subreddit of your choice using URL:
# https://api.pushshift.io/reddit/comment/search/ .
#
# For this task use concurrent and multiprocessing libraries for
# making requests to Reddit API

def make_request(nurl):
    r = requests.get(url=nurl)
    data = r.json()
    info = data['data']
    return info

def search_com(tab: list):
    out = []
    for i in tab:
        comment = i['body']
        com = {'comment':
                   comment.replace('\n', '').replace('/r','').replace('u/','')}
        out.append(com)
    pprint(out)
    #return out

if __name__ == '__main__':
    print('Task 2')
    URLMULT = 'https://api.pushshift.io/reddit/comment/search/'
    p1 = multiprocessing.Process(target=make_request, args=(URLMULT, ))
    p2 = multiprocessing.Process(target=search_com,
                                 args=(make_request(URLMULT), ))
    p1.start()
    p1.join()
    p2.start()
    p2.join()

    print('DONE!')



