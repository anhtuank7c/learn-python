import multiprocessing
import time
import os


def worker01() -> None:
    print(f"Simulate some work for worker01. {os.getpid()}")
    time.sleep(10)
    print("Done worker01")


def worker02() -> None:
    print(f"Simulate some work for worker02. {os.getpid()}")
    time.sleep(10)
    print("Done worker02")


if __name__ == "__main__":

    print(f"ID of main process: {os.getpid()}")

    # creating processes
    p1 = multiprocessing.Process(target=worker01)
    p2 = multiprocessing.Process(target=worker02)

    # starting process 1
    p1.start()

    # starting process 2
    p2.start()

    print(f"ID of process p1: {p1.pid}")
    print(f"ID of process p2: {p2.pid}")

    print(f"Process p1 alive: {p1.is_alive()}")
    print(f"Process p2 alive: {p2.is_alive()}")

    # wait until process 1 is finished
    p1.join()

    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("Done")

    # check processes are alive
    print(f"Process p1 alive: {p1.is_alive()}")
    print(f"Process p2 alive: {p2.is_alive()}")
