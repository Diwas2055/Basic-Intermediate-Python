import asyncio

e_loop = asyncio.get_event_loop()


async def hello():
    print('Searching ...')
    print('CPU is free & not blocking IO....')
    await asyncio.sleep(3)
    print('Waiting for task (1) t0 finish ...')
    await asyncio.sleep(2)
    print('Waiting for task (2) t0 finish ...')
    await asyncio.sleep(2)
    print('Tasks executed and queue is empty !')

# hello()

e_loop.run_until_complete(hello())