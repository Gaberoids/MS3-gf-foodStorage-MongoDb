import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
    if session.get('user_session') is not None:
        user_record_id = mongo.db.users.find_one(
            {"username": session["user_session"].lower()})["_id"]
        return render_template(
            "items.html",
            items_l=items_list,
            profile_username=session["user_session"],
            profile_id=user_record_id)

    return render_template("items.html", items_l=items_list)

@app.route("/sort_by_date/<profile_username>/<sort>", methods=['GET'])
def sort_by_date(profile_username, sort):
    sorting = 1 if sort == 'asc' else -1
    items_list = list(list(mongo.db.items.aggregate([{'$sort':{'expiration_date': sorting}}])))
    sort = sort
    profile_username = profile_username
    return render_template("items.html", items_l=items_list, profile_username=profile_username, sort=sort)

# @app.route("/sort_by_date/<items_l>/<profile_username>", methods=['GET'])
# def sort_by_date(items_l, profile_username):
#     if session.get('user_session') is not None:
#         p_username = profile_username

#         if request.args.get:
#             if 'sort' in request.args.get('sort'):
#                 sortkey = request.args.get('sort')
#                 print(sortkey)
#                 sort = sortkey

#                 if sortkey == 'asc':
#                     sortkey == 'asc'
#                     sorted_list = list(mongo.db.items.aggregate(
#                         [{'$sort':{'expiration_date': 1}}]))

#                 if sortkey == 'desc':
#                     sortkey == 'desc'
#                     sorted_list = list(mongo.db.items.aggregate(
#                         [{'$sort':{'expiration_date': -1}}]))
            
#         return render_template(
#             "items.html",
#             profile_username=p_username,
#             items_l=sorted_list,
#             sort=sortkey)

#     return redirect(url_for("login"))
        
        # if sort is "asc":
        #     sorted_list = list(mongo.db.items.aggregate(
        #         [{'$sort':{'expiration_date': -1}}]))
        # return render_template(
        #         "items.html",
        #         profile_username=p_username,
        #         items_l=sorted_list,
        #         sort=sort)

        # if sort is "desc"
        #     sorted_list = list(mongo.db.items.aggregate(
        #         [{'$sort':{'expiration_date': -1}}]))
        #     return render_template(
        #         "items.html",
        #         profile_username=p_username,
        #         items_l=sorted_list,
        #         sort=sort)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    items_list = list(mongo.db.items.find({"$text": {"$search": query}}))
    if session.get('user_session') is not None:
        user_record_id = mongo.db.users.find_one(
            {"username": session["user_session"].lower()})["_id"]
        return render_template(
            "items.html",
            items_l=items_list,
            profile_username=session["user_session"],
            profile_id=user_record_id)
    return render_template("items.html", items_l=items_list)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if user name exist
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("registration_username").lower()})
        if existing_user:
            flash("This username already exist.")
            return redirect(url_for("register"))

        new_user = {
            "username": request.form.get("registration_username").lower(),
            "password": generate_password_hash(
                request.form.get("registration_password"))
        }
        mongo.db.users.insert_one(new_user)
        session["user_session"] = request.form.get(
            "registration_username").lower()
        flash("You've been regitered successfully!")
        return redirect(url_for(
            "get_items", profile_username=session["user_session"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_exist = mongo.db.users.find_one({
            "username": request.form.get("login_username")})
        # check if the user name doesnt exist
        if user_exist:
            if check_password_hash(user_exist[
                    "password"], request.form.get("login_password")):
                session["user_session"] = request.form.get(
                    "login_username").lower()
                flash("Welcome, {}!".format(
                    request.form.get("login_username")))
                return redirect(url_for(
                    "get_items", profile_username=session["user_session"]))

        else:
            # invalid password match
            flash("Incorrect username and/or password.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    if session.get('user_session') is not None:
        session.pop("user_session")

    flash("You were successfully logged out.")
    return redirect(url_for("get_items"))


@app.route("/delete_user/<delete_profile_id>")
def delete_user(delete_profile_id):
    session.pop("user_session")
    mongo.db.users.remove({"_id": ObjectId(delete_profile_id)})
    flash("Account successfully deleted.")
    return redirect(url_for("get_items"))


@app.route("/add_item/<profile_username>", methods=["GET", "POST"])
def add_item(profile_username):
    if request.method == "POST":
        new_item = {
            "item": request.form.get("n_item"),
            "item_details": request.form.get("item_details"),
            "quantity": request.form.get("n_quantity"),
            "expiration_date": request.form.get("n_expiration_date")
        }
        mongo.db.items.insert_one(new_item)
        flash("Food item successfully added.")
        return redirect(url_for('get_items'))
    
    if session.get('user_session') is not None:
        p_username = profile_username
        return render_template(
            "add_item.html",
            profile_username=p_username)

    return render_template("add_item.html")


@app.route("/edit_item/<edit_item_id>/<profile_username>", methods=["GET", "POST"])
def edit_item(edit_item_id, profile_username):
    if request.method == "POST":
        edited_item = {
            "item": request.form.get("e_item"),
            "item_details": request.form.get("item_details"),
            "quantity": request.form.get("e_quantity"),
            "expiration_date": request.form.get("e_expiration_date")
        }
        mongo.db.items.update({"_id": ObjectId(edit_item_id)}, edited_item)
        flash("Food item successfuly updated.")
        return redirect(url_for('get_items'))
    
    edit_i = mongo.db.items.find_one({"_id": ObjectId(edit_item_id)})
    p_username = profile_username
    if session.get('user_session') is not None:
        return render_template(
            "edit_item.html",
            profile_username=p_username,
            itm=edit_i)

    return render_template('edit_item.html', itm=edit_i)


@app.route('/delete_item/<delete_item_id>', methods=["GET", "POST"])
def delete_item(delete_item_id):
    mongo.db.items.remove({"_id": ObjectId(delete_item_id)})
    flash("Item successfully deleted.")
    return redirect(url_for("get_items"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
