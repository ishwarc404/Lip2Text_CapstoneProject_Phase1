# Program To Read video 
# and Extract Frames 
import cv2 
from os import listdir
from os.path import isfile, join
import os
import imutils

def sortval(x):
	o = x.index("o")
	dot = x.index(".")
	return (int(x[o+1:dot]))


# Function to extract frames 
def FrameCapture(subfolder,videoname,file): 
	
	# Path to video file 
	vidObj = cv2.VideoCapture(file) 

	# Used as counter variable 
	count = 1

	# checks whether frames were extracted 
	success = 1

	if(not os.path.exists(os.getcwd()+"/inputvideos_split/"+subfolder+"/"+videoname)):
		os.mkdir(os.getcwd()+"/inputvideos_split/"+subfolder+"/"+videoname)

	while success: 
		try:
			success, image = vidObj.read() 
			cv2.imwrite(os.getcwd()+"/inputvideos_split/"+subfolder+"/"+videoname+"/frame%02d.jpg" % count, image) 
			count+=1
		except:
			#not writing to a log as last frame will always give an error
			print("Done {}".format(subfolder+"/"+videoname))
			return
			

# Driver Code 
mypath = "inputvideos_processed"
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
        #orignal_path = (os.getcwd()+"/inputvideos_unprocessed/hello/"+videoname)
        FrameCapture("hello",videoname,os.getcwd()+"/inputvideos_processed/hello/"+videoname)
    elif("bye" in i):
        #orignal_path = (os.getcwd()+"/inputvideos_processed/bye/"+videoname)
        FrameCapture("bye",videoname,os.getcwd()+"/inputvideos_processed/bye/"+videoname) #passing the video path and number too and parent folder


