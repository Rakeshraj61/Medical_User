from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd

#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/medclassify", methods=['GET', 'POST'])
def medclassify():

    #extract form inputs
    gender = request.form.get("gender")
    age = request.form.get("age")
    hypertension = request.form.get("hypertension")
    heartdisease = request.form.get("heartdisease")
    evermarried = request.form.get("evermarried")
    worktype = request.form.get("worktype")
    residencetype = request.form.get("residencetype")
    smokingstatus = request.form.get("smokingstatus")

   #convert data to json
    input_data = json.dumps({"gender": gender, "age": age, "hypertension": hypertension, "heartdisease": heartdisease, "evermarried": evermarried, "worktype": worktype,"residencetype":residencetype, "smokingstatus": smokingstatus})

    #url for bank marketing model
    url = "http://localhost:8080/api"
    # url = "https://bank-model-app.herokuapp.com/api"
  
    #post data to url
    results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    return render_template("index.html", gender = gender, age = age, hypertension = hypertension, heartdisease = heartdisease, evermarried = evermarried, worktype = worktype, residencetype=residencetype, smokingstatus = smokingstatus,  results=results.content.decode('UTF-8'))
  