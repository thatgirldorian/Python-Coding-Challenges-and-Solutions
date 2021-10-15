from flask import Flask, render_template
import numpy
app = Flask(__name__)

#http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def index():
    return render_template("index.html", num_row=8, num_col=8)

#http://localhost:5000 - should display 8 by 4 checkerboard
@app.route('/4')
def show_halfBoard():
    return render_template("index.html", num_row=4, num_col=8)

#http://localhost:5000/(x)/(y) - should display x by y checkerboard
@app.route('/<int:num_row>/<int:num_col>')
def show_random(num_row, num_col):
    return render_template("index.html", num_row=int(num_row), num_col=int(num_col))

#Have another route accept 4 parameters and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route('/<int:num_row>/<int:num_col>/<color1>/<color2>')
def show_diffColor(num_row, num_col, color1, color2):
    return render_template("index.html", num_row=int(num_row), num_col=int(num_col), color1=(color1), color2=(color2))

if __name__=="__main__":
    app.run(debug=True)