from multiprocessing import Lock, Pipe, Queue, Process
from multiprocessing.connection import PipeConnection
from multiprocessing.synchronize import Lock as LockType
from typing import Any


def queue_worker(queue: "Queue[str]", lock: LockType):
    with lock:
        print("Task executed")
        queue.put("Done")


def pipe_worker(conn: PipeConnection):
    conn.send("Data from pipe worker")
    conn.close()


def consumer(queue: "Queue[Any]", parent_conn: PipeConnection, lock: LockType):
    with lock:
        print(f"Consumer received from queue: {queue.get()}")
        print(f"Consumer received from pipe: {parent_conn.recv()}")


if __name__ == "__main__":
    # for exchange data between processes safely
    queue: "Queue[Any]" = Queue()

    # For synchronization (ensures only one process can access at a time)
    lock: LockType = Lock()

    # Pipe for two-way communications between processes
    parent_conn, child_conn = Pipe()

    # create separate processes

    # queue base process
    queue_process = Process(target=queue_worker, args=(queue, lock))
    # pipe base process
    pipe_process = Process(target=pipe_worker, args=(child_conn,))
    # consumer that receive data
    consumer_process = Process(target=consumer, args=(queue, parent_conn, lock))

    # start processes
    queue_process.start()
    pipe_process.start()

    # wait for both processes to finish
    queue_process.join()
    pipe_process.join()

    # start the consumer process after data is available
    consumer_process.start()
    consumer_process.join()

    print("Done")
