import time

import asyncio
import aiohttp


async def get_request() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:23555") as response:
            return await response.json()


async def first():
    time.sleep(1)
    data = await get_request()
    print(1, data)

async def second():
    time.sleep(1)
    data = await get_request()
    print(2, data)


async def main():
    # await first()
    # await second()

    # await asyncio.gather(first(), second())

    task1 = asyncio.Task(first())
    task2 = asyncio.Task(second())

    await task1
    await task2


start = time.time()
asyncio.run(main())
stop = time.time()

print(f"Request with concurrent async/await, time: {stop - start}")
