# from tensorflow.keras.preprocessing.image import load_img,img_to_array
# from tensorflow.keras.applications.vgg16 import preprocess_input
# from tensorflow.keras.models import Model, load_model
from joblib import dump, load

# import cv2
import pickle
import numpy as np
import os

class Predictor:
    def  __init__(self):
        self.folder_path = os.path.dirname(os.path.realpath(__file__))

    @staticmethod
    def create_titanic_numpy_array(parameter_list):
        # parameter_list = [900, '1', 'female', 15, 2, 2, 10.0, 'C']
        age = float(parameter_list[3])
        siblings = parameter_list[4]
        parch = parameter_list[5]

        male = 1 if parameter_list[2] == "male" else 0
        female = 1 if parameter_list[2] == "female" else 0

        c = 1 if parameter_list[7] == "C" else 0
        q = 1 if parameter_list[7] == "Q" else 0
        s = 1 if parameter_list[7] == "S" else 0

        class_1 = 1 if parameter_list[1] == "1" else 0
        class_2 = 1 if parameter_list[1] == "2" else 0
        class_3 = 1 if parameter_list[1] == "3" else 0

        family_size = parch + siblings + 1
        fare_per_person = float(parameter_list[6] / family_size)

        reorganized_array = [age , siblings,parch,female,male,c,q,s, class_1, class_2,class_3,family_size,fare_per_person]
        return np.array([reorganized_array])

    def calculate_probability_car(self,parameter_list):
        file_path = os.path.join(self.folder_path , "data","car.joblib")
        classifier = load(file_path)
        numpy_array = np.array([parameter_list])
        new_prediction = classifier.predict(numpy_array)
        answer = "The customer will buy the car" if new_prediction[0] == 1 else "The customer wont buy the car"
        return answer

    def calculate_probability_titanic(self, parameter_list):
        file_path = os.path.join(self.folder_path , "data","titanic.joblib")
        classifier = load(file_path)
        numpy_array = self.create_titanic_numpy_array(parameter_list)
        new_prediction = classifier.predict(numpy_array)
        answer = "The Passenger will Survive" if new_prediction[0] == 1 else "The Passenger will not Survive"
        return answer
    
    def calculate_price_boston(self, parameter_list):
        file_path = os.path.join(self.folder_path , "data","boston.joblib")
        regressor = load(file_path)
        organized_array = list(map(float,parameter_list))
        numpy_array = np.array([organized_array])
        new_prediction = regressor.predict(numpy_array)
        answer = "median value of owner-occupied homes in $1000s : " + str(new_prediction[0])
        return answer

    def calculate_weight(self, parameter_list):
        file_path = os.path.join(self.folder_path , "data","height.joblib")
        regressor = load(file_path)
        organized_array = list(map(float,parameter_list))
        numpy_array = np.array([organized_array])
        new_prediction = regressor.predict(numpy_array)
        rounded = round(float(new_prediction[0]) , 4)
        answer = "Predicted Weight of the person : " + str(rounded) + " lbs"
        return answer

    def find_cat(self, picture):
        file_path = os.path.join(self.folder_path , "data","cat_or_not_cat.h5")
        print('jher;;')
        print(picture)
        #DUMMY IMPLEMENTATION
        return "<DUMMY ANSWER> The picture is not a CAT"



