import numpy as np
import tensorflow as tf
from tensorflow import keras
from os.path import isfile
from util.logger import log

class model_loader:
    def __init__(self):
        self.__model = None

    def load_model(self):
        if not self.__model == None:
            return True
        if not isfile('./my_model'):
            return False
        try:
            self.__model = keras.models.load_model('./my_model')
            return True
        except:
            return False

    def predict(self, new_input_flow, new_time_zones):
        if self.__model == None:
            raise Exception("Please load model first.")
        new_input_flow = new_input_flow.reshape((1, 10, 1))
        new_time_zones = new_time_zones.reshape((1, 10, 1))
        predicted_output_flow = self.__model.predict([new_input_flow, new_time_zones])
        return predicted_output_flow[0][0]

