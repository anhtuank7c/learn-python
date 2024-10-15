from multiprocessing import Process, Queue, Lock
from multiprocessing.synchronize import Lock as LockType
import time
from random import randint


# Worker function that sends data to the Queue
def worker_with_queue(queue: "Queue[int]", lock: LockType) -> None:
    result = randint(1, 100)  # Simulate some work by generating a random number
    time.sleep(randint(1, 3))  # Simulate task duration
    queue.put(result)  # Send the result to the shared Queue

    # Protect console output with Lock
    with lock:
        print(f"Worker {result} sent data to the queue.")


# Aggregator function that collects results from the Queue
def aggregator_with_queue(
    queue: "Queue[int]", lock: LockType, num_workers: int
) -> None:
    results = []
    for _ in range(num_workers):
        result = queue.get()  # Collect results from the Queue
        results.append(result)

        # Protect console output with Lock
        with lock:
            print(f"Aggregator received {result} from the queue.")
    print("Final aggregated results from Queue:", results)


if __name__ == "__main__":
    queue: "Queue[int]" = Queue()  # Queue is process-safe, no Lock needed
    lock = Lock()  # Lock for protecting console output
    num_workers = 3
    processes = [
        Process(target=worker_with_queue, args=(queue, lock))
        for _ in range(num_workers)
    ]

    # Start all worker processes
    for p in processes:
        p.start()

    # Start the aggregator to collect results
    aggregator = Process(target=aggregator_with_queue, args=(queue, lock, num_workers))
    aggregator.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()
    aggregator.join()
