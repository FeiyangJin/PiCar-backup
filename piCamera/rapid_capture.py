import time
import picamera
import datetime

frames = 20

def filenames():
    frame = 0
    while frame < frames:
        current = datetime.datetime.now()
        yield '%s.jpg' % current
        frame += 1

with picamera.PiCamera(resolution=(480,480), framerate=100) as camera:
    camera.start_preview()
    # Give the camera some warm-up time
    time.sleep(2)
    start = time.time()
    camera.capture_sequence(filenames(), use_video_port=True)
    finish = time.time()
print('Captured %d frames at %.2ffps, in %f seconds' % (
    frames,
    frames / (finish - start), (finish - start)))
