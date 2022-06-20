import asyncio

async def count():
    """
    It counts from 1 to 10, printing each number to the console
    """
    print("One")
   # Telling the interpreter to pause the execution of the function until the awaitable object is
   # ready.
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    # Running the main function asynchronously.
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")