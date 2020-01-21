from random import randint
from amcrest import AmcrestCamera

class CameraInterface(object):
    # TODO(AaronWilliams): I think a good strategy is to pull the image from the camera and store it locally
    # on the computer. Delete once a new frame is grabbed for the same camera. If we name image files
    # under a convention this will be trivial. Reduces overhead for storing images in our DB
    #https://python-amcrest.readthedocs.io/
    @staticmethod
    def fetchFrame(camera):
        device = AmcrestCamera(camera.ip_address, 80, camera.username, camera.password).camera
        pic = camera.snapshot()
        f = open('file.jpeg', 'wb')
        f.write(pic.read())
        return f.name

    # TODO(AaronWilliams): This method should return the stream from the camera source we pass in.
    # Camera has: ip_address, username, password which should be sufficent in getting these.
    # Relevent link: https://stackoverflow.com/questions/56555938/show-ip-camera-live-feed-in-django-webpage
    
    @staticmethod
    def fetchFeed(camera):
        camera_source = "https://www.ready.gov/sites/default/files/2019-09/Wildfire%20toolkit_1.jpg"
        return camera_source