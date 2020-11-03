from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_get():
    return "erdogan"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    #app.run(host='0.0.0.0', port=80)
