from flask import Flask, render_template
app = Flask(__name__)

#When a user visits http://localhost:5000/play, have it render three beautiful looking blue boxes. 
@app.route('/play')
def index():
    return render_template("index.html", times=3)

#When a user visits localhost:5000/play/(x), have it display the beautiful looking blue boxes x times. 
@app.route('/play/<int:times>')
def show_box(times):
    return render_template("index.html", times=int(times))

#Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value 
@app.route('/play/<int:times>/<color>')
def change_color(times, color):
    return render_template("index.html", times=int(times), color=(color))

if __name__=="__main__":
    app.run(debug=True)

