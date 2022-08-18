import numpy as np
import keras.optimizers as optimizers
import keras.backend as K
from keras.models import model_from_config, Sequential, Model

def clone_model(model, custom_objects={}):
    config = {
        'class_name': model.__class__.__name__,
        'config': model.get_config(),
    }
    cloned_model = model_from_config(config, custom_objects=custom_objects)
    cloned_model.set_weights(model.get_weights)
    return cloned_model
