```The files in these examples are read only. To execute the files you will need to copy + paste the code, or download the files and upload them into your workspace.```

# Blue Classification

Blue Classification is a simple classification model that serves as an introduction for creating models in Domo's Jupyter Workspace environment.

## Files

Files included in this example:

- blue.ipynb - A Jupyter notebook containing instructions and code to create the Blue Classification model, and upload it to Domo's Model Management interface.
- model.py - The entrypoint for invoking the Blue Classification model. The `EndpointHandler` class must be implemented in order to deploy the model as an Endpoint or using the Model Inference Magic tile.

## Instructions

In order to execute the notebook and create the model, do the following:

1. Upload blue.ipynb and model.py to a Domo Jupyter Workspace.
2. Follow the instructions in blue.ipynb and execute all cells.


Optionally, start an endpoint for real-time inference:

1. Find the created model in Domo's Model Management Interface.
2. Go to the "Endpoint" tab and start the endpoint
3. Once started, enter test data in the "Input" (e.g. `Diamond,Blue`)
4. Click the "Test Model" button and view the prediction in the Output
5. Stop the Endpoint