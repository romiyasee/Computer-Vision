import cv2 as cv
import numpy as np
import cvzone

kernel = np.ones((3,3),dtype='uint8')
input = cv.VideoCapture('bahan.mp4')
detektor = cv.createBackgroundSubtractorMOG2()
sjdslkdj

while True:
    _,video = input.read()
    
    gray_frame = cv.cvtColor(video,cv.COLOR_BGR2GRAY)
    blur_frame = cv.GaussianBlur(gray_frame,(3,3),1)
    dilated_frame = cv.dilate(blur_frame,kernel,2)
    eroded_frame = cv.dilate(dilated_frame,kernel,2)
    masked = detektor.apply(eroded_frame)
    _,mask = cv.threshold(masked,250,255,cv.THRESH_BINARY)

    contours,_ = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 1000 :
            x,y,w,h = cv.boundingRect(contour)
            cv.rectangle(video,(x,y),(x+w,y+h),(0,255,255),5)

    hasil = cvzone.stackImages([video,mask],2,0.60)
    cv.imshow('video_frame', hasil)
    
    x = cv.waitKey(20)
    if x == 27:
        break
