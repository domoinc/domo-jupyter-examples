```The files in these examples are read only. To execute the files you will need to copy + paste the code, or download the files and upload them into your workspace.```

# Use the AI Service "Text-Summarization" in Jupyter

Example of using Text-Summarization in Jupyter

## Files
- textSummarizationExample.ipynb - A Jupyter notebook with examples of using Text-Summarization

## Instructions

1. Import required library `import domojupyter.ai as ai`
2. Call `ai.summarize()`

## Request Properties
* input - Required 
    * Text you are trying to summarize with the Text-Summarization service
* chunking_configuration - Optional
    * `ChunkingConfiguration(max_chunk_size, chunk_overlap, list_of_separators, separator_type, disallow_intermediate_chunks)`
        * `max_chunk_size` : Number
        * `chunk_overlap` : Number
        * `list_of_separators` : List of Strings
        * `separator_type` : String
        * `disallow_intermediate_chunks` : Boolean
* output_style - Optional
* output_word_length - Optional
    * `SizeBoundary(min,max)`
* model - Optional 
    * Id of a specific model if using something other than default Domo model
* prompt_template - Optional 
    * Additional prompt template to use in request to Text-Summarization
* parameters - Optional 
    * Any variables to be used with prompt_template 
    * Requires prompt_template to use

### Refer to the Jupyter notebook for specific examples