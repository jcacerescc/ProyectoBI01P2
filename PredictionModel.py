from joblib import  load

class  Model :
    def __init__(self,columns):
        self.model= load(filename="model.joblib")



    def predict(self,data):
        return self.model.predict(data)