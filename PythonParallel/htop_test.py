import time
import os
from multiprocessing import Pool

def f(x):
    print("pid for function f %i" % os.getpid())
    time.sleep(10)
    return x*x

def g(x):
    print("pid for function g %i" % os.getpid())
    time.sleep(10)
    return x+x


##start = time.time()
##
##while time.time() - start < 10:
##    print("hello")

if __name__ == '__main__':
    print("pid at top of main: %i" % os.getpid())
    pool = Pool()
    result1 = result1 = pool.apply_async(f,[4])
    result2 = pool.apply_async(g,[5])
    answer1 = result1.get()
    answer2 = result2.get()
    print("answers are %f and %f" % (answer1,answer2))
    print("pid at end of main: %i" % os.getpid())
