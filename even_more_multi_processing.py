from multiprocessing import Pool
import numbers

def cube(number):
    return number ** 3

if __name__ == "__main__":
    numbers = range(10)

    pool = Pool()
    result = pool.map(cube, numbers)

    pool.close()
    pool.join()

    print(result)  
    