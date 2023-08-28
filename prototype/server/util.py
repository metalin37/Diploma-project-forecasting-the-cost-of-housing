import json
import pickle
import numpy as np

# функция для обработки входных данных 
def preprocess_and_predict(df_input, model):
    '''Pre-processes input data and makes predictions using the provided model.'''
    
    def log_data(df_input):
        df_output = df_input.copy()
        df_output['zipcode'] = df_output['zipcode'].astype(str)
        df_output['Year built'] = df_output['Year built'].astype(str)
        
        #scaler = MinMaxScaler()
        for column in ['baths', 'sqft', 'school_rating _mean', 'school_dist_min']:
            #df_output[column] = scaler.fit_transform(df_output[[column]])[:,0]
            df_output[column] = df_output[column].apply(lambda x: abs(x))
            constant = 1e-6
            df_output[column] = np.log(df_output[column] + constant)
        return df_output

    X_test = log_data(df_input)
    y_test_pred_loaded = model.predict(X_test)
    target = np.exp(y_test_pred_loaded)
    rounded_target = np.round(target)
    print(rounded_target)
    
    return rounded_target

# функция для загрузки названий колонок
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global data_columns
    global flatTypes
    global regions
    global cities
    global materialTypes

    with open("./artifacts/columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']
        flatTypes = data_columns[21:24]
        regions = data_columns[24:27]
        cities= data_columns[27:47]
        materialTypes = data_columns[47:60]

    global model
    if model is None:
        with open('./artifacts/best_cb_model.pkl', 'rb') as f:
            model = pickle.load(f)
    print("loading saved artifacts...done")    
