import threading

print('Task 1')
#
# A shared counter

# Make a class called Counter, and make it a subclass of the Thread class  in
# the Threading module. Make the class have two global variables, one  called
# counter set to 0, and another called rounds set to 100.000.  Now implement
# the run() method, let it include a simple for-loop that iterates  through
# rounds (e.i. 100.000 times) and for each time increments the value  of the
# counter by 1. Create 2 instances of the thread and start them, then  join
# them and check the result of the counter, it should be 200.000, right? Run
# it a couple of times and consider some different reasons why you get  the
# answer that you get.
class Counter(threading.Thread):

    COUNTER = 0
    ROUNDS = 1000000

    def run(self):
        for _ in range(Counter.ROUNDS):
            Counter.COUNTER += 1
        print(Counter.COUNTER)

x = Counter()
x.run()
x.run()

print('*'*80)

print('Task 3')
import requests
from pprint import pprint

# Download all comments from a subreddit of your choice using
# URL: https://api.pushshift.io/reddit/comment/search/ .
#
# As a result, store all comments in chronological order in JSON and dump it
# to a file. For this task use Threads for making requests to reddit API.

URL = 'https://api.pushshift.io/reddit/comment/search/'

resp = requests.get(url=URL)

data = resp.json()

info = data['data']
out, day = [], []

for el in info:
    comment = el['body']
    pprint(comment)
    com = {'comment':
               comment.replace('\n', '').replace('/r','').replace('/u','')}
    out.append(com)
pprint(out)
