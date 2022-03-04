from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "Mapa Mundi"

@app.route('/play')
def play0():
    return render_template('juegos.html', num= 3)

@app.route('/play/<int:num>')
def play1(num):
    return render_template('juegos.html', num = num)

@app.route('/play/<int:num>/<string:color>')
def play2(num, color):
    return render_template('juegos.html', num=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)