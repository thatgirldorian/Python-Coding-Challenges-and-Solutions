from flask import Flask, render_template, request, redirect

# import the class from user.py
from user import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route("/users")
def users():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)

@app.route('/create_user')
def new():
    return render_template('create.html')

@app.route('/create',methods=['POST'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')
    # Don't forget to redirect after saving to the database.

if __name__ == "__main__":
    app.run(debug=True)