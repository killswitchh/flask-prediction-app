import pickle
from joblib import dump  , load
import numpy as np
import os

class Predictor:
    def  __init__(self):
        self.folder_path = os.path.dirname(os.path.realpath(__file__))
        self.file_path = os.path.join(self.folder_path , "car.joblib")
        self.classifier = load(self.file_path)
        
    def calculate_probability(self,parameter_list):
        numpy_array = np.array([parameter_list])
        new_prediction = self.classifier.predict(numpy_array)
        answer = "The customer will buy the car" if new_prediction[0] == 1 else "The customer wont buy the car"
        return answer


