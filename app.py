import numpy as np
from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)
df1 = pd.read_csv('try.csv')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    c=request.form.get('LocationID',None)
    n=request.form.get('Nod',None)
    n=int(n)
    data=df1[c]
    data=np.array(data)
    day=df1['Index']
    data=data[0:n]
    day=np.array(day)
    return render_template("index.html",dataz=zip(data, day))

if __name__ == "__main__":
    app.run(debug=True)