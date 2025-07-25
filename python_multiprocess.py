import multiprocessing
import time

def worker_func(args):
    id, timeout = args
    print(time.time(), id, "START")
    time.sleep(timeout)
    print(time.time(), id, "END")

pool = multiprocessing.Pool(processes=2)
pool.map(worker_func, [(1,2),(2,4),(3,3),(4, 5)])
pool.close()
pool.join()

