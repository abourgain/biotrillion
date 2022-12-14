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


# Load raw images in RGB and BGR format
def load_raw_image(image_path):
    bgr = cv.imread(image_path)
    rgb = cv.cvtColor(bgr, cv.COLOR_BGR2RGB)
    return rgb, bgr


def load_raw_images(imagePaths: str):
    bgrImages = []
    rgbImages = []
    for image_path in imagePaths:
        # bgr image
        rgb, bgr = load_raw_image(image_path)
        rgbImages.append(rgb)
        bgrImages.append(bgr)
    return rgbImages, bgrImages

# Images transformation to grayscale


def load_gray_image(image, blur_size: int = None):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    if blur_size is not None:
        gray = cv.GaussianBlur(gray, (blur_size, blur_size), 0)
    return gray


def load_gray_images(images: list, blur_size: int = None):
    grayImages = []
    for image in images:
        gray = load_gray_image(image, blur_size)
        grayImages.append(gray)
    return grayImages

# Images transformation with threshold


def threshdold_images(images, thres: int = 127, method=cv.THRESH_BINARY_INV):
    threshdoldImages = []
    for image in images:
        ret, thresh = cv.threshold(image, thres, 255, method)
        # open mask
        #thresh = cv.dilate(thresh, None, iterations=1)
        thresh = cv.erode(thresh, None, iterations=1)
        threshdoldImages.append(thresh)
    return threshdoldImages
