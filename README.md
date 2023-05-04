# OpenCV Car Detection Tracking
Object Detection and Tracking using OpenCV.

In this short app I have applied the basic principles of object detection and tracking using OpenCV.

These are - in a nutshell - the main bullet points that have been approached:

+ **Global Thresholding**
+ **Binary Thresholding**
+ **Inverse-Binary Thresholding**
+ **Truncate Thresholding**
+ **Threshold to Zero**
+ **Inverted Threshold to Zero**

![Source Image Sequence](general.gif)

## Contents :
Object detection and tracking has numerous applications in computer vision, thus I wanted to summarize the main challenges we face when approaching a detection and tracking app in the following table. As we give solutions to challenges via built-in functions, I have only included the main functions used and a brief description of what it does.

| Function        |Action                                                                        |
|----------------:|------------------------------------------------------------------------------|
|cv2.threshold()   |We apply the threshold.|
|**cv2.THRESH_BINARY** | Binary Thresholding|
|**cv2.THRESH_BINARY_INV**| Inverse-Binary Thresholding|
|**cv2.THRESH_TRUNC**       |Truncate Thresholding|
|**cv2.THRESH_TOZERO** | Threshold to Zero|
|**cv2.THRESH_TOZERO_INV**|Inverted Threshold to Zero|

## Test Image used: 
I have used traffic_algo_github.mp4 that can be found in the repository.

![Source Image Sequence](source_1.jpg)
![Source Image Sequence](source_2.jpg)![Source Image Sequence](source_3.jpg)

## Summary:

```python
# Basic threhold example 
th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY); 
cv2.imwrite("opencv-threshold-example.jpg", dst); 
```
```python
# Thresholding with maxValue set to 128
th, dst = cv2.threshold(src, 0, 128, cv2.THRESH_BINARY); 
cv2.imwrite("opencv-thresh-binary-maxval.jpg", dst); 
```
```python
# Thresholding with threshold value set 127 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_BINARY); 
cv2.imwrite("opencv-thresh-binary.jpg", dst); 
```
```python
# Thresholding using THRESH_BINARY_INV 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_BINARY_INV); 
cv2.imwrite("opencv-thresh-binary-inv.jpg", dst); 
```
```python
# Thresholding using THRESH_TRUNC 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TRUNC); 
cv2.imwrite("opencv-thresh-trunc.jpg", dst); 
```
```python
# Thresholding using THRESH_TOZERO 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TOZERO); 
cv2.imwrite("opencv-thresh-tozero.jpg", dst); 
```
```python
# Thresholding using THRESH_TOZERO_INV 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TOZERO_INV); 
cv2.imwrite("opencv-thresh-to-zero-inv.jpg", dst);
```



