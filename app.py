from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/explore")
def explore():
    return render_template("explore.html")


@app.route("/activity/<int:activity_id>")
def activity(activity_id):
       return render_template("activity.html", activity_id=activity_id)


@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(debug=True)