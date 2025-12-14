import numpy as np
import time
import cv2 as cv
from matplotlib import pyplot as plt

cam1 = cv.VideoCapture(0)
cam2 = cv.VideoCapture(1)




while 1:
    _,img1 = cam1.read()
    _,img2 = cam2.read()

    cv.imwrite('1.png', img1)
    cv.imwrite('2.png', img2)

    imgL = cv.imread('2.png', cv.IMREAD_GRAYSCALE)
    imgR = cv.imread('1.png', cv.IMREAD_GRAYSCALE)
    
    stereo = cv.StereoBM.create(numDisparities=16, blockSize=17)
    disparity = stereo.compute(imgL,imgR)
    
    #cv.imshow('',disparity)
    plt.imshow(disparity,'gray')
    plt.show()
    
    