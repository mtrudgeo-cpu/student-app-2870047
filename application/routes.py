from application import app
from flask import render_template, request
import joblib
import numpy as np
import os

_model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model.joblib')
_clf = joblib.load(_model_path)['model']

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/studentclassify", methods=['GET', 'POST'])
def studentclassify():
    course         = request.form.get("course")
    sneeds         = request.form.get("sneeds")
    debtor         = request.form.get("debtor")
    tuition        = request.form.get("tuition")
    gender         = request.form.get("gender")
    scholarship    = request.form.get("scholarship")
    age            = request.form.get("age")
    international  = request.form.get("international")
    first_enrolled = request.form.get("first_enrolled")
    first_approved = request.form.get("first_approved")
    second_enrolled = request.form.get("second_enrolled")
    second_approved = request.form.get("second_approved")

    features = np.array([[
        int(course), int(sneeds), int(debtor), int(tuition),
        int(gender), int(scholarship), int(age), int(international),
        int(first_enrolled), int(first_approved),
        int(second_enrolled), int(second_approved),
    ]])
    prediction = _clf.predict(features)[0]

    return render_template(
        "index.html",
        course=course, sneeds=sneeds, debtor=debtor, tuition=tuition,
        gender=gender, scholarship=scholarship, age=age,
        international=international, first_enrolled=first_enrolled,
        first_approved=first_approved, second_enrolled=second_enrolled,
        second_approved=second_approved,
        results=prediction,
    )
