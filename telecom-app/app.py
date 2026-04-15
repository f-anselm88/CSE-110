import re
def validate_namibia_phone(phone):
  pattern = r"^\+264(81|82|83|84|85|86|87|88|89)\d{7}$"
  return re.fullmatch(pattern, phone)


from flask import Flask, render_template, request, redirect, session
import sqlite3
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- DB ----------------
def get_db():
    return sqlite3.connect("database.db")

def init_db():
    db = get_db()
    db.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        phone TEXT,
        password TEXT,
        balance REAL
    )
    """)
    db.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        amount REAL,
        type TEXT
    )
    """)
    db.commit()

init_db()

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return render_template("index.html")


# -------- REGISTER --------
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        phone = request.form["phone"]
        password = generate_password_hash(request.form["password"])

        phone = request.form["phone"].strip()

        pattern = r"^\+264(81|82|83|84|85|86|87|88|89)\d{7}$"

        if not re.fullmatch(pattern, phone):
            return "Invalid phone number format (+264XXXXXXXXX)"

        db = get_db()
        db.execute(
            "INSERT INTO users (phone, password, balance) VALUES (?, ?, ?)",
            (phone, password, 100)
        )
        db.commit()

        return redirect("/login")

    return render_template("register.html")


# -------- LOGIN --------
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        phone = request.form["phone"]
        password = request.form["password"]

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE phone=?", (phone,)).fetchone()

        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            return redirect("/dashboard")

        return "Invalid login"

    return render_template("login.html")


# -------- DASHBOARD --------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()
    user = db.execute("SELECT * FROM users WHERE id=?", (session["user_id"],)).fetchone()
    transactions = db.execute("SELECT * FROM transactions WHERE user_id=?", (session["user_id"],)).fetchall()

    return render_template("dashboard.html", user=user, transactions=transactions)


# -------- SEND AIRTIME --------
@app.route("/send", methods=["POST"])
def send():
    if "user_id" not in session:
        return redirect("/login")

    phone = request.form["phone"]
    amount = float(request.form["amount"])

    db = get_db()

    sender = db.execute("SELECT * FROM users WHERE id=?", (session["user_id"],)).fetchone()
    receiver = db.execute("SELECT * FROM users WHERE phone=?", (phone,)).fetchone()

    if not receiver:
        return "Receiver not found"

    if sender[3] < amount:
        return "Insufficient balance"

    db.execute("UPDATE users SET balance=? WHERE id=?", (sender[3]-amount, sender[0]))
    db.execute("UPDATE users SET balance=? WHERE id=?", (receiver[3]+amount, receiver[0]))

    db.execute("INSERT INTO transactions (user_id, amount, type) VALUES (?, ?, ?)", (sender[0], amount, "Sent"))
    db.execute("INSERT INTO transactions (user_id, amount, type) VALUES (?, ?, ?)", (receiver[0], amount, "Received"))

    db.commit()
    return redirect("/dashboard")


# -------- DEPOSIT --------
@app.route("/deposit", methods=["POST"])
def deposit():
    if "user_id" not in session:
        return redirect("/login")

    amount = float(request.form["amount"])

    db = get_db()
    user = db.execute("SELECT * FROM users WHERE id=?", (session["user_id"],)).fetchone()

    db.execute("UPDATE users SET balance=? WHERE id=?", (user[3]+amount, user[0]))
    db.execute("INSERT INTO transactions (user_id, amount, type) VALUES (?, ?, ?)", (user[0], amount, "Deposit"))

    db.commit()
    return redirect("/dashboard")


app.run(debug=True)