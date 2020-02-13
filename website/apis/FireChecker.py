import torch
from models.WildfireModel import WildfireModel
import cv2
import numpy as np

IMG_SZ = 100

class FireChecker():

    wildfire_model = torch.load('./models/wfm.pt') 

    @staticmethod
    def IsWildFire(img_path):
        #  read the image and resize it 
        img = cv2.imread(img_path)
        img = cv2.resize(img, (IMG_SZ, IMG_SZ))

        # convert the image to a tensor and view it in the form that the model expects (3 channels, IMG_SZxIMG_SZ)
        img = (torch.tensor(img)/255.0).view(-1,3,IMG_SZ,IMG_SZ)

        #  run the image through the model and grab the 0th result (returns a list bc of batching)
        output = FireChecker.wildfire_model(img)[0]

        # output is a probability, 0 is no fire and 1 is fire
        predicted_class = np.round(output.detach())

        # cast the predicted class to a boolean
        if predicted_class == 1: return True
        else: return False