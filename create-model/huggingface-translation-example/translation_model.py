from transformers import pipeline

class EndpointHandler():     
    def __init__(self):         
        #initialize model  
        self.pipe = pipeline("translation", model="model-t5-base", tokenizer="tokenizer-t5-base")
        pass
        
    def invoke(self, data, **kwargs):         
        return self.pipe(data)

