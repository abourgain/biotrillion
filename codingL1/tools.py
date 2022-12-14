import numpy as np
import argparse
import cv2 as cv
import os
import imutils
from matplotlib import pyplot as plt
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
from math import sqrt


# Canny detection for the images
def canny_detection(images, t_lower, t_upper, aperture_size, erode=True, dilate1=True, dilate2=True):
    edgedImages = []
    for image in images:
        edged = cv.Canny(image, t_lower, t_upper)  # , aperture_size)
        if dilate1:
            edged = cv.dilate(edged, None, iterations=1)
        if erode:
            edged = cv.erode(edged, None, iterations=1)
        if dilate2:
            edged = cv.dilate(edged, None, iterations=1)
        edgedImages.append(edged)
    return edgedImages

# Dilatation on images


def dilate_image(image, kernel=np.ones((5, 5), np.uint8), iterations=1):
    return cv.dilate(image, kernel, iterations=iterations)


def dilate_images(images, kernel=np.ones((5, 5), np.uint8), iterations=1):
    results = []
    for image in images:
        image = dilate_image(image, kernel, iterations=iterations)
        results.append(image)
    return results

# Erosion on images


def erode_image(image, kernel=np.ones((5, 5), np.uint8), iterations=1):
    return cv.erode(image, kernel, iterations=iterations)


def erode_images(images, kernel=np.ones((5, 5), np.uint8), iterations=1):
    results = []
    for image in images:
        image = erode_image(image, kernel, iterations=iterations)
        results.append(image)
    return results

# Define the kernel for erosion or dilatation


def kernel(val: int):
    return cv.getStructuringElement(cv.MORPH_ELLIPSE, (val, val))

# Define the distance between two points


def distance(ptA, ptB):
    return sqrt((ptA[0] - ptB[0])**2 + (ptA[1] - ptB[1])**2)
