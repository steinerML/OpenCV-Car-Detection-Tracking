import cv2
from object_tracker import *

#This line was written after fine-tuning the object detection object
tracker = EuclideanDistTracker()

#We create the capture object
capture = cv2.VideoCapture("traffic algo\highway\highway.mp4")

#1-Object detector extractor through mask
#object_detector = cv2.createBackgroundSubtractorMOG2()
#Improved detection via parameters!
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=80)

#start the loop that goes through each and every frame

while True:
    ret,frame = capture.read()
    height, width, _ = frame.shape
    # print(height,width)

    #Region of Interest (ROI)

    roi = frame[340:720,500:800]

    mask = object_detector.apply(roi) #We apply mask to every frame
    _, mask = cv2.threshold(mask, 254,255,cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    detections = [] #Empty array to add coordinates

    for cnt in contours:

        #Calculate unwanted area and remove small elements
        area = cv2.contourArea(cnt)

        if area > 100:
            #cv2.drawContours(roi,[cnt], -1, (0,255,0), 2)
            x,y,w,h = cv2.boundingRect(cnt)
            # cv2.rectangle(roi,(x,y),(x + w, y + h), (0,255,0), 3)
            detections.append([x,y,w,h])
   
   #2 - Object Tracking
    box_id = tracker.update(detections)
    for box in box_id:
        x,y,w,h,id = box
        cv2.putText(roi,str(id), (x,y - 15),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,255),1)
        cv2.rectangle(roi,(x,y),(x + w, y + h), (0,255,0), 3)
    cv2.imshow("ROI", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(10)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()