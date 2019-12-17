from random import randint

class CameraInterface(object):
    # TODO(AaronWilliams): I think a good strategy is to pull the image from the camera and store it locally
    # on the computer. Delete once a new frame is grabbed for the same camera. If we name image files
    # under a convention this will be trivial. Reduces overhead for storing images in our DB
    @staticmethod
    def fetchFrame(camera):
        image_urls = [
            "https://www.ready.gov/sites/default/files/2019-09/Wildfire%20toolkit_1.jpg",
            "https://cdn.5280.com/2018/09/wildfires-lede_ap-images-1280x720.jpg",
            "https://cdn.mos.cms.futurecdn.net/UyPZMiJU8DSntDZ3yMEptB-320-80.jpg",
            "https://www.positive.news/wp-content/uploads/2019/03/feat-1800x0-c-center.jpg",
            "https://miro.medium.com/max/10670/0*wDfweQrKYCvDXWk7",
            "https://daily.jstor.org/wp-content/uploads/2016/10/Moving_Forest_1050_700.jpg"
        ]
        return image_urls[randint(0, len(image_urls)-1)]

    # TODO(AaronWilliams): This method should return the stream from the camera source we pass in.
    # Camera has: ip_address, username, password which should be sufficent in getting these.
    # Relevent link: https://stackoverflow.com/questions/56555938/show-ip-camera-live-feed-in-django-webpage
    
    @staticmethod
    def fetchFeed(camera):
        camera_source = "https://www.ready.gov/sites/default/files/2019-09/Wildfire%20toolkit_1.jpg"
        return camera_source