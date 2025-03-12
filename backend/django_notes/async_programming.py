"""Async programming introduction with Python and Django"""

""" 
    Python Asyncio
    
    Python asynchronous programming is built around the asyncio
    library and uses async/await syntax. The libraries normally are 
    asyncio and time
"""
import asyncio
import time


""" 
    Here a simple example of how to achieve this: 
    
    - async def: Declares an asynchronous function
    - await: Used inside async funtions to wait for other 
             async operations to complete.
"""
async def my_function():
    await asyncio.sleep(1) # Awaitable method
    return "Done!"


""" 
    Running Tasks Concurrently
    
    Knowing this, we can run multiple tasks at the same time.
    The program will do the following steps: 
    
    1. Start both tasks
    2. While task_one is "sleeping", it switches to task_two
    3. Complete task_two while task_one is still running 
    4. Return to and complete task_one
    5. Finish in about two seconds and not 3 as would happen
       sequentially. 
"""
async def task1():
    print("Starting task 1")
    await asyncio.sleep(2)
    print("Task 1 complete")
    return "Result 1"

async def task2():
    print("Starting task 2")
    await asyncio.sleep(3)
    print("Task 2 complete")
    return "Result 2"

async def main():
    results = await asyncio.gather(task1(), task2())
    print(f"Final results: {results}")


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Total execution time: {time.time() - start_time:.2f} seconds")
    
""" 
    How it works
    
    Asyncio is based on an event loop and coroutines:
    - Event Loop: The central execution mechanism that manages all the async tasks
    - Coroutines: Functions defined with async def that can pause execution with await
    - Tasks: Wrappers around coroutines to track their execution
    - Awaitables: Objects that can be used with await (coroutines, tasks, futures)
    
    The key concept here is that when a coroutine hits an await statement, it yields
    control back to the event loop, which can then run other coroutines while the awaited
    operation completes.
"""