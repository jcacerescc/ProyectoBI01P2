import nltk

from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from langdetect import detect
from nltk import pos_tag

from num2words import num2words
from sklearn.pipeline import make_pipeline
from joblib import dump, load
import numpy as np
import pandas as pd
from my_tokenizer import tokenizer




filename = 'model.joblib'

#model = load(filename)
 
