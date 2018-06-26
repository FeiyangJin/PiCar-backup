from multiprocessing import Pool
import time
import picamera
import datetime

frames = 20
def f(x):
    time.sleep(3)
    return x*x

def g(x):
    time.sleep(5)
    return x+x

def filenames():
    frame = 0
    while frame < frames:
        current = datetime.datetime.now()
        yield '%s.jpg' % current
        frame += 1
        
def capture():
    with picamera.PiCamera(resolution=(480,480), framerate=100) as camera:
        camera.start_preview()
        # Give the camera some warm-up time
        time.sleep(2)
        camera.capture_sequence(filenames(), use_video_port=True)
        return 1
    
if __name__ == '__main__':
    pool = Pool()
    start = time.time()
##    answer1 = f(4)
##    answer2 = g(5)
    result1 = pool.apply_async(f,[4])
    result2 = pool.apply_async(g,[5])
    result3 = pool.apply_async(capture)
    #answer1 = result1.get()
    #answer2 = result2.get()
    #result3.get()
    end = time.time()
    time.sleep(5)
    #print("the square is %i" % (answer1))
    #print("the sum is %i" % (answer2))
    print("total time is %f" % (end - start))
##    with Pool(5) as p:
##        print("hello")
##        result = p.map(f, [1, 2, 3])
##        print(result)
