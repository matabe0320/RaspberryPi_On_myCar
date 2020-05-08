import picamera
import time
import os
from datetime import datetime

PICTURE_WIDTH = 1280
PICTURE_HEIGHT = 720
SAVEDIR = "/home/pi/画像/camera"
RECORD_SECONDS = 300 #5分間撮影
RECORD_FILES = 36 #5分*36=3時間撮影

cam = picamera.PiCamera()
cam.resolution = (PICTURE_WIDTH, PICTURE_HEIGHT)
cam.rotation = 180

cam.start_preview(fullscreen=False,window=(0,10,480,260))
time.sleep(2)

while(True):
    cDatetime = datetime.now()
    filename =  cDatetime.strftime("%Y%m%d-%H%M%S") + ".h264"
    save_file = SAVEDIR +"/"+ filename

    cam.start_recording(save_file)
    cam.wait_recording(RECORD_SECONDS)
    cam.stop_recording()
    
    files = os.listdir(SAVEDIR)
    if len(files) > RECORD_FILES:
        files.sort() #ファイル名一覧を昇順にソート
        for i in range(len(files)-RECORD_FILES):
            os.remove(SAVEDIR + "/" + files[i]) #先頭からファイルを削除

#cam.stop_preview()