from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1> Home Page <h1>"

@app.route("/titanic")
def titanic():
    return "<h1> Titanic Page <h1>"

@app.route("/car")
def car():
    return "<h1> Car Page <h1>"

if __name__ == "__main__":
    app.run(debug=True)

