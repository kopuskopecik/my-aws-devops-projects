from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World."

@app.route("/second")
def second():
    return "This is the second page."

@app.route("/third/subthird")
def third():
    return "This is the subthird page."
    
@app.route("/forth/<string:id>")
def forth(id):
    return f"ID of this page is {id}"

print(__name__)

if __name__ == "__main__" :
    print(__name__)
    app.run(debug = True)  # It gives us errors.


