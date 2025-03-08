from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import os

app = Flask(__name__)

# Use a strong secret key (update this for production)
app.secret_key = os.getenv("SECRET_KEY", "change_this_secret_key")

FLAG = "FLAG{4uTh3nTic4tI0n_ByPas5_34h}"

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)  # Prevent crash if JSON is invalid

    if data and data.get("username") == "admin":
        session["user"] = "admin"
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", flag=FLAG)
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Use Render's assigned port or default to 5000
    app.run(host="0.0.0.0", port=port, debug=False)  # Disable debug mode for production
