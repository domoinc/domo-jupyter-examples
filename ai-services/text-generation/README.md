```The files in these examples are read only. To execute the files you will need to copy + paste the code, or download the files and upload them into your workspace.```

# Use the AI Service "Text Generation" in Jupyter

Example of using Text Generation in Jupyter

## Files
- textGenerationExample.ipynb - A Jupyter notebook with examples of using Text Generation

## Instructions

1. Import required library `import domojupyter.ai as ai`
2. Call `ai.generate_text()`

## Request Properties
* input - Required 
    * Prompt/question you are asking the Text-to-SQL service
* model - Optional 
    * Id of a specific model if using something other than default Domo model
* prompt_template - Optional 
    * Additional prompt template to use in request to Text-to-SQL
* parameters - Optional 
    * Any variables to be used with prompt_template 
    * Requires prompt_template to use

### Refer to the Jupyter notebook for specific examples