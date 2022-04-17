from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is sharon. Trna understand web"

if __name__ == '__main__' :
    app.run(debug=True)
