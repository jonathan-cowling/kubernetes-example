from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__, static_url_path="", static_folder="public", template_folder="template")
app.config.from_json("config/base.json")
stage = "DEV" if os.environ.get("STAGE") == None else os.environ("STAGE")
app.config.from_json("config/%s.json" %(stage.lower()))

@app.route("/")
def root():
    return render_template("/index.html")

@app.route("/posts/")
def getPost():
    post_id = request.args.get("id")
    post = requests.get(app.config["STORE_URL"], params={"post_id": post_id})
    return requests.post(app.config["CONVERTER_URL"], data=post.text).text