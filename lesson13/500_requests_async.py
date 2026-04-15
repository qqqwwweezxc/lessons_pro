import asyncio
import aiohttp
import time


URL: str = "https://lms.ithillel.ua/"
REQUESTS: int = 500


async def fetch(session: aiohttp.ClientSession) -> str:
    """
    Sends a single asynchronous HTTP request and returns response text.
    """
    async with session.get(URL) as response:
        return await response.text()


async def async_requests() -> None:
    """
    Executes HTTP requests concurrently using asyncio and aiohttp, measuring execution time.
    """
    start_time: float = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session) for _ in range(REQUESTS)]
        await asyncio.gather(*tasks)

    end_time: float = time.time()

    print(f"Time: {end_time - start_time:.2f} sec")


if __name__ == "__main__":
    asyncio.run(async_requests()) # 0.82 sec
    