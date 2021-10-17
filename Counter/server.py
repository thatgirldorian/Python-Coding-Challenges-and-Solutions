from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = 'tgyipksn14567'

#Have the root route render a template that displays the number of times the client has visited this site.
@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

#Have the resetButton get it back to 1 when clicked
@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
        app.run(debug=True)