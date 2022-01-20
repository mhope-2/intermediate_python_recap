import queue
from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q, lock):
    while True:
        value = q.get()
        # processing
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()

if __name__ == "__main__":
    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread1 = Thread(target=worker, args=(q,lock))
        thread1.daemon = True
        thread1.start()

    for i in range(1,21):
        q.put(i)
    
    q.join()
    # q.put(1)
    # q.put(2)
    # q.put(3)

    # first = queue.get()
    # print(first)

    # q.task_done()
    # q.join()

    print("end main")