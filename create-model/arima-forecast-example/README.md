# ARIMA Forecasting example

This is an example of creating a forecasting model in Jupyter

## Files

Files included in this example: 
 
- arima.ipynb - A Jupyter notebook containing instructions and code to create a forcasting model
- forecast_arima.py - The entrypoint for invoking the model. The `EndpointHandler` class must be implemented in order to deploy the model as an Endpoint or using the Model Inference Magic tile.

## Instructions

In order to execute the notebook and create the model, do the following:

1. Upload arima.ipynb and forecast_arima.py to a Domo Jupyter Workspace.
2. Follow the instructions in arima.ipynb and execute all cells.


Optionally, start an endpoint for real-time inference:

1. Find the created model in Domo's Model Management Interface.
2. Go to the "Endpoint" tab and start the endpoint
3. Once started, enter test data in the "Input"
4. Click the "Test Model" button and view the prediction in the Output
5. Stop the Endpoint