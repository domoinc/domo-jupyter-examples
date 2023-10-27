# Use the AI Service "Text-to-SQL" in Jupyter

Example of using Text-to-SQL in Jupyter

## Files
- textToSqlExample.ipynb - A Jupyter notebook with examples of using Text-to-SQL

## Instructions

1. Import required library `import domojupyter.ai as ai`
2. Call `ai.text_to_sql()`

## Request Properties
* input - Required 
    * Prompt/question you are asking the Text-to-SQL service
* data_source_schemas - Required
    * Optional if using dataFrame or workspace_data_source_alias
* dataframe - Required 
    * Optional if using data_source_schemas or workspace_data_source_alias
    * pandas dataframe for the data or dataset you are using in your text-to-sql request
        * See more documentation on Pandas: [documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
* workspace_data_source_alias - Required
    * Optinal if using data_source_schemas or dataframe
    * Use this option if using a Domo Dataset and no additional data transformation is needed before making the request
* model - Optional 
    * Id of a specific model if using something other than default Domo model
* prompt_template - Optional 
    * Additional prompt template to use in request to Text-to-SQL
* parameters - Optional 
    * Any variables to be used with prompt_template 
    * Requires prompt_template to use

### Refer to the Jupyter notebook for specific examples