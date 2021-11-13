from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.email import Email

#Have the root route render the form
@app.route('/')
def index():
    return render_template("index.html")

#Have the "/result" route display the information from the form on a new HTML page
# @app.route('/create/survey',methods=['POST'])
# def create_survey():
#     #validate here with the class
#     if Survey.is_valid(request.form):
#         Survey.save(request.form)
#         return redirect('/result')
#     return redirect('/')

# @app.route('/result')
# def result():
#     return render_template('result.html', survey = Survey.get_last_survey())