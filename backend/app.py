from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hey this is coming flask backend"


if __name__ == '__main__':
    app.run(debug=True)