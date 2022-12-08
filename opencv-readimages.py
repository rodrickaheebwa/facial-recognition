import os
import cv2 as cv

# load and read image, return as a matrix of pixels
# img = cv.imread("known-faces/rodrick/cocis_window.jpg")

# resizing frames for performance
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# displays image in new window
# cv.imshow('rodrick', img)

# resized image
# resized_img = rescaleFrame(img)
# cv.imshow('rodrick_resized', resized_img)

for filename in os.listdir('known-faces/rodrick'):
    img = cv.imread(os.path.join("known-faces/rodrick", filename))
    img = rescaleFrame(img, 0.5)
    cv.imshow('Rodrick Images', img)
    cv.waitKey(0)

# cv.waitKey(5000)