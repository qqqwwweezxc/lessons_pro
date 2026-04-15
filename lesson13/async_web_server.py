import asyncio
from aiohttp import web


async def handle_root(request: web.Request) -> web.Response:
    """Handler for route '/'."""
    return web.Response(text="Hello world!")


async def handle_slow(request: web.Request) -> web.Response:
    """Handler for the '/slow' route that simulates a long operation."""
    await asyncio.sleep(5)
    return web.Response(text="Operation completed!")


if __name__ == "__main__":
    app = web.Application()
    app.router.add_get("/", handle_root)
    app.router.add_get("/slow", handle_slow)
    
    web.run_app(app, host="127.0.0.1", port=8080)