import asyncio


async def slow_task() -> None:
    """Function which simulates the task for 10 seconds."""
    print("Proccesing with task...")

    await asyncio.sleep(10)

    print("Task completed!")


async def main() -> None:
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        print("Timeout error.")


asyncio.run(main())