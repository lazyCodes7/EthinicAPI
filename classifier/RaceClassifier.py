from __future__ import print_function, division
import warnings
warnings.filterwarnings("ignore")
import os.path
import pandas as pd
import torch
import torch.nn as nn
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import os
import argparse
import cv2
class RaceClassifier:
    def __init__(self,model_path):
        ## Loading the Resnet34 pretrained model
        self.model = torchvision.models.resnet34(pretrained=True)
        # Selecting the device
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # Output has lots of features like the age, race which sum upto 18
        self.model.fc = nn.Linear(self.model.fc.in_features, 18)
        #model_fair_7.load_state_dict(torch.load('fair_face_models/fairface_alldata_20191111.pt'))

        # Loading the pretrained model trained on the Fairface dataset
        self.model.load_state_dict(torch.load(model_path,map_location=torch.device('cpu')))
        self.model = self.model.to(self.device)

        # Setting eval mode to not compute gradients
        self.model.eval()
    
    # Predict function used to predict the race of the face detected
    def predict(self,cvImage):
            trans = transforms.Compose([
                        transforms.ToPILImage(),
                        transforms.Resize((224, 224)),
                        transforms.ToTensor(),
                        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
            ])
            # img pth of face images
            # list within a list. Each sublist contains scores for all races. Take max for predicted race
            # image = cv2.imread(cvImage) 
            image = cv2.cvtColor(cvImage, cv2.COLOR_BGR2RGB)        
            image = trans(image)
            image = image.view(1, 3, 224, 224)  # reshape image to match model dimensions (1 batch size)
            image = image.to(self.device)

            # fair
            outputs = self.model(image)
            outputs = outputs.cpu().detach().numpy()
            outputs = np.squeeze(outputs)

            race_outputs = outputs[:7]
            gender_outputs = outputs[7:9]
            age_outputs = outputs[9:18]

            race_score = np.exp(race_outputs) / np.sum(np.exp(race_outputs))
            gender_score = np.exp(gender_outputs) / np.sum(np.exp(gender_outputs))
            age_score = np.exp(age_outputs) / np.sum(np.exp(age_outputs))

            race_pred = np.argmax(race_score)
            gender_pred = np.argmax(gender_score)
            age_pred = np.argmax(age_score)

            return (race_pred,gender_pred,age_pred)
