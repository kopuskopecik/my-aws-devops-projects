from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def head():
    return render_template("index.html", number1 = 150, number2 = 200)


@app.route("/second")
def seconds():
    return render_template("second.html")


if __name__ == "__main__" :
    app.run(debug = True)  