import requests
import time


URL: str = "https://lms.ithillel.ua/"
REQUESTS: int = 500


def sync_requests() -> None:
    """
    Sends HTTP requests sequentially synchronous mode and measures total execution time.
    """
    start_time: float = time.time()

    for _ in range(REQUESTS):
        requests.get(URL)

    end_time: float = time.time()

    print(f"Time: {end_time - start_time:.2f} sec")


if __name__ == "__main__":
    sync_requests() # 77.83 sec

