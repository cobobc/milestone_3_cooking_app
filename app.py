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
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # to check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Oops! This username already exists")
            return redirect(url_for("register"))

        # to check if the email already exists in the database
        existing_email = mongo.db.emails.find_one(
            {"email": request.form.get("email")}) 

        if existing_email:
            flash("Oops! This email already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        mongo.db.emails.insert_one(register)

        # to put the new user into a 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You have successfully registered! Happy cooking!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # to check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # to ensure the hashed password matches the user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))

            else:
                # an invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # the username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # to get the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    # to remove the user from the session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipe_list.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipe_list.html", recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_type": request.form.get("recipe_type"),
            "recipe_name": request.form.get("recipe_name"),
            "cooking_time": request.form.get("cooking_time"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your recipe has been added")
        return redirect(url_for("get_recipes"))

    recipe_type = mongo.db.recipe_type.find().sort("recipe_type", 1)
    return render_template("add_recipe.html", recipe_type=recipe_type)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        update_recipe = {
            "recipe_type": request.form.get("recipe_type"),
            "recipe_name": request.form.get("recipe_name"),
            "cooking_time": request.form.get("cooking_time"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, update_recipe)
        flash("Your recipe has been updated")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipe_type = mongo.db.recipe_type.find().sort("recipe_type", 1)
    return render_template("edit_recipe.html", recipe=recipe, recipe_type=recipe_type)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Your recipe was successfully deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_types")
def get_types():
    recipe_type = list(mongo.db.recipe_type.find().sort("recipe_type", 1))
    return render_template("recipe_types.html", recipe_type=recipe_type)


@app.route("/add_type", methods=["GET", "POST"])
def add_type():
    if request.method == "POST":
        recipe_type = {
            "recipe_type": request.form.get("recipe_type")
        }
        mongo.db.recipe_type.insert_one(recipe_type)
        flash("New Recipe Type Added")
        return redirect(url_for("get_types"))

    return render_template("add_recipe_type.html")


@app.route("/edit_type/<type_id>", methods=["GET", "POST"])
def edit_type(type_id):
    if request.method == "POST":
        submit = {
            "recipe_type": request.form.get("recipe_type")
        }
        mongo.db.recipe_type.update({"_id": ObjectId(type_id)}, submit)
        flash("Recipe Type Successfully Updated")
        return redirect(url_for("get_types"))

    type = mongo.db.recipe_type.find_one({"_id": ObjectId(type_id)})
    return render_template("edit_recipe_type.html", type=type)


@app.route("/delete_type/<type_id>")
def delete_type(type_id):
    mongo.db.recipe_type.remove({"_id": ObjectId(type_id)})
    flash("Recipe Type Successfully Deleted")
    return redirect(url_for("get_types"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
        