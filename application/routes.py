from application import app
from flask import render_template, request
import json
import requests

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/studentclassify", methods=['GET', 'POST'])
def studentclassify():

    #extract form inputs
    course = request.form.get("course")
    sneeds = request.form.get("sneeds")
    debtor = request.form.get("debtor")
    tuition = request.form.get("tuition")
    scholarship = request.form.get("scholarship")
    age = request.form.get("age")
    gender = request.form.get("gender")
    international = request.form.get("international")
    first_enrolled = request.form.get("first_enrolled")
    first_approved = request.form.get("first_approved")
    second_enrolled = request.form.get("second_enrolled")
    second_approved = request.form.get("second_approved")

    #extract data from json
    input_data = json.dumps({"course": course, "sneeds": sneeds, "debtor": debtor, "tuition": tuition, "scholarship": scholarship,
                             "age":age, "gender":gender,"international":international,"first_enrolled":first_enrolled,"first_approved":first_approved,
                             "second_enrolled":second_enrolled,"second_approved":second_approved})

    #url for car classification api
    url = "http://localhost:5000/api"

    #post data to url
    results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    return render_template("index.html", course = course, sneeds = sneeds, debtor = debtor, tuition = tuition, scholarship = scholarship,
                           age = age, gender=gender,international=international,first_enrolled=first_enrolled,
                            first_approved=first_approved,second_enrolled=second_enrolled,
                            second_approved=second_approved, results=results.content.decode('UTF-8'))
