from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = 'tgyipksn 14567'

#Have the root route render a template that displays the number of times the client has visited this site.
@app.route('/')
def render_session():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)