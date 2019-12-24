import asyncio
import datetime
import random

async def sleep_func(num):
    await asyncio.sleep(num)

async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await sleep_func(num+1)

loop = asyncio.get_event_loop()
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
loop.run_forever()
