from datetime import datetime

from flask import Flask, render_template, request, redirect
from werkzeug.exceptions import default_exceptions

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
    return render_template("index.html", users=users, default=datetime.utcnow)

@app.route('/create_user')
def new():
    return render_template('create.html')

@app.route('/create',methods=['POST'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')
# Don't forget to redirect after saving to the database.

#edit person with their id
@app.route('/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",user=User.get_one(data))

#show user iformation when id is passed
@app.route('/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show.html",user=User.get_one(data))


@app.route('/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')


#delete people when their id is passed
@app.route('/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)