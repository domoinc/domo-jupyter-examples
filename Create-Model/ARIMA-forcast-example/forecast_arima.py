import pickle
import pandas as pd
import numpy as np
from pathlib import Path
from sktime.forecasting.arima import AutoARIMA

def invoke(data, content_type_header, accept_header):
    
    fh = np.arange(1, 25)
    #load model
    path_to_mdl = str(Path(__file__).parent.resolve()) + '/models/arima.mdl'
    print(path_to_mdl)
    forecaster= pickle.load(open(path_to_mdl, 'rb'))
    y_pred = forecaster.predict(fh)
    result = y_pred.to_csv(header=False)
    return result

print('this is a test')