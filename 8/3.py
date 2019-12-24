from concurrent.futures import ThreadPoolExecutor
from time import sleep

def return5sec(message):
    sleep(5)
    return message

pool = ThreadPoolExecutor(3)

future = pool.submit(return5sec, ("hello"))
print(future.done())
sleep(5)
print(future.done())
print(future.result())
