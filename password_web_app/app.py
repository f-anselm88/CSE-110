from xmlrpc.client import _HostType

from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, strength):
    if strength == "weak":
        chars = string.ascii_letters
        score = "Weak"
    elif strength == "medium":
        chars = string.ascii_letters + string.digits
        score = "Medium"
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
        score = "Strong"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password, score


@app.route("/", methods=["GET", "POST"])
def home():
    passwords = []
    score = ""

    if request.method == "POST":
        length = int(request.form["length"])
        strength = request.form["strength"]

        for _ in range(5):  # generate multiple passwords
            pwd, score = generate_password(length, strength)
            passwords.append(pwd)

    return render_template("index.html", passwords=passwords, score=score)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000)