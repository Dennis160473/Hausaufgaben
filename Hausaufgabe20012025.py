from flask import Flask

app = Flask(__name__)


# Begrüßungsroute
@app.route("/")
def home():
    return "Willkommen bei meiner Flask-App!"


# Performance
@app.route("/about")
def info():
    return (
        "Mein Name ist Dennis Angermann, und ich interessiere mich für Webentwicklung."
    )


# Project specification
@app.route("/project")
def team():
    return "My current project is a Flask API for beginners."


# News
@app.route("/news")
def hilfe():
    return "Today we will learn how to create APIs with Flask!"


# Feedback
@app.route("/feedback")
def kontakt():
    return "We look forward to your feedback at feedback@example.com."


# Feedback
@app.route("/support")
def kontakt():
    return "Visit our support page at support.example.com."


if __name__ == "__main__":
    app.run(port=6060)
