import multiprocessing
import time


def calculate_part_of_factorial(start: int, end: int) -> int:
    """Calcultaing a part of factorial"""
    result = 1

    for i in range(start, end + 1):
        result *= i
    return result


def paralell_factorial(number: int, num_processes: int = None) -> int:
    """Calculating a factorial by multiprocessing"""

    if number < 0:
        raise ValueError("Factorial cant be negative!")
    if number in (0, 1):
        return 1
    
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()

    chunk_size = number // num_processes
    parts = []

    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i != num_processes - 1 else number

    if start <= end:
        parts.append((start, end))

    with multiprocessing.Pool(processes=num_processes) as pool:
        partial_results = pool.starmap(calculate_part_of_factorial, parts)

    result = 1

    for res in partial_results:
        result *= res

    return result


if __name__ == "__main__":
    number = 1000

    print(f"Start calculating {number}!...")
    start_time = time.time()

    result = paralell_factorial(number)

    end_time = time.time()

    print(f"Calculation time: {end_time - start_time:.2f} sec.")

    print(f"Result: {result}")



