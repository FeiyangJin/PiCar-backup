import time

last = time.time()
while True:
    print(time.time() - last)
    last = time.time()
