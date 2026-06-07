from application import app
from flask import render_template, request, json, jsonify
import requests

# Home page
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

# Student classification route
@app.route("/studentclassify", methods=['GET', 'POST'])
def studentclassify():

    # Extract form inputs
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

    # Build JSON payload
    input_data = json.dumps({
        "course": course,
        "sneeds": sneeds,
        "debtor": debtor,
        "tuition": tuition,
        "gender": gender,
        "scholarship": scholarship,
        "age": age,
        "international": international,
        "first_enrolled": first_enrolled,
        "first_approved": first_approved,
        "second_enrolled": second_enrolled,
        "second_approved": second_approved
    })

    # URL for ML API
    url = "http://localhost:5000/api"

    # POST request with correct headers
    results = requests.post(url, data=input_data, headers={"Content-Type": "application/json"})

    # Render results
    return render_template(
        "index.html",
        course=course, sneeds=sneeds, debtor=debtor, tuition=tuition,
        scholarship=scholarship, age=age, gender=gender,
        international=international, first_enrolled=first_enrolled,
        first_approved=first_approved, second_enrolled=second_enrolled,
        second_approved=second_approved, results=results.content.decode('UTF-8')
    )
