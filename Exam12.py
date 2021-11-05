import torch
import cv2

#Cat is seen as "Dog by model"
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
frameCount = 0
framesWithCat=[]
frames = []
cap = cv2.VideoCapture("cat.mp4")

while True:
    frameCount += 1
    success, frame = cap.read()
    if frame is None:
        break
    results = model(frame)
    detections = results.pandas().xyxy[0]
    #print(detections['name'])
    xMin = detections['xmin']
    yMin = detections['ymin']
    xMax = detections['xmax']
    yMax = detections['ymax']
    try:
        names = detections['name']
        i=-1
        for name in names:
            i+=1
            if name == 'dog':
                x1,y1,x2,y2 = int(xMin[i]), int(yMin[i]), int(xMax[i]), int(yMax[i])
                framesWithCat.append([frameCount, [(x1, y1, x2, y2)]])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 1)
                cv2.putText(frame, "Cat", (x1,y1-10), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1)
    except:
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
        frames.append(frame)
        continue
    cv2.imshow("frame", frame)
    frames.append(frame)
    if cv2.waitKey(1)==ord('q'):   
        break

print(framesWithCat)

#Video: 640x360, 25fps
out = cv2.VideoWriter('cat_opencv.avi',cv2.VideoWriter_fourcc(*'DIVX'), 25, (640, 360))
for i in range(len(frames)):
    out.write(frames[i])