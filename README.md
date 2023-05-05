# OpenCV Car Detection Tracking
Object Detection and Tracking using OpenCV.

In this short app I have applied the basic principles of object detection and tracking using OpenCV.

These are - in a nutshell - the main bullet points that have been approached:

+ **Object Detector creation**
+ **Mask creation**
+ **Mask Thresholding (254-255)**
+ **Creation of ROI (Region of Interest)**
+ **Apply Mask to ROI**
+ **Detect Objects in ROI**
+ **Apply Tracker**

![Source Image Sequence](general.gif)

## Contents :
Object detection and tracking has numerous applications in computer vision, thus I wanted to summarize the main challenges we face when approaching a detection and tracking app in the following table. As we give solutions to challenges via built-in functions, I have only included the main functions used and a brief description of what each one does.

| Function            |Action                                                                        |
|:--------------------|------------------------------------------------------------------------------|
|*_Object Detection_*||
|project.py           | Main app|
|**cv2.VideoCapture()**   |We create the capture object|
|**cv2.createBackgroundSubtractorMOG2()** | Object Detector (background subtractor through mask)|
|**object_detector.apply()**| Apply object detector both to frame and roi.|
|**cv2.findContours()**     |Extract coordinates from mask.|
|**cv2.drawContours()**    | Draw contours.|
|**cv2.contourArea()**|Calculate Area.|
|**roi = frame[x1 : x2, y1 : y2]**|Extract region of intrest (ROI)|
|**cv2.createBackgroundSubtractorMOG2(history,varThreshold)**   |Improve Detection via history & varThreshold.|
|**cv2.boundingRect(),cv2.rectangle()**|Draw rectangle based on contour.|
|**cv2.drawContours()**    | Draw contours.|
|**cv2.threshold(mask, colour1, colour2,cv2.THRESH_BINARY)**    | Apply threshold to mask.colour1 & colour 2 range 0-255 BGR.|
|*_Object Tracking_*||
|object_tracker.py           | Tracker class|
|```from object_tracker import *```    | Import tracker so we can load EuclideanDistTracker class.|
|**tracker = EuclideanDistTracker()**    | Create object tracker.|
|**tracker.update(detections)**    | Tracker update.|
|**detections = []**    | Empty list to store object coordinates (x, y, w, h).|
|**cv2.putText()**    | Add text.|
|**cv2.rectangle()**    | Add rectangle.|







## Test Image used: 
I have used traffic_algo_github.mp4 that can be found in the repository.

![Source Image Sequence](source_1.jpg)![Source Image Sequence](source_2.jpg)

## Region of Interest (ROI):
![Source Image Sequence](roi_1.jpg)![Source Image Sequence](roi_2.jpg)


## Mask:
![Source Image Sequence](mask_1.jpg)![Source Image Sequence](mask_2.jpg)

## Issues:
Several issues around the detection and tracking algorithm can be spotted if we take a closer look at some of the screenshots provided.
Most of the issues are related with:

+ Camera Instability.
+ Lighting Granularity.
+ Shade Inconsistency.
+ Poor Colour Thresholding.

![Source Image Sequence](source_3.jpg)

## Summary:

```python
# Create object detector via a mask
object_detector = cv2.createBackgroundSubtractorMOG2()
```
```python
# Create object detector (improved with parameters)
cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=10)
```
```python
# Find contours of the objects in the mask
cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
```
```python
# Calculate area delimited by the contours (so we can impose a conditional later)
cv2.drawContours(roi,[cnt], -1, (0,255,0), 2)
```
```python
# Define Region of Interest (ROI)
roi = frame[340:720,500:800]
```
```python
#Apply the mask to ROI
object_detector.apply(roi)
```
```python
#Apply the mask to frame
object_detector.apply(frame)
```
```python
#Extract coordinates from contours
contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
```
```python
#Calculate area of contours
area = cv2.contourArea(cnt)
```
```python
#Define Region of Interest (ROI)
roi = frame[340:720,500:800]
```
```python
#Apply mask to ROI
mask = object_detector.apply(roi)
```
```python
#Improved detection via parameters!
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=80)
```
```python
#Draw rectangle based on contours
x,y,w,h = cv2.boundingRect(cnt)
```
```python
#Find contours
contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
```
```python
#Apply threshold to mask
 _, mask = cv2.threshold(mask, 254,255,cv2.THRESH_BINARY)
```
```python
#Create object tracker
tracker = EuclideanDistTracker()
```
```python
#Define empty list for object detection coordinates.
detections = []
```
```python
#Append coordinates to list
detections.append([x,y,w,h])
```
```python
#Update detections with box id
box_id = tracker.update(detections)
```
```python
#Add text (id number)
cv2.putText(roi,str(id), (x,y - 15),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,255),1)
```
```python
#Draw rectangle
cv2.rectangle(roi,(x,y),(x + w, y + h), (0,255,0), 3)
```
```python
#Print all windows (Source, Mask, ROI)
cv2.imshow("Frame", frame)
cv2.imshow("Mask", mask)
cv2.imshow("ROI", roi)
```


