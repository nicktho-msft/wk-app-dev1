from datetime import datetime
from flask import Flask, render_template, jsonify
from . import app
import json

@app.route("/")
def idp():
    return jsonify(
        {
            "providers": ["Dev1TestObject1111.com","Dev1TestObject2222.com","Dev1TestObject3333.com","Dev1TestObject4444","Dev1TestObject5555"],
        })

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
