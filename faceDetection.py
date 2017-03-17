import cv2
import sys

# Camera Imports
from picamera.array import PiRGBArray
from picamera import PiCamera

# Sleep function to wait on Camera
from time import sleep

# Get user supplied values
# path to cascade file is first argument to script
cascPath = sys.argv[1]

# Create the haar cascade
face_cascade = cv2.CascadeClassifier(cascPath)

# Capture Object
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))

# Wait for the camera to start up
sleep(1.0)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
  
  # Grab an image from the camera
  image = frame.array
 
  # Shrink it down
  height, width = image.shape[:2]
  image = cv2.resize(image,(width/2,height/2),interpolation=cv2.INTER_CUBIC)
 
  # Your code here...
  # Follow the OpenCV tutorial to use their detection algorithms!
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

  cv2.imshow('img',image)

  
  # Press 'q' to quit
  key = cv2.waitKey(1) & 0xFF
  rawCapture.truncate(0)
  if key == ord("q"):
     break
