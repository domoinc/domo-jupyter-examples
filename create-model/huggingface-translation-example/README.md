## Hugging Face translation model example

This example demonstrates how to create a model using the Hugging Face library and upload it to Domo's Model Management interface.

> This model is using Hugging Face's model : https://huggingface.co/t5-base

## Files

- TranslationModel.ipynb - A Jupyter notebook containing instructions and code to create the Hugging Face translation model, and upload it to Domo's Model Management interface.
- translation_model.py - The entrypoint for invoking the Hugging Face translation model. The `EndpointHandler` class must be implemented in order to deploy the model as an Endpoint or using the Model Inference Magic tile.
- PreModelSetup.ipynb - A Jupyter notebook containing instructions and code to download the Hugging Face model and tokenizer, to be done before creating the model.
- TestModel.ipynb - A Jupyter notebook containing instructions and code to test the Hugging Face model.

## Instructions

In order to execute the notebook and create the model, do the following:

1. Upload PreModelSetup.ipynb, TranslationModel.ipynb, and translation_model.py to a Domo Jupyter Workspace.
2. Follow the instructions in PreModelSetup.ipynb and execute all cells.
3. Optionally, follow the instructions in TestModel.ipynb to test you model before deploying the model to Domo's model management.
4. Follow the instructions in TranslationModel.ipynb and execute all cells.


Optionally, start an endpoint for real-time inference:

1. Find the created model in Domo's Model Management Interface.
2. Go to the "Endpoint" tab and start the endpoint
3. Once started, enter test data in the "Input" (e.g. `Translate this sentence`)
4. Click the "Test Model" button and view the prediction in the Output
5. Stop the Endpoint