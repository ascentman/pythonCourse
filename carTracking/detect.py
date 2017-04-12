''' 
Car detection and tracking program. It uses HAAR Cascades and KCF tracking alg.

'''
import os
import cv2
import numpy as np
import threading
import Queue
import logging
import time as t
from time import time
from flask import Flask, render_template, Response, url_for, send_file
import kcftracker

app = Flask(__name__)
VID_FILENAME = 'static/vid3.mp4'
vc = cv2.VideoCapture(VID_FILENAME)

# =========================================

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('base.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(detectCars(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/open/')
def open_video():
    try:
        return send_file('static/vid3.mp4', attachment_filename='vid3.mp4')
    except Exception as e:
        return str(e)

@app.route('/process/', methods = ['GET', 'POST'])
def process_video():
    return render_template('index.html')

@app.route('/analyze', methods=['GET','POST'])
def show_res():
    car_count = 0
    car_list = []
    for car in os.listdir('static/detected'):
        car_list.append(os.path.join('static/detected', car))
        car_count += 1
    return render_template('res.html', car_list=car_list, car_count=car_count)
 
# =============================================================================

def is_new_roi(rx,ry,rw,rh,rectangles):
    '''
    function check if detected area can be threated as new Region of Interest
    '''
    for r in rectangles:
        if abs(r[0] - rx) < 4*rw and abs(r[1] - ry) < 4*rh:
           return False
    return True
 
def detect_regions_of_interest(frame, cascade):
    '''
    find new area with HAAR algorithm
    '''
    scaleDown = 2
    frameHeight, frameWidth, fdepth = frame.shape 
    # Resize
    frame = cv2.resize(frame, (frameWidth/scaleDown, frameHeight/scaleDown)) 
    frameHeight, frameWidth, fdepth = frame.shape
 
    cars = cascade.detectMultiScale(frame, 1.2, 1)
 
    newRegions = []
    for (x,y,w,h) in cars:
        roi = [x,y,w,h]
        newRegions.append( [x*scaleDown,y*scaleDown,w*scaleDown,h*scaleDown] )
 
    return newRegions

def track():
    '''
    tracking with KCF algorythm. NOTE: does not work with more than one target
    '''
    while q.empty() is False:
        obj = q.get()
        tracker.init(obj, frame)
 
def detectCars():
    '''
    main functionality: reading file, finding cars, counting
    '''
    rectangles = []
    car_count = 0
    cascade = cv2.CascadeClassifier('cars.xml')
    tracker = kcftracker.KCFTracker(False, True, True)
    duration = 0.01
    scale = 0.8
 
    if vc.isOpened():
        rval , frame = vc.read()
    else:
        rval = False

    frameCount = 0
 
    while rval:
        rval, frame = vc.read()
        frameHeight, frameWidth, fdepth = frame.shape 
        t.sleep(0.05)
        cv2.putText(frame, 'Car count: '+str(car_count), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,100,0), 2)
        newRegions = detect_regions_of_interest(frame, cascade)
        for region in newRegions:
            if is_new_roi(region[0],region[1],region[2],region[3],rectangles):
                rectangles.append(region)
                q.put(region)

                tracker.init([region[0],region[1],region[2],region[3]], frame)
                t0 = time()
                boundingbox = tracker.update(frame)
                t1 = time()
                boundingbox = map(int, boundingbox)
                cv2.rectangle(frame,(boundingbox[0],boundingbox[1]), (boundingbox[0]+boundingbox[2],boundingbox[1]+boundingbox[3]), (0,255,255), 2)
                cv2.putText(frame,"Car detected", (int(boundingbox[0]),int(boundingbox[1]-20)), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 3)
                car_count += 1
                logging.info("New car detected: %s", region)
                
                poss_car = frame[region[1]:region[1]+region[2], region[0]:region[0]+region[3]]
                poss_car_name = "static/detected/car_" + str(car_count) + ".jpg"
                cv2.imwrite(poss_car_name, poss_car)

                duration = 0.8*duration + 0.2*(t1-t0)
                cv2.putText(frame, 'FPS: '+str(1/duration)[:4].strip('.'), (8,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

        frameCount = frameCount + 1
        if frameCount > 150: 
            frameCount = 0
            rectangles = []

        resized = cv2.resize(frame, (int(scale*frameWidth), int(scale*frameHeight)))
        cv2.imwrite('t.jpg', resized)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')

 # ============================================================================
 
if __name__ == '__main__':

    # clear old log file
    if os.path.exists("log.txt"):
        os.remove("log.txt")
    # set logger
    logging.basicConfig(filename="log.txt",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)
    logger = logging.getLogger('myapp')

    global car_count
    q = Queue.Queue(maxsize=0)
    
    # clear detected cars
    dirPath = "static/detected"
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        os.remove(dirPath+"/"+fileName)

    #start app
    app.run(host='0.0.0.0', debug=True, threaded=True)