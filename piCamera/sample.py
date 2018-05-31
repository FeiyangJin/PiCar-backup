from picamera import PiCamera
from time import sleep
import time

camera = PiCamera()

camera.start_preview()
for i in range(3):
    #sleep(3)
    start = time.time()
    camera.capture('/home/pi/Desktop/imageNoSleep%s.jpg' % i)
    end = time.time()
    print("taking photo time: %f" % (end - start))
camera.stop_preview()

