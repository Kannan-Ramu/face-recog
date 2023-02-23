''''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)
	==> Faces will be stored on a directory: dataset/ (if does not exist, pls create one)
	==> Each face will have a unique numeric integer ID as 1, 2, 3, etc                       
'''

import cv2
import os
from PIL import Image
import time

cam = cv2.VideoCapture(0)
cam.set(3, 640) 
cam.set(4, 480) 
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #Note the change


face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
count = 0

while(True):

    ret, img = cam.read()
    
    cv2.imshow('image1', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        print(count)
        cv2.imwrite("D:\\Hackathon dumps 2k23\\OpenCV-Face-Recognition\\FacialRecognition\\dataset\\User." + str(face_id) + '.' + str(count) + ".jpg",gray[y:y+h,x:x+w])
      

        cv2.imshow('image', img)
        

        

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 300:
         break


print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()


