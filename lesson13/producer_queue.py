import asyncio


async def producer(queue: asyncio.Queue) -> None:
    """Function adds 5 tasks to the queue with a delay of 1 second."""
    for i in range(1, 6):
        await asyncio.sleep(1)
        task = f"Task {i}"
        await queue.put(task)
        print(f"Produced: {task}")


async def consumer(queue: asyncio.Queue, consumer_id: int) -> None:
    """Function removes a task from the queue, executes it"""
    while True:
        task = await queue.get()
        print(f"Consumer #{consumer_id} processing {task}")

        await asyncio.sleep(2)

        print(f"Consumer {consumer_id} finished {task}")
        queue.task_done()


async def main() -> None:
    queue = asyncio.Queue()

    tasks = asyncio.create_task(producer(queue))

    consumers = [
        asyncio.create_task(consumer(queue, 1)),
        asyncio.create_task(consumer(queue, 2))
    ]

    await tasks
    await queue.join()

    for c in consumers:
        c.cancel()

    print("All tasks completed!")


if __name__ == "__main__":
    asyncio.run(main())