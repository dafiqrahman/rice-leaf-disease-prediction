import keras 

def load_model():
    model = keras.models.load_model('mobilenetv2')
    return model