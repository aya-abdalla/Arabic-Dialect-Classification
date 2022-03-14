import numpy as np
from flask import Flask, request, jsonify, render_template
#from sklearn.feature_extraction.text import CountVectorizer
from ipynb.fs.full.Data_preprocessing import clean_unicode
import pickle
import pandas as pd
app = Flask(__name__)
model = pickle.load(open('MultinomialNB.pkl', 'rb'))
vectorizer=pickle.load(open('vector.pickel', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    text = request.form.values()
   # text=clean_unicode(text)
    X2 = vectorizer.transform(text)
    prediction = model.predict(X2)
  
    output = prediction[0]

    return render_template('index.html', prediction_text='Text most likely to be  {}'.format(output))
     
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    
    mytext=list(data.values())
    X2 = vectorizer.transform(mytext)
    prediction = model.predict(X2)

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
