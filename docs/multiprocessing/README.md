# Multiprocessing

## Theory

### What is multiprocessing?

- Multiprocessing refers to the ability of a system to support more than one processor at the same time. Application in a multiprocessing system are broken to smaller routines that run independently. The operating system allocates these threads to the processors improving performance of the system.

### Why multiprocessing?

- Consider a computer system with a single processor. If it is assigned several processes at the same time, it will have to interrupt each task and switch briefly to another, to keep all the processes going. This situation is just like a chef workin in a kitchen alone. He has to do several tasks like baking, stirring kneading dough, etc. So the gist is that: The more tasks you must do at once, the more difficult it gets to keep track of them all, and keeping the timing right becomes more of a challenge. This is where the concept of mutiprocessing arise!

![single-task](./chef.png)

### A multiprocessing system can have

1. multiprocessor: ie a computer with more than one CPU (some server computer support more than one CPU such dual Xeon CPU)
2. multi-core processor: ie a single computing component with two or more independant actual processing units (called cores, a Xeon CPU can have 28 to 36 cores per CPU)

Here the CPU can easily executes several tasks at once, with each task using it own processor. It is just like the chef in last situation being assisted by his assistants. Now, they can divide the tasks among themself and chef doesn't need to switch between his tasks.

![multi-tasks](./multi-chef.png)

## Example

### Multiprocessing in Python

In Python the [mutiprocessing](https://docs.python.org/3/library/multiprocessing.html) module includes a very simple and intuitive API for dividing work between multiple processes. Let us consider a simple example using `multiprocessing` module.

#### Example 01

```python
import multiprocessing
import time


def print_cube(num: float) -> None:
    """
    function to print cube of given num

    Parameters:
    - num: float

    Returns:
    - None
    """

    print("Simulate some work for cube")
    time.sleep(10)
    print(f"Cube: {num * num * num}")


def print_square(num: float) -> None:
    """
    function to print square of given num

    Parameters:
    - num: float

    Returns:
    - None
    """

    print("Simulate some work for square")
    time.sleep(15)
    print(f"Square: {num * num}")


if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(13,))

    # starting process 1
    p1.start()

    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()

    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("Done")

# Result
#
# Simulate some work for cube
# Simulate some work for square
# Cube: 2197
# Square: 100
# Done
```

Explain the example from above:

* To import the `multiprocessing` module, do: `import multiprocessing`
* To create a process, we create an object of Process class, it take following arguments:
  * target: the function to be executed by process
  * args: the arguments to be passed to the target function, we passing a tuple of parameters
  ```python
  p1 = multiprocessing.Process(target=method_name_01, args=(param1, param2))
  p2 = multiprocessing.Process(target=method_name_02, args=(param1,))
  ```
* to start a process, we use `start` method of `Process` class: `p1.start()`
* once the processes start, the current program also keeps on executing, in order to stop execution of current program until a process is complete, we use `join` method
  ```python
  p1.join()
  p2.join()
  ```

#### Example 02

Consider another program to understand the concept of different processes running on the same Python script. In this example, we print the ID of the processes running the target function

```python
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

# Result
#
# ID of main process: 25392
# ID of process p1: 17192
# ID of process p2: 24004
# Process p1 alive: True
# Process p2 alive: True
# Simulate some work for worker01. 17192
# Simulate some work for worker02. 24004
# Done worker01
# Done worker02
# Done
# Process p1 alive: False
# Process p2 alive: False
```

* The main Python script has a different process ID and multiprocessing module spawns new processes with different process IDs as we create **Process** object **p1**, **p2**. In above program, we use **os.getpid()** function to get ID of process running the current target function. Notice that it matches with the process IDs p1, p2 which we using pid attribute of Process class.
* Each process runs independently and has its own memory space
* As soon as the execution of target function is finished, the processes get terminated. In above program we used `is_alive()` method of **Process** class to check if a process is still active or not.

Consider the diagram below to understand how new processes are different from main Python script

![multiprocessing](./multiprocessing.png)

## The 4 Essential Parts of Multiprocessing in Python

Multiprocessing in Python involes several key components that allow efficient parallel execution of tasks:

* **Process**: The Process class is used to create and manage independent processes. Each process runs in its own memory space
* **Queue**: The Queue class is a shared job queue that allows process-safe data exchange and coordination between processes. It's used for passing messages or results between process instances.
* **Pipe**: Pipes provide a way to establish a communication channel between processes. They are useful for bidirectional communication between two processes.
* **Lock**: Locks are used to ensure that only process is executing a certain section of code at a time. This prevents data corruption by synchronizing access to shared resources.

```python
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
    """
    Example that emphasize 4 essential key components of multiprocessing
    * Process
    * Queue
    * Pipe
    * Lock
    """
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

# Result
#
# Task executed
# Consumer received from queue: Done
# Consumer received from pipe: Data from pipe worker
# Done
```