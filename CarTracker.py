#Author: Becker

import cv2 as cv

vid = cv.VideoCapture("video.mp4")

#Object Detector -> Focus on important objects
detector = cv.createBackgroundSubtractorMOG2(history = 100, varThreshold = 50)

while True:
   
    red, frame = vid.read()
    height, width, _ = frame.shape

    #Region of interest -> Road
    roi = frame[127:240, 0:]
    mask = detector.apply(roi)
  
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_TC89_KCOS)
    detections = []
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 100:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(roi, (x, y), (x+w, y+h), (0,0,255), 2) 
            detections.append([x, y, w, h])
        #trails: represent vehicle size
        for detection in detections:
            if detection[1] > 55:
                cv.line(roi, (detection[0], detection[1]+int(detection[3]/2)), (int(detection[0]-(detection[2]*detection[3])/10), detection[1]+int(detection[3]/2)), (0,255,0), 2)
            else:
                cv.line(roi, (detection[0]+detection[2], detection[1]+int(detection[3]/2)), (int((detection[0]+detection[2]) + (detection[2]*detection[3])/10), detection[1]+int(detection[3]/2)),(255,0,0) , 2)

    cv.imshow("Video (press 'q' to quit)", frame)
    if cv.waitKey(1) == ord('q'):
        break
cv.release()
cv.destroyAllWindows()

