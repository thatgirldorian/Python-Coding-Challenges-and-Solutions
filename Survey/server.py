from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = 'tgyipksn14567'

#Have the root route render the form
@app.route('/')
def index():
    return render_template("index.html")

#Have the "/result" route display the information from the form on a new HTML page
@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=="__main__":
        app.run(debug=True)