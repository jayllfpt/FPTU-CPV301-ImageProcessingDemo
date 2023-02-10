import numpy as np
import cv2

# img = cv2.imread('ColorChecker.jpg')
img = cv2.imread('fuji.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"


def function1(alpha, beta, img=img):
    # color balance base on alpha and beta
    imgNew = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    cv2.imshow('func1', imgNew)
    return imgNew


def function2(img=img):
    # show histogram
    #  equalize
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    # equalize the histogram of the Y channel
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    # convert the YUV image back to RGB format
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    cv2.imshow('func2', img_output)
    return img_output


def function3(img=img):
    # median filter
    imgNew = cv2.medianBlur(img, 3)
    cv2.imshow('func3', imgNew)
    return imgNew


def function4(img=img):
    # mean filter
    imgNew = cv2.blur(img, (5, 5))
    cv2.imshow('func4', imgNew)
    return imgNew


def function5(img=img):
    # gaussian filtering
    imgNew = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imshow('func5', imgNew)
    return imgNew


alpha = float(input("Enter alpha: "))
beta = float(input("Enter beta: "))
function1(alpha, beta)
function2()
function3()
function4()
function5()
cv2.waitKey(0)
