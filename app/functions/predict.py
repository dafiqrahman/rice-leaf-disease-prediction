import tensorflow as tf
import numpy as np


def predict(model, image):

    class_names = ['Bakteri Hawar Daun', 'Bercak Coklat', 'Padi Sehat', 'Penyakit Blast', 'Daun Lepuh', 'Bercak Coklat Sempit']
    image = image.resize((256,256))
    image_array = np.array(image)
    image_tensor = tf.cast(image_array, tf.float32)
    image_tensor = tf.expand_dims(image_tensor, 0)
    predictions = model.predict(image_tensor)
    score = predictions[0]
    #argmax return index of max value
    class_index = np.argmax(score)
    #get class name from class_names
    class_name = class_names[class_index]
    #return class names and green if class_name is healthy else red
    if class_name == 'Padi Sehat':
        score = f"<p class = 'center fs-2 green' > {class_name} </p>"
    else:
        score = f"<p class = 'center fs-2 red' > {class_name} </p>"
    return score, class_name