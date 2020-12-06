# Program To Read video 
# and Extract Frames 
import cv2 
from os import listdir
from os.path import isfile, join
import os
import imutils
from moviepy.editor import *

def sortval(x):
    o = x.index("o")
    dot = x.index(".")
    return int(x[o+1:dot])


#function to trim
def trim(orignal,new):
    vid  = VideoFileClip(orignal)
    try:
    # vid = vid.rotate(90)
        edited = vid.subclip(0,3)
        edited.write_videofile(new,codec='libx264')
        return
    except:
        f = open("trimmer_log.txt", "a")
        f.write("Trimming Failed for {} \n".format(orignal))
        return

mypath = "inputvideos_unprocessed"
#accessing the word folders
subfolders = [f for f in listdir(mypath)]
try:
    subfolders.remove(".DS_Store")
except:
    pass

allvideos = []

# #lets access the video files now
for i in subfolders:
    foldername = os.getcwd()+"/"+mypath+"/"+i  #going to that directory
    videos = [foldername + "/" + f for f in listdir(foldername) if isfile(join(foldername, f))]
    allvideos.extend(videos)


#now for every video, we need to trim it down

for i in allvideos:
    reversePath = i[::-1] #reversing to get position from behind
    positionOfSlash = reversePath.index("/")
    videoname = reversePath[:positionOfSlash][::-1] #splitting and reversing again 
    if(".DS_Store" in i):
        pass
    elif("hello" in i):
        orignal_path = (os.getcwd()+"/inputvideos_unprocessed/hello/"+videoname)
        trim_path = (os.getcwd()+"/inputvideos_processed/hello/"+videoname)
        print("Ori:",orignal_path)
        print("New:",trim_path)
        trim(orignal_path,trim_path)
    elif("bye" in i):
        orignal_path = (os.getcwd()+"/inputvideos_unprocessed/bye/"+videoname)
        trim_path = (os.getcwd()+"/inputvideos_processed/bye/"+videoname)
        trim(orignal_path,trim_path)
    

