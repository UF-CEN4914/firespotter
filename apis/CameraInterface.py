from random import randint
from amcrest import AmcrestCamera
from amcrest import AmcrestError
import os
import datetime
import sys
import logging
import requests
import time

class CameraInterface(object):
    # TODO(AaronWilliams): I think a good strategy is to pull the image from the camera and store it locally
    # on the computer. Delete once a new frame is grabbed for the same camera. If we name image files
    # under a convention this will be trivial. Reduces overhead for storing images in our DB
    #https://python-amcrest.readthedocs.io/
    @staticmethod
    def fetchFrame(camera):
        logger = logging.getLogger(__name__)

        try:
            device = AmcrestCamera(host= camera.ip_address, port = 80, user = camera.username, password =camera.password).camera
            cwd = os.getcwd()
            img_path = '/Images/' + camera.short_name + '.png'  
            path =cwd +img_path 
            request = device.snapshot(path_file = path)
            if request._fp_bytes_read <1000:  
                raise AmcrestError            
            del device
            return img_path

        except AmcrestError:
            
            pwd = os.getcwd()
            camera_source = '/Images/cam_not_found.png'
            logging.error("Made an exception")
            logging.error(request._fp_bytes_read)
            logging.error(request.closed)
            return camera_source

        



    # TODO(AaronWilliams): This method should return the stream from the camera source we pass in.
    # Camera has: ip_address, username, password which should be sufficent in getting these.
    # Relevent link: https://stackoverflow.com/questions/56555938/show-ip-camera-live-feed-in-django-webpage
    
    @staticmethod
    def fetchFeed(camera):
        camera_source = "https://www.ready.gov/sites/default/files/2019-09/Wildfire%20toolkit_1.jpg"
        return camera_source
