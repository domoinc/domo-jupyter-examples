from transformers import pipeline
import pathlib
import json

class EndpointHandler():     
    def __init__(self):         
        #initialize model  
        path = pathlib.Path(__file__).parent.resolve()
        self.pipe = pipeline("translation", model=f"{path}/model-t5-base", tokenizer=f"{path}/tokenizer-t5-base")
        pass
        
    def invoke(self, data, **kwargs):         
        return json.dumps(self.pipe(data))

