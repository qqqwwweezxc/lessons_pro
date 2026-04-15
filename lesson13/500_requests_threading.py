import requests
import time
from concurrent.futures import ThreadPoolExecutor


URL: str = "https://lms.ithillel.ua/"
REQUESTS: int = 500
MAX_WORKERS: int = 50


def fetch(_) -> int:
    """
    Sends a single HTTP request and returns status code.
    """
    response = requests.get(URL)
    return response.status_code


def threaded_requests() -> None:
    """
    Executes HTTP requests using multithreading and measures execution time.
    """
    start_time: float = time.time()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        list(executor.map(fetch, range(REQUESTS)))

    end_time: float = time.time()

    print(f"Time: {end_time - start_time:.2f} sec")


if __name__ == "__main__":
    threaded_requests() # 2.21 sec