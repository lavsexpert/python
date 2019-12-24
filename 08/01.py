import threading
import time
import random

def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("Worker {} slept {} seconds\n".format(number, sleep))

for i in range(8):
    t = threading.Thread(target=worker, args=(i,))
    t.start()

print("All Treads are in queries\n")


