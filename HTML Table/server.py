from flask import Flask, render_template
app = Flask(__name__)

#http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/dict')
def render_dic():

            users_info = [
    {'first_name' : 'Cherechi', 'last_name' : 'Grace'},
    {'first_name' : 'Simisola', 'last_name' : 'Adeoluwa'},
    {'first_name' : 'Omolara', 'last_name' : 'Elizabeth'},
    {'first_name' : 'Zubby', 'last_name' : 'Amaechi'}
    ]
            return render_template("index.html", users=users_info)

if __name__=="__main__":
    app.run(debug=True)