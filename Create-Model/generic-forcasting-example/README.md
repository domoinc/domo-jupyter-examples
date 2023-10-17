# Generic Forecasting example

This is an example of creating a generic forecasting model in Jupyter

## Files

Files included in this example: 
 
- generic.ipynb - A Jupyter notebook containing instructions and code to create a generic forcasting model
- forecast_generic.py - The entrypoint for invoking the model. The `invoke(data, content_type_header, accept_header)` function must be implemented in order to deploy the model as an Endpoint or using the Model Inference Magic tile.

## Instructions

In order to execute the notebook and create the model, do the following:

1. Upload generic.ipynb and forecast_generic.py to a Domo Jupyter Workspace.
2. Follow the instructions in generic.ipynb and execute all cells.


Optionally, start an endpoint for real-time inference:

1. Find the created model in Domo's Model Management Interface.
2. Go to the "Endpoint" tab and start the endpoint
3. Once started, enter test data in the "Input"
4. Click the "Test Model" button and view the prediction in the Output
5. Stop the Endpoint