from threading import Thread
import os
import time

def square_numbers():
    for i in range(50):
        i * i
        time.sleep(0.1)
if __name__ == "__main__":

    threads = []
    num_of_threads = 10

    # create processes
    for i in range(num_of_threads):
        t = Thread(target=square_numbers)
        threads.append(t)

    # start
    for t in threads:
        t.start()

    # join
    for t in threads:
        t.join()

    print("end main")