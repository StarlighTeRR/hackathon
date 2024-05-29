import aiohttp
import asyncio
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    url = "http://localhost:3030"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(100000):  # Укажите количество запросов
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)
        
        responses = await asyncio.gather(*tasks)
        print(f"Completed {len(responses)} requests")

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    duration = time.time() - start_time
    print(f"Load test completed in {duration} seconds")