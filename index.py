from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "hello"

@app.route("/bye")
def bye():
    return "bye world"


if __name__ == "__main__":
    app.run()

