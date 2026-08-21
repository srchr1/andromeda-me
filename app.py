from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.secret_key = "andromeda_brand_secret_key"

# Tells Flask to trust ngrok's HTTPS and Host headers
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

PARTNERS = [
    {"id": "digitinary", "name": "Digitinary", "category": "Digital Transformation & Solutions"},
    {"id": "ais", "name": "AIS Digicore", "category": "Enterprise Core Technology"},
    {"id": "fimple", "name": "Fimple", "category": "Core Banking & FinTech"},
    {"id": "kayanhr", "name": "KayanHR", "category": "HR Tech & Talent Management"},
    {"id": "ripple", "name": "Ripple", "category": "Enterprise Blockchain & Payments"},
    {"id": "cybercode", "name": "Cybercode", "category": "Cybersecurity & Risk Governance"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        company = request.form.get("company")
        message = request.form.get("message")

        print(f"[NEW LEAD] Name: {name} | Email: {email} | Company: {company} | Message: {message}")
        flash("Thank you for reaching out! The AndromedaME team will contact you shortly.", "success")
        return redirect(url_for("index") + "#contact")

    return render_template("index.html", partners=PARTNERS)

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)