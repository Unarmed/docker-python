from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/reverse", methods = ["POST"])
def reverse():
    reverse = request.get_data()[::-1]
    return reverse

if __name__ == "__main__":
    app.run()
