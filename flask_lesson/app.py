from flask import Flask

app = Flask(__name__)
@app.route('/')
@app.route('/<name>')
def index(name="Anonymous"):
    return "Hello, my frend, {}".format(name)
if __name__=='__main__':
    app.run(debug=True)
