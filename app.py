from flask import Flask

app = Flask(__name__)

@app.route("/")
def public():
    return "Welcome to the Public Page!"

@app.route("/admin")
def admin():
    return "Welcome to the Admin Page! (Protected - Only for Admins)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
