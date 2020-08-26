import pickle
from joblib import dump  , load
import numpy as np
import os

class Predictor:
    def  __init__(self):
        self.folder_path = os.path.dirname(os.path.realpath(__file__))

    def calculate_probability_car(self,parameter_list):
        file_path = os.path.join(self.folder_path , "car.joblib")
        classifier = load(file_path)
        numpy_array = np.array([parameter_list])
        new_prediction = classifier.predict(numpy_array)
        answer = "The customer will buy the car" if new_prediction[0] == 1 else "The customer wont buy the car"
        return answer

    def calculate_probability_titanic(self, parameter_list):
        return "Test"
