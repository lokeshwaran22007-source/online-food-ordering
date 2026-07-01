from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Online Food Ordering API is Running"
    }

app.run(host="0.0.0.0", port=5000)
