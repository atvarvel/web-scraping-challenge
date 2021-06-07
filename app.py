from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# MongoDB connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def home():

    mars_data = mongo.db.collection.find_one()

    # Return data and render template
    return render_template("index.html", mars=mars_data)


@app.route("/scrape")
def scrape():

    # Call scrape function to get updated data
    mars_data = scrape_mars.scrape()
    # Update database
    mongo.db.collection.update({}, mars_data, upsert=True)
    # Return to home page
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)