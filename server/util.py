import json
import pickle
import numpy as np

_locations = None
_data_columns = None
_model = None 

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = _data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(_data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(_model.predict([x])[0], 2)


def get_location_names():
    return _locations

def get_data_columns():
    return _data_columns    

def load_saved_artifacts():
    print("loading saved artifacts... start")
    global _data_columns
    global _locations
    global _model

    with open("server/artifacts/columns.json", "r") as f:
        _data_columns = json.load(f)['data_columns']
        _locations = _data_columns[3:]  #as locations is from column 3, first column index = 0

    if _model is None:
        with open("server/artifacts/Bangalore Real Estate Price Prediction.pickle", "rb") as f:
            _model = pickle.load(f)

if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_location_names())
    print("1st Phase Jp Nagar', 1000, 3, 3 : ")
    print(get_estimated_price('1st Phase Jp Nagar', 1000, 3, 3))

    print("'1st Phase Jp Nagar', 1000, 2, 2 : ")
    print(get_estimated_price('1st Phase Jp Nagar', 1000, 2, 2))

    print("'Indira Nagar', 800, 2, 2 : ")
    print(get_estimated_price('Indira Nagar', 800, 2, 2))

    print("'devarachikkanahalli', 1200, 3, 2 : ")
    print(get_estimated_price('devarachikkanahalli', 1200, 3, 2))

    print("'Ejipura', 950, 3, 2 : ")
    print(get_estimated_price('Ejipura', 950, 3, 2))

    print("'Indira Nagar', 800, 2, 2 : ")
    print(get_estimated_price('Indhhira Nagar', 800, 2, 2))
    

# dev bhut 