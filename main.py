import asyncio
import random


async def cook(name, queue):
    while True:
        order = await queue.get()
        print(f"👨‍🍳 Кухар {name} розпочав готувати {order}...")
        cook_time = random.uniform(2, 5)
        await asyncio.sleep(cook_time)
        print(f"✅ Кухар {name} видав {order} за {cook_time:.2f}с.")
        queue.task_done()


async def cashier(name, queue, orders_count):
    for i in range(1, orders_count + 1):
        order_name = f"Замовлення #{i}"
        await queue.put(order_name)
        print(f"💰 Касир {name} прийняв {order_name} і передав на кухню.")
        await asyncio.sleep(random.uniform(0.5, 1.5))


async def main():
    kitchen_queue = asyncio.Queue()

    cooks = [
        asyncio.create_task(cook("Stephan", kitchen_queue)),
        asyncio.create_task(cook("Danil", kitchen_queue)),
        asyncio.create_task(cook("Volodimir", kitchen_queue))
    ]

    cashiers = [
        asyncio.create_task(cashier("Olha", kitchen_queue, 5)),
        asyncio.create_task(cashier("Bohdan", kitchen_queue, 5))
    ]

    await asyncio.gather(*cashiers)
    await kitchen_queue.join()

    for c in cooks:
        c.cancel()

    print("\n🚀 Всі замовлення видані! Ресторан зачиняється.")

if __name__ == "__main__":
    asyncio.run(main())