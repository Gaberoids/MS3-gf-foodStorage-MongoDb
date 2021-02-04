import os
from flask import (Flask, flash, render_template, redirect, request, url_for)
from flask_pymongo import PyMongo
# from bson.objectid import ObjectId
# from werkzeug.security import generate_password_hash, chech_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_items")
def get_items():
    print("caraca")
    flash('flashfreaking message')
    items_list = list(mongo.db.items.find())
    return render_template("items.html", items_l=items_list)


@app.route('/add_item', methods=["GET", "POST"])
def add_item():
    print("works out of if")
    if request.method == "POST":
        print("works INSIDE of if")
        new_item = {
            "item": request.form.get("n_item"),
            "item_details": request.form.get("n_item_details"),
            "quantity": request.form.get("n_quantity"),
            "expiration_date": request.form.get("n_expiration_date")
        }
        mongo.db.items.insert_one(new_item)
        flash("Food item successfully added")
        return redirect(url_for('get_items'))
    return render_template("add_item.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
