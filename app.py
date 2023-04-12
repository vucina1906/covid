from flask import Flask,request,render_template
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from predict_pipeline import CustomData,PredictPipeline
from sklearn.impute import SimpleImputer

application=Flask(__name__)
app=application

#Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else: # CustomData get values after user post it on html home page. It use request.for and take values from key(keys are name from div containers in home.html)
        data = CustomData(
            USMER = request.form.get('USMER', ""),
            MEDICAL_UNIT = request.form.get('MEDICAL_UNIT', ""),
            SEX = request.form.get('SEX', ""),
            HOSPITALIZED = request.form.get('HOSPITALIZED', ""),
            PNEUMONIA = request.form.get('PNEUMONIA', ""),
            AGE = request.form.get('AGE', ""),
            PREGNANT = request.form.get('PREGNANT', ""),
            DIABETES = request.form.get('DIABETES', ""),
            COPD = request.form.get('COPD', ""),
            ASTHMA = request.form.get('ASTHMA', ""),
            INMSUPR = request.form.get('INMSUPR', ""),
            HIPERTENSION = request.form.get('HIPERTENSION', ""),
            OTHER_DISEASE = request.form.get('OTHER_DISEASE', ""),
            CARDIOVASCULAR = request.form.get('CARDIOVASCULAR', ""),
            OBESITY = request.form.get('OBESITY', ""),
            RENAL_CHRONIC = request.form.get('RENAL_CHRONIC', ""),
            TOBACCO = request.form.get('TOBACCO', ""),
            ANTIGEN_TEST = request.form.get('ANTIGEN_TEST', ""),
            AGE_GROUP = request.form.get('AGE_GROUP', "")
            )
        
        pred_df = data.get_data_as_data_frame()#convert data to dataframe for prediction,using function from predict pipeline
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)