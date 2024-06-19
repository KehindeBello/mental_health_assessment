from flask import Flask, render_template, request
from utils import calculate_scores, interpret_results

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/home")
def assessment_form():
    return render_template("assessment.html")

@app.post("/home")
def submit():

    phq9scores = [int(request.form[f"phq9_{i}"]) for i in range(1,10)]
    gad7scores = [int(request.form[f"gad7_{i}"]) for i in range(1,8)]
    pss4scores = [int(request.form[f"pss_{i}"]) for i in range(1,5)]

    phq9_normalized, gad7_normalized, pss4_normalized, aggregate_score = calculate_scores(phq9scores, gad7scores, pss4scores)

    result, interpretation = interpret_results(phq9scores, phq9_normalized, gad7_normalized, pss4_normalized, aggregate_score)
    
    return render_template("result.html", assessment=result, interpretation=interpretation)
