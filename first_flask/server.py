from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = 'tgyipksn14567'

#Have the root route render the form
@app.route('/')
def index():
    return render_template("index.html")

if __name__=="__main__":
        app.run(debug=True)