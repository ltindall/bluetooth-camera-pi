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

fgbg = cv2.BackgroundSubtractorMOG()

# Wait for the camera to start up
sleep(1.0)

counter = 0 
frame_count = 0 
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
  print 'frame = ',frame_count
  if frame_count % 30 == 0: 
    fgbg = cv2.BackgroundSubtractorMOG()
    print 'new background'
  frame_count = frame_count + 1
  # Grab an image from the camera
  #image = frame.array
 
  # Shrink it down
  #height, width = image.shape[:2]
  #image = cv2.resize(image,(width/2,height/2),interpolation=cv2.INTER_CUBIC)
 
  # Your code here...
  # Follow the OpenCV tutorial to use their detection algorithms!
  #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  #for (x,y,w,h) in faces:
  #  cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

  fgmask = fgbg.apply(frame.array)
  #print 'length of fgmask = ',len(fgmask)
  #print 'fgmask = ',fgmask
  #print 'sum of 1s in fgmask = ',sum(fgmask)
  contours, hierarchy = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

  
  for c in contours: 
    #print 'contour area = ',cv2.contourArea(c)
    if cv2.contourArea(c) > 300: 
      print 'MOTION DETECTED ',counter
      counter = counter + 1
  #print 'contours = ',contours 
  #cnt = contours[4]
  #cv2.drawContours(fgmask, contours, -1, (0,255,0), 3)

  cv2.imshow('img',fgmask)

  
  # Press 'q' to quit
  key = cv2.waitKey(1) & 0xFF
  rawCapture.truncate(0)
  if key == ord("q"):
     break
