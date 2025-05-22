from multiprocessing import Pipe, Process
from multiprocessing.connection import PipeConnection


def pipe_worker(conn: PipeConnection):
    conn.send("Data from pipe worker")
    conn.close()


if __name__ == "__main__":
    print("Start")
    parent_conn, child_conn = Pipe()
    pipe_process = Process(target=pipe_worker, args=(child_conn,))
    pipe_process.start()
    pipe_process.join()
    print(parent_conn.recv())
    print("Done")
