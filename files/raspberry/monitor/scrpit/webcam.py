#!/opt/monitor/venv/bin/python

from datetime import datetime
import time
import cv2
import numpy as np
import sys
import logging
import os

logging.basicConfig(stream=sys.stdout, format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO)

minutes=1
wait=minutes*60

def main():
    while True:
        try:
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
            cap.set(cv2.CAP_PROP_FRAME_WIDTH,  1920) #3840
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080) #2160

            ret, image = cap.read()
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            now = datetime.now()
            current_time = now.strftime("%H%M")
            #            cv2.imwrite("out/pic_"+current_time+".png", image)

            cv2.imwrite("/opt/monitor/out/webcam.png", image)
            logging.info("Save webcam.png : ".format(current_time))
            os.popen("scp /opt/monitor/out/webcam.png ymmon:/monitor/www/html/webcam1/")
            time.sleep(wait)
            cap.release()
        except KeyboardInterrupt:
            logging.info('Good bye')
            break
        except:
            logging.exception('Exception')
            time.sleep(wait)

if __name__ == '__main__':
    main()

