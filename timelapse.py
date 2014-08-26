import time
import picamera

file_path = '/home/pi/timelapse/foto/' # Where to save the pictures

with picamera.PiCamera() as camera:
    camera.rotation = 180 # Only if camera module is not upright
    camera.resolution = (2592, 1944) # Maximum resolution because bigger is better in post
    camera.ISO = 100 # 100, 200, 320, 400, 500, 640, 800
    camera.shutter_speed = 333333 # shutterspeed of the camera, 1000000 = 1 second
    camera.awb_mode = 'horizon' # off, auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent, flash, horizon
    for filename in camera.capture_continuous(file_path + 'timelapse_{timestamp:%Y%m%d%H%M%S}.jpg'): # prefix with timestamp (date, month, day, hour, minute, seccond) to ensure unique filenames
        print('Captured %s' % filename)
        time.sleep(1) # time between shots in seconds
