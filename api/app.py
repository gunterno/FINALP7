# Import all packages and libraries
import pandas as pd
import numpy as np
from flask import Flask, render_template, url_for, request
import pickle
import math
import base64
from zipfile import ZipFile
from lightgbm import LGBMClassifier

z = ZipFile("echantillon.zip")
dataframe = pd.read_csv(z.open('echantillon.csv'), encoding ='utf-8')
all_id_client = list(dataframe['SK_ID_CURR'].unique())

model = pickle.load(open('lgbm.pickle', 'rb'))
seuil = 0.6

app= Flask(__name__)


@app.route('/')
def home():
    return "Prédiction rapide (ajouté /predict?id_client=ID à l'URL) (échantillon de clients) essayez par exemple avec les id : 100001,100028,456202,100066,100074,100107,100128' "


@app.route('/predict', methods = ['GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    ID = request.args.get('id_client')
    ID = int(ID)
    if ID not in all_id_client:
        prediction="Ce client n'est pas répertorié"
    else :
        X = dataframe[dataframe['SK_ID_CURR'] == ID]
        X = X.drop(['SK_ID_CURR'], axis=1)

        #data = df[df.index == comment]
        probability_default_payment = model.predict_proba(X)[:, 1]
        if probability_default_payment >= seuil:
            prediction = "Prêt NON Accordé"
        else:
            prediction = "Prêt Accordé"

    return str(prediction)

# Define endpoint for flask
app.add_url_rule('/predict', 'predict', predict)


# Run app.
# Note : comment this line if you want to deploy on heroku
app.run()
app.run(debug=True)
