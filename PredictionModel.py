from joblib import  load
from my_tokenizer import tokenizer
class  Model :
    def __init__(self):
        self.model= load(filename="ARandomForestModel.joblib")
    def predict(self,data):
        return self.model.predict(data)