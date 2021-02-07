import os
from flask import (Flask, flash, render_template, redirect, request, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    items_list = list(mongo.db.items.find())
    return render_template("items.html", items_l=items_list)


@app.route('/add_item', methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
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


@app.route("/edit_item/<edit_item_id>", methods=["GET", "POST"])
def edit_item(edit_item_id):
    if request.method == "POST":
        edited_item = {
            "item": request.form.get("e_item"),
            "item_details": request.form.get("e_item_details"),
            "quantity": request.form.get("e_quantity"),
            "expiration_date": request.form.get("e_expiration_date")
        }
        mongo.db.items.update({"_id": ObjectId(edit_item_id)}, edited_item)
        flash("Food item successfuly updated")

    edit_i = mongo.db.items.find_one({"_id": ObjectId(edit_item_id)})
    return render_template('edit_item.html', itm=edit_i)


@app.route('/delete_item/<delete_item_id>', methods=["GET", "POST"])
def delete_item(delete_item_id):
    print("delete function")
    mongo.db.items.remove({"_id": ObjectId(delete_item_id)})
    flash("Item successfully deleted")
    return redirect(url_for("get_items"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
