from flask import Flask, render_template

app = Flask(__name__, template_folder="C:/Users/JABER/MyGames/templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game1')
def game1():
    return render_template('game1.html')

@app.route('/game2')
def game2():
    return render_template('game2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
