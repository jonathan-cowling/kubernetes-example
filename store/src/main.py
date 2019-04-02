from flask import Flask

app = Flask(__name__, static_url_path="" ,static_folder="data")

@app.route("/")
def get():
    return app.send_static_file("post.md")