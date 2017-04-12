''' 
Car detection and tracking program. It uses HAAR Cascades and KCF tracking alg.

'''

import cv2
import numpy as np
from time import time
import kcftracker
import thread
 
def isNewRoi(rx,ry,rw,rh,rectangles):
    for r in rectangles:
        if abs(r[0] - rx) < 2.5*rw and abs(r[1] - ry) < 2.5*rh:
           return False  
    return True
 
def detectRegionsOfInterest(frame, cascade):
    scaleDown = 2
    frameHeight, frameWidth, fdepth = frame.shape 
    # Resize
    frame = cv2.resize(frame, (frameWidth/scaleDown, frameHeight/scaleDown)) 
    frameHeight, frameWidth, fdepth = frame.shape
 
    # haar detection
    cars = cascade.detectMultiScale(frame, 1.2, 1)
 
    newRegions = []
    # iterate regions of interest
    for (x,y,w,h) in cars:
        roi = [x,y,w,h]
        newRegions.append( [x*scaleDown,y*scaleDown,w*scaleDown,h*scaleDown] )
    return newRegions
 
def track_init(obj, frame):
	tracker.init(obj, frame)
 
def detectCars(filename):
    rectangles = []
    cascade = cv2.CascadeClassifier('cars.xml')
    vc = cv2.VideoCapture(filename)
    duration = 0.01
 
    if vc.isOpened():
        rval , frame = vc.read()
    else:
        rval = False
 
    roi = [0,0,0,0]
    frameCount = 0
    bbox = [250, 172, 76, 76]
    print "First object to track:" + str(bbox)
    thread.start_new_thread(track_init, (bbox, frame))
 
    while rval:
        rval, frame = vc.read()
        frameHeight, frameWidth, fdepth = frame.shape
        cv2.line(frame, (0,int(0.9*frameHeight)), (frameWidth,int(0.7*frameHeight)), (0,255,150), 1)
        newRegions = detectRegionsOfInterest(frame, cascade)
        for region in newRegions:
            if isNewRoi(region[0],region[1],region[2],region[3],rectangles):
                rectangles.append(region)
    
        print '{} {}'.format("RECTANGLES:", rectangles)
        #ok, bbox = tracker.update(frame)
        #tracker.init([region[0],region[1],region[2],region[3]], frame)
        t0 = time()
        boundingbox = tracker.update(frame)
        t1 = time()
        boundingbox = map(int, boundingbox)
        print '{} {} {} {}'.format("TRACKING:", boundingbox[0],boundingbox[1], (boundingbox[0]+boundingbox[2]),(boundingbox[1]+boundingbox[3]))
        cv2.rectangle(frame,(boundingbox[0],boundingbox[1]), (boundingbox[0]+boundingbox[2],boundingbox[1]+boundingbox[3]), (0,255,0), 2)
        
        duration = 0.8*duration + 0.2*(t1-t0)
        cv2.putText(frame, 'FPS: '+str(1/duration)[:4].strip('.'), (8,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

 
        frameCount = frameCount + 1
        if frameCount > 150: 
            frameCount = 0
            rectangles = []
 
        # show result
        cv2.imshow("Result",frame)
        cv2.waitKey(1);
    vc.release()

if __name__ == '__main__':
	tracker = kcftracker.KCFTracker(False, True, True)
	detectCars('static/vid3.mp4')