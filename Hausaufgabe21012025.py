from flask import Flask, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]


# Aufgabe 2 Route 1
@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user1 = request.args.get("users[1]")

    return f"Our User for testing the Flask App is {user1}."


# Aufgabe 2 Route 2
@app.route("/logIn/<id>", methods=["GET"])
def get_logIn(id):
    if users == 2:
        print("The LogIn is approved.")

    else:
        print(f"The LogIn is not correct.")


# Aufgabe 2 Route 3
@app.route("/search/<name>", methods=["GET"])
def get_search(name):
    for i in range(users):
        user3 = {Charlie}

    return f"Found user: Charlie"


@app.route("/brand", methods=["GET"])
def get_mamazon_default_brand_page():
    # Should return a welcome to brand page text
    return "Welcome to brand page"


@app.route("/brand/<brand_id>", methods=["GET"])
def get_brand_by_id(brand_id):
    # Should return  welcome to specific brand page text
    # E.g. Welcome to Hilfigher (dynamisch)
    # Should be able to filter by brand type and should display the filter on the screen

    brand_type = request.args.get("type")
    # E.g. Welcome to Hilfigher and the type is t-shirts
    # Should be able to filter by condition of the article and should display the condition on the screen
    # --> Goals E.g. Welcome to Hilfigher and the type is t-shirts and the condition is used
    condition = request.args.get("condition")
    return (
        f"My Brand id is:{brand_id}, type: {brand_type} and the condition: {condition}"
    )


if __name__ == "__main__":
    app.run(debug=True, port=6060)
