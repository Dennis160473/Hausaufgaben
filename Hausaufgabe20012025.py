from flask import Flask, request

app = Flask(__name__)


# Begrüßungsroute
@app.route("/greet/<name>")
def Get_Query_Params():
    firstname = request.args["firstname"]
    name = request.args["name"]

    return f"I am {firstname} {name}. Hello Users, welcome to my Flask API!"


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
def help():
    return "Today we will learn how to create APIs with Flask!"


# Feedback
@app.route("/feedback")
def contact():
    return "We look forward to your feedback at feedback@example.com."


# Feedback
@app.route("/support")
def support():
    return "Visit our support page at support.example.com."


if __name__ == "__main__":
    app.run(port=6060)
