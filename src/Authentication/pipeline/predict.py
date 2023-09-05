import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import os


class PredictionPipeline:
    def __init__(self, file_name):
        self.file_name = file_name

    def predict(self):

        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        image_name = self.file_name
        test_image = load_img(image_name, target_size = (224, 224))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = "Healthy"
            return [{"image" : prediction}]
        else:
            prediction = "Coccidiosis"
            return [{"image" : prediction}]