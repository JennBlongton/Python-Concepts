import asyncio

async def fetch_data():
    print('Start Fetching')
    await asyncio.sleep(2)
    print('Done Fetching')
    return {'data': 1}

async def print_data():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_data())

    value = await task1
    print(value)
    await task2

asyncio.run(main())

# Start Fetching
# 0
# 1
# 2
# 3
# Done Fetching
# {'data': 1}
# 4
# 5
# 6
# 7
# 8
# 9