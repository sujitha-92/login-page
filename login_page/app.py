from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# Replace this with a strong secret key stored in an environment variable before deployment.
app.config["SECRET_KEY"] = "change-this-secret-key-for-local-development"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        remember = request.form.get("remember") == "on"

        if not email or not password:
            flash("Please enter both your email and password.", "error")
            return render_template("login.html")

        # Demo only: connect this to a real user database and password-hash verification.
        # Do not accept credentials or create sessions based only on these form checks.
        flash("The form was submitted. Connect authentication to enable real login.", "info")
        return render_template("login.html")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not name or not email or not password or not confirm_password:
            flash("Please complete all fields.", "error")
        elif password != confirm_password:
            flash("Passwords do not match. Please try again.", "error")
        elif len(password) < 8:
            flash("Your password must be at least 8 characters long.", "error")
        else:
            # Demo only: no account is saved. Add database storage and password hashing
            # before using this page for real customer registration.
            flash("The form looks good, but account creation is not connected to a database yet.", "info")

    return render_template("signup.html")


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        if not email:
            flash("Please enter your email address.", "error")
        else:
            # Demo only: no reset email is sent. Add a secure, time-limited reset-token
            # flow and email delivery before using this for real customer accounts.
            flash("This demo does not send reset emails yet. Password recovery must be connected before use.", "info")
    return render_template("forgot_password.html")


if __name__ == "__main__":
    app.run(debug=True)
