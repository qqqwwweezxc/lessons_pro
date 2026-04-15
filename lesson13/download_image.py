import asyncio 
import aiohttp


async def download_image(url: str, filename: str) -> None:
    """Download one image."""

    path_to_save = "./lesson13/downloaded_images/" + filename

    print(f"Download image {filename}...")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.read()
        
        with open(path_to_save, "wb") as file:
            file.write(data)
        
        print(f"Dowloading complete for file {filename}.")

    except Exception as error:
        print(f"Failed downloading. Error: {error}")


async def main() -> None:
    tasks = [
        asyncio.create_task(download_image(
            "https://images.unsplash.com/photo-1773311400657-29c0891cc045?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "image_1.jpg"
        )),
        asyncio.create_task(download_image(
            "https://images.unsplash.com/photo-1776179342972-875cbbcdd32f?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "image_2.jpg"
        )),
        asyncio.create_task(download_image(
            "https://images.unsplash.com/photo-1774270905852-497bf9d49f89?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "image_3.jpg"
        ))
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())