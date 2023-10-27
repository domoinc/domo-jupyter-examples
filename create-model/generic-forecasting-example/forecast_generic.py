import pickle
import pandas as pd
import numpy as np
from sktime.forecasting.arima import AutoARIMA
from sktime.forecasting.ets import AutoETS
from io import StringIO

class EndpointHandler():
    def __init__(self):         
        #initialize model  
        pass

    def invoke(self, data, **kwargs):         
        fh = np.arange(1, 25)
        
        df = pd.read_csv(StringIO(data), names=['date', 'value'])
        df['date'] = pd.to_datetime(df['date'])
        df['value'] = df['value'].astype(float)
        
        df.index = df['date']
        df.index.freq = df.index.inferred_freq
        
        y_train = df['value']

        forecaster = AutoARIMA(sp=12, suppress_warnings=True)
        # forecaster = AutoETS(sp=12, auto=True)
        forecaster.fit(y_train)
        
        y_pred = forecaster.predict(fh) 
        result = y_pred.to_csv(header=False)
        
        return result