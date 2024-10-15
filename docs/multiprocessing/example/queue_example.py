from multiprocessing import Queue, Process
from typing import List


def square_list(mylist: List[int], queue: "Queue[int]"):
    for item in mylist:
        queue.put(item**2)


def print_queue(queue: "Queue[int]"):
    while not queue.empty():
        print(queue.get())
    print("Queue is now empty")


if __name__ == "__main__":
    queue: "Queue[int]" = Queue()
    myList = [1, 4, 5, 6, 7, 4]
    p1 = Process(target=square_list, args=(myList, queue))
    p2 = Process(target=print_queue, args=(queue,))

    # running process p1 to square the list
    p1.start()
    p1.join()

    # running process p2 to get queue elements to print
    p2.start()
    p2.join()

    print("All Done")
