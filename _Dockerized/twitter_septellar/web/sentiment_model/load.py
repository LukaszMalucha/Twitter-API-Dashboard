from keras.models import model_from_json
import tensorflow as tf
import os.path

## PATHS ############################################################################


my_path = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(my_path, "../sentiment_model/sentiment_model.h5")
model_weights_path = os.path.join(my_path, "../sentiment_model/sentiment_model.json")


## Compile graph from saved sentiment_model
def init_model():
    json_file = open(model_weights_path, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(model_path)
    print("Loaded Sentiment Analysis Model")

    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    graph = tf.get_default_graph()

    return loaded_model, graph
