from typing import Optional

from fastapi import FastAPI
from DataModel import DataModel
import pandas as pd
from joblib import load

from logic import tokenizer


import string
import json
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from PredictionModel import Model
from fastapi import FastAPI, File, UploadFile
import io
from fastapi.responses import FileResponse

app = FastAPI()


# Mount the 'static' directory as '/static'
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    # Serve the 'index.html' file as the main page
    return FileResponse("templates/index.html")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

#se debe recibir un archivo con varias reviews

# se recibe la ruta del archivo

@app.post("/predict")

# se recibe la ruta del archivo y se hace la prediccion
@app.post("/predict")
async def make_predictions(file: UploadFile = File(...)):
    # Get the contents of the uploaded file
    contents = await file.read()
    
    # Process the contents of the file and make predictions
    df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
    model=Model()
    df=df['review_text'] + " " + df['title']
    result=model.predict(df)
    #result will be the number of positive reviews and negative reviews
    positive=result.tolist().count(1)
    negative=result.tolist().count(0)

    return {"positive": positive, "negative": negative}
