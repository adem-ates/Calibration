#!/usr/bin/python
import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Input: directory path
Function: Initialize all images in the path
Output: the ndarray images[] as a global variable
"""
def initimages(directory):
    global images
    images = []
    for x in range(1, 6):
        img = cv.imread(directory %x)
        img = np.array(img)
        images.append(img)

"""
input: figure number (n), image name (img)
function: shows image with matplotlib images viewer
output: a window named after (n), x- and y-axes not defines but in pixels
"""
        
def showimage(n, img):
    plt.figure(n)
    plt.imshow(img)

"""
input:
function: 
output:
"""


"""
input:
function: 
output:
"""


initimages('/media/sf_VboxGemein/Calibration/rpi%s.jpg')

img = images[0]

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

showimage(1, img)
showimage(2, gray)

plt.show()


print 'done'
