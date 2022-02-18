from flask import Flask, render_template, request
import web_map
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/reroute", methods=["POST"])
def reroute():
    if request.method == "POST":
        dct = request.form
        nickname = dct["name"]
        web_map.main(nickname)
        return render_template('friends_map.html')
