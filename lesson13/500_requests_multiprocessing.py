import requests
import time
from multiprocessing import Pool, cpu_count


URL: str = "https://lms.ithillel.ua/"
REQUESTS: int = 500
PROCESSES: int = cpu_count()


def fetch(_: int) -> int:
    """
    Sends a single HTTP request and returns status code.
    """
    response = requests.get(URL)
    return response.status_code


def process_requests() -> None:
    """
    Executes HTTP requests using multiprocessing and measures execution time.
    """
    start_time: float = time.time()

    with Pool(processes=PROCESSES) as pool:
        pool.map(fetch, range(REQUESTS))

    end_time: float = time.time()

    print(f"Time: {end_time - start_time:.2f} sec")


if __name__ == "__main__":
    process_requests() # 9.22 sec
    