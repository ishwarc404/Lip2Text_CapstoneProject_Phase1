import dlib
import numpy as np
from skimage import io
import cv2
import os
from os import listdir
from os.path import isfile, join
import pandas as pd

#predictor data
predictor_path = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

#sorting function key
def sortval(x):
    e = x.index("e")
    dot = x.index(".")
    return int(x[e+1:dot])

def foldersort(x):
    return int(x)

def PolygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area



def final_area(frame_path):
    
    try:
        img = cv2.imread(frame_path)
        dets = detector(img)
        # print("im there")
        #output face landmark points inside retangle
        #shape is points datatype
        #http://dlib.net/python/#dlib.point
        for k, d in enumerate(dets):
            shape = predictor(img, d)
        # print("im here again")
        vec = np.empty([68, 2], dtype = int)
        # print("im 2")
        for b in range(68):
            vec[b][0] = shape.part(b).x
            vec[b][1] = shape.part(b).y
        corners = vec[61:69]
        area = (PolygonArea(corners))
        # print("Frame name:",frame_path)
        # print("Area:",area)
        print("Frames to Area: Happening")
        return area

    except:
        return -1
    

#initial dataset path list
#we will iterate through this
paths = ["inputvideos_split/hello","inputvideos_split/bye"] #,"NEWDATASET/apple_frames","NEWDATASET/banana_frames"]


folders = []
for mypath in paths:
    frame_parent_folders = [f for f in listdir(mypath)]
    try:
        frame_parent_folders.remove(".DS_Store")
    except:
        pass

    folders.append(frame_parent_folders)


#now we have a 2D array
#[[all folders in hello], [all folders in bye]]

count = -1
parent_area_array = []
for folder_list in folders:
    parent_area_array = []
    count+=1
    flag = True
    for each_parent_folder in folder_list:
        path = os.getcwd()+"/"+paths[count]+"/"+each_parent_folder 
        frames = sorted([f for f in listdir(path) if isfile(join(path, f))])
        #this gives all the frames in that folder now
        #we need to get the area of each of these frames
        areas = []
        for each_frame in frames:
            if(each_frame!=".DS_Store"):
                areas.append(final_area(path +"/"+each_frame))
        print("DONE: {}".format(path))
        try:
            area_max = max(areas)
            new_areas = [i/area_max for i in areas]
            new_areas.append(paths[count][paths[count].index("/")+1:])
            parent_area_array.append(new_areas)
            if(len(parent_area_array)==0):
                flag = False
        except:
            pass

    if(flag):
        df = pd.DataFrame(parent_area_array)
        # if(os.path.exists("datasets"+paths[count][paths[count].index("/"):]+"data.csv")):
        #     df_old = pd.read_csv("datasets"+paths[count][paths[count].index("/"):]+"data.csv")
        #     df_old = df_old.drop(columns=["Unnamed: 0"]) #dropping the initial indexing column
        #     new_df = df_old.append(df)
        #     new_df.to_csv("datasets"+paths[count][paths[count].index("/"):]+"data.csv")
        # else:
        df.to_csv("datasets"+paths[count][paths[count].index("/"):]+"data.csv")
        



