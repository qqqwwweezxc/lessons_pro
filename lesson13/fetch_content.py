import asyncio
import aiohttp
from typing import List


async def fetch_content(url: str) -> bytes:
    """Fetch content from a given URL"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.read()
                print(f"Page content '{url}': {len(data)} bytes")
                return data
        

    except aiohttp.ClientError as error:
        return f"Request error for '{url}': {error}"
    except asyncio.TimeoutError:
        return f"Timeout when requesting to url '{url}'"


async def fetch_all(urls: list) -> List[bytes]:
    """Fetch multiple URLs concurrently."""
    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [fetch_content(url) for url in urls]
        results = await asyncio.gather(*tasks)

    return results


if __name__ == "__main__":
    urls = ["https://www.youtube.com/", "https://www.google.com/", "https://lms.ithillel.ua/"]
    asyncio.run(fetch_all(urls))
