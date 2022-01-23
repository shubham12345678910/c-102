from distutils.command.upload import upload
from email.mime import image
from mmap import ACCESS_READ
from tracemalloc import Snapshot, start
import cv2
import random
import time
import dropbox
start_time=time.time()

def takeSnapshot():
    videocapture=cv2.VideoCapture(0)
    result=True 
    while(result):
        number=random.randint(0,100)
        ret,frame=videocapture.read()
        #we are going to use imwrite()to save the image in the device
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        start_time=time.time
        result=False
    
    return imagename
    print("Snapshot is taken")
    videocapture.release()
    cv2.destroyAllWindows()
    
def uploadfile(imagename):
    access_token='YYenz_cMo78AAAAAAAAAAW4wOmJOk7lqHnkEkguwNhDHx3r0UK3L30pqsYhguabr'
    file=imagename
    filefrom=file
    fileto="/testfolder"+(imagename)
    dbx = dropbox.Dropbox(access_token)
    with open(filefrom,'rb') as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("File is susccessfully uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=takeSnapshot()
            uploadfile(name)
main()

    