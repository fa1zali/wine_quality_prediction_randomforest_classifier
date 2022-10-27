import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import json

loaded_model = pickle.load(open("saved_model/wine_trained_model.sav", 'rb'))
app = FastAPI()

class model_input(BaseModel):
    
    fixed_acidity : float
    volatile_acidity : float
    citric_acid : float
    residual_sugar : float
    chlorides : float
    free_sulfur_dioxide : int
    total_sulfur_dioxide : int
    density : float
    pH : float
    sulphates : float
    alcohol : float

@app.post("/get_wine_quality")
def get_wine_quality(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dct = json.loads(input_data)

    a = input_dct["fixed_acidity"]
    b = input_dct["volatile_acidity"]
    c = input_dct["citric_acid"]
    d = input_dct["residual_sugar"]
    e = input_dct["chlorides"]
    f = input_dct["free_sulfur_dioxide"]
    g = input_dct["total_sulfur_dioxide"]
    h = input_dct["density"]
    i = input_dct["pH"]
    j = input_dct["sulphates"]
    k = input_dct["alcohol"]

    input_list = [a,b,c,d,e,f,g,h,i,j,k]
    input_data_arr = np.asarray([input_list])

    prediction = loaded_model.predict(input_data_arr)
    if prediction[0] == 0:
        return {'result':'Bad Quality'}
    else:
        return {'result':'Good Quality'}