import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")

#loading the saved model
loaded_model = pickle.load(open('C:/Users/yashu/Desktop/IOE/trainedmmodel.sav', 'rb'))


new_data = [[60.0, 38.0]]
predictions = loaded_model.predict(new_data)
if predictions==['Normal']:
    print("Your Heartrate and body temperature is Abnormal")
else:
    print("Your Heartrate and body temperature is Normal")
