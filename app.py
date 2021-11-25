from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

#### Creating object of Standard Scaler


#### Loading the pickle Files

scalar=pickle.load(open("standard_scaler.pickle","rb"))
model = pickle.load(open('finalized_model.pickle', 'rb'))

#### Defining the routes
@app.route('/',methods=['GET'])
def Home():
    return render_template('index12.html')



@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

        ### Requesting all the data from Frontend Server and saving  into a variables

        age = int(request.form['age'])
        sex =request.form['sex']
        if sex=="male":
            d=1
        else:
            d=0
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker =request.form['smoker']
        if smoker=="yes":
            smoker=1
        else:
            smoker=0
        region = request.form['region']
        if region=="region_northwest":
            a=0
            b=0
            c=1
        elif region=="region_southeast":
            a=0
            b=1
            c=0
        elif region=="region_southwest":
            a=1
            b=0
            c=o
        else:
            a=0
            b=0
            c=0

       ## Applying the Scaling

        
        prediction=model.predict([[age,d,bmi,children,smoker,a,b,c]])
        return render_template("index12.html",prediction_number=prediction)
    else:
        return  "something wrong"

if __name__=="__main__":
    app.run(debug=True)
