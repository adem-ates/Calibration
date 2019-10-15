#!/usr/bin/python
import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
"""
Input: directory path
Function: Initialize all images in the path
Output: the ndarray images[] as a global variable
"""
def initimages(directory, fileextension):
    global images
    images = []
    file_count = glob.glob(directory+fileextension)
    print('Number of Files in the directory:', len(file_count))
    for x in range(0, len(file_count)):
        img = cv2.imread(directory+'rpi%s.jpg' %x)
        img = np.array(img)
        images.append(img)
    global row, col, dim
    row, col, dim = images[0].shape
    print('Image features:', 'row:', row,'colum:', col,'dimension:', dim)

"""
input:
function: 
output:
"""
"""
def grayimages(images):
    global grayimage
    grayimage = []
    for x in range()
"""
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

initimages('/media/sf_VboxGemein/Calibration/', '*.jpg') #rpi%s.jpg')

img = images[0]


"""Test rgb to gray values transformation"""
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


"""
show image img and gray in two seperate windows
if plt.show() is in the function only one figure window
will be opened for each image
if its in the last line to figures will show up in each figure
"""
showimage(1, img)
showimage(2, gray)

plt.show()


print('done')
