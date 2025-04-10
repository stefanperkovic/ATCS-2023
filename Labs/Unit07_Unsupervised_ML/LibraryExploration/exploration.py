import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('court.jpg')
img = cv2.resize(img, (2650, 1610))


# start_point = (0, 0) 
  
# # End coordinate, here (250, 250) 
# # represents the bottom right corner of image 
# end_point = (1250, 1250) 
  
# # Green color in BGR 
# color = (255, 0, 0) 
  
# # Line thickness of 9 px 
# thickness = 9
  
# # Using cv2.line() method 
# # Draw a diagonal green line with thickness of 9 px 
# img = cv2.line(img, start_point, end_point, color, thickness) 


# Python program to illustrate HoughLine
# method for line detection
import cv2
import numpy as np
 
# Reading the required image in
# which operations are to be done.
# Make sure that the image is in the same
# directory in which this python program is
 
# Convert the img to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Apply edge detection method on the image
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
 
# This returns an array of r and theta values
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
 
# The below for loop runs till r and theta values
# are in the range of the 2d array
for r_theta in lines:
    arr = np.array(r_theta[0], dtype=np.float64)
    r, theta = arr
    # Stores the value of cos(theta) in a
    a = np.cos(theta)
 
    # Stores the value of sin(theta) in b
    b = np.sin(theta)
 
    # x0 stores the value rcos(theta)
    x0 = a*r
 
    # y0 stores the value rsin(theta)
    y0 = b*r
 
    # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
    x1 = int(x0 + 1000*(-b))
 
    # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
    y1 = int(y0 + 1000*(a))
 
    # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
    x2 = int(x0 - 1000*(-b))
 
    # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
    y2 = int(y0 - 1000*(a))
 
    # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
    # (0,0,255) denotes the colour of the line to be
    # drawn. In this case, it is red.
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
 
# All the changes made in the input image are finally
# written on a new image houghlines.jpg
cv2.imwrite('linesDetected.jpg', img)

cv2.imshow("image", img)
cv2.waitKey(0)



# 1. Which library did you choose to explore?
# I choose to explore the OpenCV library for Computer Vision. 
# 2. Link the tutorial or hello world you tried.
# I used the GeeksforGeeks tutorial specifically the one on line detection using the Houghline method
# 3. What could you hope to create with this library?
# With this library you could create a way to detect parts of images. For the houghline specifically I am
# using it here for a tennis court to detect the lines. This could be usefull when evaluating whether a ball goes in or out. 
# 4. What difficulties do you anticipate when working with this library
# I antipate difficulties with getting the line detection to perfectly find the and detect the lines in the images 