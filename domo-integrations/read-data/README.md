```The files in these examples are read only. To execute the files you will need to copy + paste the code, or download the files and upload them into your workspace.```

# Read Data into Jupyter

Example of how to read data from a Domo DataSet and use it in a Jupyter Notebook

## Files
- ExampleReadData.ipynb - A Jupyter notebook with a simple example of adding a Domo DataSet to a notebook

## Instructions
In order to use a DataSet in a notebook do the following: 

#### Before running your workspace

1. When creating or updating a workspace choose the optional step "Input DataSets"
2. Select the button "Add Input DataSet"
3. Choose a DataSet

Optionally, give the dataset a different alias

4. Click "Save Workspace" to apply your dataset

### After updating/creating a workspace

1. Start your workspace
2. Create a new notebook (or update an existing notebook)
3. On the left navigation there is a DataSet icon
    - Use this to view the input DataSets you have configured for the workspace
    - Optionally double-click on the dataset name to pre-populate starting code to use the DataSet. Skip steps 4 - 5 

In Jupyter we use pandas.DataFrame to work with data. We will be using Pandas for our example. 
- See more documentation on Pandas: [documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

4. Import the domojupyter asset
    - `import domojupyter as domo`
5. Create a variable and assign it to the value of `input = domo.read_dataframe('dataset_name', query='SELECT * FROM table')`

## Notes
* You can update the query parameter to change what data is pulled from the DataSet
* You can output data into a Domo DataSet (see other example)
