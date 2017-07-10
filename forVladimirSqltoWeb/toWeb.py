from flask import Flask


app = Flask(__name__)
@app.route("/")
@app.route("/<name>")
def index(name="User"):
    return "{}".format(name)
if __name__== '__main__':
    app.run()
