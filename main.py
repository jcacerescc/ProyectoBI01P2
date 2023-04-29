from typing import Optional

from fastapi import FastAPI
from DataModel import DataModel
import pandas as pd
from joblib import load
app = FastAPI()
import nltk

from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from langdetect import detect
from nltk import pos_tag


from num2words import num2words

# create tokenizer
tokenizer = RegexpTokenizer(r'\w+')

# create lemmatizer
lemmatizer = WordNetLemmatizer()

# function to map part-of-speech tags to WordNet POS tags
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return 'a' # Adjetivo
    elif treebank_tag.startswith('V'):
        return 'v' # Verbo
    elif treebank_tag.startswith('N'):
        return 'n' # Sustantivo
    elif treebank_tag.startswith('R'):
        return 'r' # Adverbio
    else:
        return 'n' # Sustantivo por defecto

# function to tokenize and lemmatize text
def tokenizer(text):
    # detect language of text
    language = detect(text)

    # initialize spellchecker based on language
    if language == 'es':
        # tokenize Spanish text
        tokens = nltk.word_tokenize(text, language='spanish')
    else:
        # tokenize English text
        tokens = nltk.word_tokenize(text)

    # remove non-alphanumeric characters
    tokens = [token for token in tokens if token.isalnum()]
    
    # transform numbers from digit format to word format
    tokens = [num2words(token) if token.isnumeric() else token for token in tokens]

    # lemmatize tokens
    tokens = [lemmatizer.lemmatize(token, pos=get_wordnet_pos(pos_tag([token])[0][1])) for token in tokens]
    
    

    return tokens

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

#se debe recibir un archivo con varias reviews

# se recibe la ruta del archivo

@app.post("/predict")

def make_predictions(dataModel: DataModel):
    
    print('model loading')
    df = pd.read_csv('./HotelsReviewsPruebas.csv')
    print('model loading')
    print(df.head(5))
    model = load('./model.joblib')

    df=df['review_text'] + " " + df['title']
    result = model.predict(df)
    return {"prediction": result[0]}




