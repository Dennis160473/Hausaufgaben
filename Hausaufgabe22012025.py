from flask import Flask, request

app = Flask(__name__)


@app.route("/home", methods=["GET"])
def home():
    return "Welcome to our users api"


products = [
    {"id": 1, "name": "T-Shirt", "color": "green", "gender": "woman"},
    {"id": 2, "name": "pants", "color": "blue", "gender": "man"},
    {"id": 3, "name": "socks", "color": "white", "gender": "all"},
]


@app.route("/search<gender>", methods=["POST"])
def get_search():
    credentials = request.get.json()
    name = credentials["name"]
    color = credentials["color"]
    gender = credentials["gender"]
    for u in products:
        if u["gender"] == gender:
            return f"This Product is for {gender}"


@app.route("/products/<int:user_id>", methods=["GET"])
def get_products_by_id(user_id):
    final_user = None

    for u in products:
        if u["id"] == user_id:
            final_user = u

        if final_user == None:
            return "This Product could not be found"

        return f"The Product is {final_user}"


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    return f"Searching for: {query}"


if __name__ == "__main__":
    app.run(debug=True, port=6060)
