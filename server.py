from flask import Flask, render_template  # added render_template!
app = Flask(__name__)

@app.route('/play')
def play(x=3):
    return render_template('index.html', x = x) # returns the result of the render_template method, passing in the name of our HTML file

@app.route('/play/<int:x>')
def play_box(x):
    return render_template('index.html', x = x)

@app.route('/play/<int:x>/<color>')
def play_boxes(x, color):
    return render_template('index.html', x = x, color = color)


if __name__=="__main__":
    app.run(debug=True)