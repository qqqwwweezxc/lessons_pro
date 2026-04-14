import multiprocessing
import random
from typing import List

def sum_of_the_part(part: list) -> int:
    """Function that calculates the sum of part of an array"""
    return sum(part)

def main():
    """
    Program that divides a huge amount of numbers into several parts and calculates 
    the sum of each part in parallel in different processes.
    """

    array_size = 10_000_000
    data: List[int] = [random.randint(1, 100) for _ in range(array_size)]

    num_processes: int = multiprocessing.cpu_count()

    chunk_size: int = len(data) // num_processes
    chunks: List[int] = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with multiprocessing.Pool(processes=num_processes) as pool:
        results: List[int] = pool.map(sum_of_the_part, chunks)

    total: int = sum(results)

    print(f"Sum of the array: {total}")

if __name__ == "__main__":
    main()

