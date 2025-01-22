from flask import Flask, request

app = Flask(__name__)


@app.route("/home", methods=["GET"])
def home():
    return "Welcome to our users api"


users = [
    {"id": 1, "name": "Alice", "password": "letsGO", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "password": "letsGO1", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "password": "letsGO2", "email": "charlie@example.com"},
]


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    final_user = None

    for u in users:
        if u["id"] == user_id:
            final_user = u

        if final_user == None:
            return "User could not be found"

        return f"The User is {final_user}"


@app.route("/search", methods=["GET"])
def get_user_by_name():
    final_user = None
    name = request.args.get("name")
    for u in users:
        if u["name"] == name:
            final_user = u

        if final_user == None:
            return "User could not be found"

        return f"The User is {final_user}"


@app.route("/users/login", methods=["POST"])
def login():
    credentials = request.get.json()
    name = credentials["name"]
    password = credentials["password"]

    for u in users:
        if u["name"] == name:
            final_user = u
        if u["password"] == password:
            final_user = u
        if final_user == None:
            return f"User could not be found"
    else:
        return f"Hallo {credentials}{name} {password}"


# Route 1
@app.route("/brand/<int:id>", methods=["GET"])
def brand(id):
    type = request.args.get("type")
    condition = request.args.get("condition")
    return f"brand-id: {id}, type: {type}, condition: {condition}"


# Route 2
@app.route("/product/<product_id>", methods=["GET"])
def product(product_id):
    return f"product_id: {product_id}"


# Route 3
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    return f"Searching for: {query}"


if __name__ == "__main__":
    app.run(debug=True, port=6060)
