from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = 'tgyipksn14567'

#Have the root route render a template that displays the number of times the client has visited this site.
@app.route('/')
def index():
    return render_template("index.html")


if __name__=="__main__":
        app.run(debug=True)