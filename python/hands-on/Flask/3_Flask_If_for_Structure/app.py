from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    first = "This is my first condition experience in Flask"
    return render_template("index.html", message = first)


@app.route("/for")
def for_example():
    names = ["Tom", "Angelina", "Tommy"]
    return render_template("for.html", names = names)

if __name__ == "__main__":
    app.run(debug = True)