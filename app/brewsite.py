from flask import Flask
from flask import render_template as rt
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user = "Joshua Fraire")

@app.route("/breweries")
def breweries():
    return rt("breweries.html", user = "Joshua Fraire")

@app.route("/beer_types")
def beer_types():
    return rt("beer_types.html", user = "Joshua Fraire")

@app.route("/about")
def about():
    return rt("about.html", user = "Joshua Fraire")

if __name__ == "__main__":
    app.run(debug=True)