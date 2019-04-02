from flask import Flask

app = Flask(__name__, static_url_path="" ,static_folder="data")

@app.route("/", methods=["POST"])
def convert():
    return "<html><head></head><body><h1>test</h1></body></html>"