import dlib
import numpy as np
from skimage import io
import cv2
import os


#stage 1
#getting the coordinates
predictor_path = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)


def sortval(x):
    e = x.index("e")
    dot = x.index(".")
    return int(x[e+1:dot])

from os import listdir
from os.path import isfile, join
mypath = "frames"

count = 0

i = "frame1.jpg"
img = cv2.imread("frame2.jpg")

dets = detector(img)

#output face landmark points inside retangle
#shape is points datatype
#http://dlib.net/python/#dlib.point
for k, d in enumerate(dets):
    shape = predictor(img, d)

vec = np.empty([68, 2], dtype = int)
for b in range(68):
    vec[b][0] = shape.part(b).x
    vec[b][1] = shape.part(b).y

# print("Shape of the image is:",img.shape) #height width and number of colour chanels i guess
# print("Coordinates are:",vec[49:69])

#stage 3
#lets find the area of the lip
#49 - 60th coordinates tell us about the lip contour
#using the shoelace formulae
def PolygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

# examples
corners = vec[61:69]
print("Area is:")
print(PolygonArea(corners))

