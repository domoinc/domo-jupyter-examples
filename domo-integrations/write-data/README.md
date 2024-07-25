```The files in these examples are read only. To execute the files you will need to copy + paste the code, or download the files and upload them into your workspace.```

# Write data from Jupyter to Domo

Example of how to write data from a Jupyter notebook to a Domo DataSet

## Files
- ExampleWriteData.ipynb - A Jupyter notebook with a simple example of pushing data to a Domo Dataset

## Instructions
In order to add data to a Domo Dataset do the following: 

#### Before running your workspace

1. When creating or updating a workspace choose the optional step "Output DataSets"
2. Select the button "Add Output DataSet"
3. Give your new DataSet a name
4. Click "Save Workspace" to apply your dataset

### After updating/creating a workspace

1. Start your workspace
2. Create a new notebook (or update an existing notebook)
3. On the left navigation there is a DataSet icon
    - Use this to view the output DataSets you have configured for the workspace
    - Optionally double-click on the dataset name to pre-populate starting code to use the DataSet. Skip steps 4 - 6 

In Jupyter we use pandas.DataFrame to work with data. We will be using Pandas for our example. 
- See more documentation on Pandas: [documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

4. Import the domojupyter asset
    - `import domojupyter as domo`

    If you are creating your own sample data you will want to import pandas `import pandas as pd`

  
5. Create the data you wish to output to a DataSet
6. Create a variable and assign it to the value of `domo.write_dataframe(output, 'Dataset Name')`
    - "Output" is a variable with your pandas dataFrame
