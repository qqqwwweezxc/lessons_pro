import asyncio
import aiohttp
import random
import time


async def download_page(url: str) -> bytes:
    """Function loads the page"""
    start_time = time.time()

    await asyncio.sleep(random.randint(1, 5))
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()

    end_time = time.time()
    print(f"URL: {url} successfully downloaded. Time: {end_time - start_time:.2f}")

    return data


async def main(urls: list) -> None:
    """Loads all pages by function download_page"""
    tasks = [download_page(url) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = ["https://www.youtube.com/", "https://www.google.com/", "https://lms.ithillel.ua/"]
    asyncio.run(main(urls))
