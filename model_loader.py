import numpy as np
import tensorflow as tf
from tensorflow import keras


class model_loader:
    def __init__(self):
        self.model = keras.models.load_model('./my_model')

    def predict(self, new_input_flow):
        new_input_flow = new_input_flow.reshape((1, 10, 1))
        predicted_output_flow = self.model.predict(new_input_flow)
        return predicted_output_flow[0][0]

