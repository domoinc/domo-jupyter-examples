import pandas as pd
from io import StringIO

class EndpointHandler():
    def __init__(self):
        """Initialize model"""
        pass
        
    def invoke(self, data, **kwargs):
        """Invoke the model using data as the input

        :param data: The input data
        
        :Keyword Arguments:
            * *content_type_header* str: The Content-Type header, or MediaType of the input data
            * *accept_header* str: The Accept header, or expected MediaType of the response
            
        :return: The model prediction
        """
        # Read csv input
        input_data = pd.read_csv(StringIO(data), header=None).to_numpy()

        # "predict" that the input is blue (1) if the color is Blue, otherwise 0
        predictions = [1 if entry[1] == 'Blue' else 0 for entry in input_data]

        # Convert and return predictions as csv
        return pd.DataFrame(predictions).to_csv(header=False, index=False)