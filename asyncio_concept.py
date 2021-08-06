# Synchronous Programming -> Everything we write is happening sequentially
def foo():
    return "Yes"

foo()
# The print program won't run, until foo() function hasn't executed totally, this is sequential programming.
print("Jenn")

# Asynchronous Programmming _> We don't need to wait for something to be completely done before we run other parts of the code. This is benefecial, when we are waiting for something, example, querying the dB, response form network, user input.

import asyncio
 
async def main():
    print("Jenn")
    await poo("Jenny")
    print("Finished")
# Async creates a wrapper around a function and the function becomes a coroutine. For it to execute we need to use await.
print(main())
# <coroutine object main at 0x0000027DB71822C0>
# we need to create event-loop for the coroutine to work/ or using await keyword inside the coroutine.

async def poo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())
# Jenn -- main()
# Jenny -- poo()

# Output -> Jenn
# Jenny (after 1 sec)
# Finished
# ____________________________________________________________________________________________________
# A "Task" is created so that the program run asynchrounously, line 15 will be changed for that. 
async def main():
    print("Jenn")
    task = asyncio.create_task(poo('text'))
    # the above line tells, that to run this piece of code as soon as possible, but while it executes, complete other task.
    print("Finished")

async def poo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())
# Jenn
# Finished
# text