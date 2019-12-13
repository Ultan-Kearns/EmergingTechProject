import os
from keras.models import model_from_json
from tensorflow.python.framework import ops
#Reference - https://www.pytorials.com/deploy-keras-model-to-production-using-flask/
def init():
  json_file = open(os.getcwd() + '/model_json','r')
  loaded_model_json = json_file.read()
  json_file.close()
  loaded_model = model_from_json(loaded_model_json)
  #load weights into new model
  loaded_model.load_weights(os.getcwd() + "/trained.h5")
  print("Loaded Model from disk")
  #compile and evaluate loaded model
  loaded_model.compile(loss='sparse_categorical_crossentropy',optimizer='adadelta',metrics=['accuracy'])
  graph = ops.get_default_graph()
  return graph,loaded_model
