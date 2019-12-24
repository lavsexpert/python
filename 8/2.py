import multiprocessing
import time
import random

def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("Worker {} slept {} seconds\n".format(number, sleep))

for i in range(4):
    t = multiprocessing.Process(target=worker, args=(i,))
    t.start()

print("All Processes are in queries\n")
