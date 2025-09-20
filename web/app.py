# Add to this file for the sample app lab
import os
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

mongo_uri = os.environ.get("MONGO_URI")
db_name = os.environ.get("DB_NAME")

# data = []
# client = MongoClient("mongodb://mongo:27017/")
client = MongoClient(mongo_uri)
# mydb = client["mydatabase"]
mydb = client[db_name]
mycol = mydb["routers"]

mycol2 = mydb["interface_status"]


@app.route("/")
def main():
    data = mycol.find()
    return render_template("index.html", data=data)


@app.route("/router/<ip>")
def show_router(ip):
    data = mycol2.find({"router_ip": ip}).sort("timestamp", -1).limit(3)
    print(data)
    return render_template("router_detail.html", data=data, ip=ip)


@app.route("/add", methods=["POST"])
def add_router():
    ipaddress = request.form.get("ipaddress")
    username = request.form.get("username")
    password = request.form.get("password")

    if ipaddress and username and password:
        # data.append({"yourname": yourname, "message": message})
        mycol.insert_one({"ip": ipaddress, "username": username, 
        "password": password})
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete_router():
    try:
        print(request.form.get("idx"))

        idx = ObjectId(request.form.get("idx"))
        mycol.delete_one({"_id": idx})
        # if 0 <= idx < len(data):
        #     data.pop(idx)
    except Exception:
        pass
    return redirect(url_for("main"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
