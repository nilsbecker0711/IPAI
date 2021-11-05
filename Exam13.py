import torch
import cv2


model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
vid = cv2.VideoCapture("cut.mp4")

while True:
    _, frame = vid.read()
    if frame is None:
        break
    results = model(frame)
    detections = results.pandas().xyxy[0]
    names = detections['name']
    confidences = detections['confidence']
    xMin = detections['xmin']
    yMin = detections['ymin']
    xMax = detections['xmax']
    yMax = detections['ymax']
    for i in range (len(names)):
        x1, y1, x2, y2 = int(xMin[i]), int(yMin[i]), int(xMax[i]), int(yMax[i])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 2)
        cv2.putText(frame, f'{names[i]}, Confidence:{confidences[i]}', (x1,y1-10), cv2.FONT_HERSHEY_PLAIN, 1, (0,0, 255), 1)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break

