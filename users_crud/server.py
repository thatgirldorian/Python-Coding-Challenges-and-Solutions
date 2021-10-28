from flask import Flask, render_template, redirect, request, url_for
from flask.globals import session

# import the class from user.py
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)

@app.route('/create_user')
def result():
    return render_template('create.html')

@app.route('/create', methods=['GET','POST'])
def create_user():
    if request.method == "POST":
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
        data = {
            "fname": request.form["fname"],
            "lname" : request.form["lname"],
            "email" : request.form["email"]
        }
    # We pass the data dictionary into the save method from the User class.
        User.save(data)
        return (url_for(render_template("create.html")))
    else:
        return redirect('/')
    # Don't forget to redirect after saving to the database.
    

            
if __name__ == "__main__":
    app.run(debug=True)