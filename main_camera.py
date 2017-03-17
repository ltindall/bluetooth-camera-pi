import cv2
import sys
import requests 
from RPi_API_Interface import * 

# Camera Imports
from picamera.array import PiRGBArray
from picamera import PiCamera

# Sleep function to wait on Camera
from time import sleep

# Get user supplied values
# path to cascade file is first argument to script
#cascPath = sys.argv[1]

# Create the haar cascade
#face_cascade = cv2.CascadeClassifier(cascPath)

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

device = 'b8-27-eb-4f-b9-f6'
email = raw_input("Email: ") 
password = raw_input("Password: ")

token = get_token(email, password)['token']

url = 'http://smartplug.host/api/v1/devices/'+device+'/semantic'
headers = {'Token-Authorization':token} 


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
  print 'frame = ',frame_count
  if frame_count % 30 == 0: 
    fgbg = cv2.BackgroundSubtractorMOG()
    print 'new background'
  frame_count = frame_count + 1

  fgmask = fgbg.apply(frame.array)
  contours, hierarchy = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

  
  for c in contours: 
    area = cv2.contourArea(c)
    #print 'contour area = ',cv2.contourArea(c)
    if area > 300: 
      data = {'semantic_label':'movement', 'data':area}
      resp = requests.post(url, headers=headers, data=data)
      parsed_json = resp.json()
      print parsed_json
      print 'MOTION DETECTED ',counter
      counter = counter + 1

  cv2.imshow('img',fgmask)

  
  # Press 'q' to quit
  key = cv2.waitKey(1) & 0xFF
  rawCapture.truncate(0)
  if key == ord("q"):
     break
