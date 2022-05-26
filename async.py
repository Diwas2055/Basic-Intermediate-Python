# Importing the asyncio module.
import asyncio

# Creating an event loop.
e_loop = asyncio.get_event_loop()


async def hello():
    print('Searching ...')
    print('CPU is free & not blocking IO....')
    
    # A coroutine that suspends the execution of the current task 
    # and allows other tasks to run.
    await asyncio.sleep(3)
    print('Waiting for task (1) t0 finish ...')
    await asyncio.sleep(2)
    print('Waiting for task (2) t0 finish ...')
    await asyncio.sleep(2)
    print('Tasks executed and queue is empty !')


# hello()

# Running the event loop until the future is done.
e_loop.run_until_complete(hello())
