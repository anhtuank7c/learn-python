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
    # p2.join()

    # both processes finished
    print("Done")
