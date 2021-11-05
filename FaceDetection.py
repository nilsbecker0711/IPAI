#Author: Nils Becker


import numpy as np
import cv2
import mediapipe as mp
import face_recognition
import base64

cap = cv2.VideoCapture("w3r1.mp4")
#out = cv2.VideoWriter('w3r1_cv.avi',cv2.VideoWriter_fourcc(*'DIVX') , 25, (1280,720))     Creates new Video
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
FaceDetection = mpFaceDetection.FaceDetection(min_detection_confidence = 0.7)
frameCounter = 0
personCounter = 0
faces = {}
table = [] #Hold frames and samples for all ids, form: [[personId,[frames],[faceSamples]]]


def getFaces():
    '''
    This method decodes all saved faces
    '''
    #From FaceRecognition Lab xD
    face_bytes = dict((k, base64.b64decode(v)) for k, v in faces.items())   
    face_embeddings = dict((k, np.frombuffer(v, dtype=np.float) if len(v) > 0 else None) for k, v in face_bytes.items())
    return face_embeddings

while True:
    success, frame = cap.read()
    if frame is None: #last frame of video reached
        break
   
    cv2.putText(frame, f'Total persons in video: {personCounter}',(10,50), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2)
    frameCounter += 1
    newFace = True
    #Defines detection tolerance for part where participants wear masks
    if frameCounter > 1100:
        detectionCutOff = 0.2
    else:
        detectionCutOff = 0.35
    
    results = FaceDetection.process(frame)
    if results.detections: #faces are present
        for id, detection in enumerate(results.detections):
            bbox1 = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bbox1.xmin * iw), int(bbox1.ymin * ih), int(bbox1.width * iw), int(bbox1.height * ih)
           
            embedding = face_recognition.face_encodings(frame, known_face_locations=[bbox])
            face = base64.b64encode(embedding[0].tobytes())
            faces[personCounter] = face
            faceEmbeddings = getFaces()

            cv2.rectangle(frame, bbox, (0,255,0), 2)
                    
            if len(table) == 0: #gets called when first face is spotted
                personCounter += 1
                table.append([personCounter,[frameCounter],[face]])
                cv2.putText(frame, f'Person {personCounter}, Score{int(detection.score[0]*100)}%', (bbox[0],bbox[1]-10), cv2.FONT_HERSHEY_PLAIN, 1.2, (0,255,0), 1)
                
            else:
                embeddingsOnly = [x for x in faceEmbeddings.values() if x is not None]
                #strickt tolerance, leads to more different persons detected but differnciates better between faces
                comparisons = face_recognition.compare_faces(embeddingsOnly, faceEmbeddings[personCounter], tolerance = detectionCutOff)
                #Person is already spotted -> 
                #comparisons hold at least one "true" for the new face
                for i in range (len(comparisons[:-1])): 
                    if comparisons[i]:
                        #Get the face closest to found face
                        distance = face_recognition.face_distance(embeddingsOnly, faceEmbeddings[personCounter])
                        nameIdx = np.argmin(distance[:-1]) + 1
                        for entry in table:
                            if entry[0] == nameIdx:
                                entry[1].append(frameCounter)
                                entry[2].append(face)
                        newFace = False
                        cv2.putText(frame, f'Person{nameIdx}, Score{int(detection.score[0]*100)}%', (bbox[0],bbox[1]-10), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1)
                        break
                if (newFace):  #New Person found
                    personCounter += 1
                    cv2.putText(frame, f'Person{personCounter}, Score{int(detection.score[0]*100)}%', (bbox[0],bbox[1]-10), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1)
                    table.append([personCounter,[frameCounter],[face]])
                    
                
    #out.write(frame)   Write frame with boundling box etc. to new Video            
    cv2.imshow("press 'q' to quit",frame)
    if cv2.waitKey(1)==ord('q'):   
        break

print(f'Total persons in video:{personCounter}')

#out.release()
cap.release()
cv2.destroyAllWindows()
