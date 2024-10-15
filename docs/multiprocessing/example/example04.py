from multiprocessing import Queue, Pipe, Process, Lock
from multiprocessing.connection import PipeConnection
from multiprocessing.synchronize import Lock as LockType
import time
import random
from typing import List, Tuple


def scrape_website(
    url: str,
    queue: "Queue[Tuple[str, str]]",
    child_conn: PipeConnection,
    lock: LockType,
):
    print(f"Scraping {url}")
    scrape_time = random.randint(1, 10)
    time.sleep(scrape_time)
    data = f"Scraped data in {scrape_time} seconds"
    # Using lock to ensure only one process write data to share resource
    with lock:
        print(f"Scraped {url}")

    # send data to the main process
    queue.put((url, data))

    # send metadata via Pipe
    child_conn.send((url, data))
    child_conn.close()


def aggregate_data(
    queue: "Queue[Tuple[str, str]]",
    parent_conn: PipeConnection,
    lock: LockType,
    websites: List[str],
) -> None:
    results = []
    times = []

    for url in websites:
        web, data = queue.get()
        results.append((web, data))

        web_url, scrape_time = parent_conn.recv()
        times.append((web_url, scrape_time))

    # safely print the aggregate data using Lock
    with lock:
        print("---Aggregated result---")
        for url, data in results:
            print(f"{url}: {data}")

        for url, scrape_time in times:
            print(f"{url}: {scrape_time} seconds")


if __name__ == "__main__":
    websites = ["google.com", "facebook.com", "x.com", "github.com"]

    queue: "Queue[Tuple[str, str]]" = Queue()
    parent_conn, child_conn = Pipe()
    lock = Lock()

    processes = []

    for url in websites:
        p = Process(target=scrape_website, args=(url, queue, child_conn, lock))
        processes.append(p)
        p.start()

    # wait for all processes to finish
    for p in processes:
        p.join()

    aggregate_process = Process(
        target=aggregate_data, args=(queue, parent_conn, lock, websites)
    )
    aggregate_process.start()
    aggregate_process.join()
    print("Done")
