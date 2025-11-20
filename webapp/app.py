from flask import Flask, render_template, request, redirect, url_for, session
from password_check import validate_password

app = Flask(__name__)
app.secret_key = "ssd-secret-key"   # for session handling


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pw = request.form.get("password")

        if validate_password(pw):
            session["password"] = pw
            return redirect(url_for("welcome"))
        else:
            return render_template("index.html", error="Invalid password.")

    return render_template("index.html")


@app.route("/welcome")
def welcome():
    if "password" not in session:
        return redirect(url_for("home"))
    return render_template("welcome.html", password=session["password"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
