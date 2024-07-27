
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portfolio-details/")
def portfolio():
    return render_template("portfolio-details.html")

@app.route("/service/")
def service():
    return render_template("service-details.html")

@app.route("/admin")
def admin():
    return redirect(url_for("home", name="devi"))

if __name__ == "__main__":
    print("Start running...")
    app.run(host='0.0.0.0', debug=True)