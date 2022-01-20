from multiprocessing import Process, Value, Array, Lock
import os
import time

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock: # prevents race conditions (multiple processes attempting to modify a shared value)
            number.value += 1

def add_200_arr(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] +=1 

if __name__ == "__main__":

    lock = Lock()

    # shared_number = Value('i', 0)
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('array at beginning is ', shared_array[:])

    # print('Number at beginning is ', shared_number.value)

    p1 = Process(target=add_200_arr, args=(shared_array,lock))
    p2 = Process(target=add_200_arr, args=(shared_array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('array at end is ', shared_array[:])

