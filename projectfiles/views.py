from projectfiles import app
from flask import jsonify, request
import datetime

category_id = 1
user_id = 1
records_id = 1

CATEGORIES = [{
    "id": 1,
    "name": "Food",
}]

USERS = [{
    "id": 1,
    "name": "Yuriy",
}]

RECORDS = [{
    "id": 1,
    "user_id": 1,
    "category_id": 1,
    "date": datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"),
    "costs": 1,
}]


# GET /categories
# POST /category


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route("/category", methods=['POST'])
def create_categories():
    global category_id
    request.data = request.get_json()

    category_id += 1

    CATEGORIES.append({"id": category_id,
                       "name": request.data['name'], })
    return jsonify(request.data)


# GET /users
# POST /user

@app.route("/users")
def get_users():
    return jsonify({"users": USERS})


@app.route("/user", methods=['POST'])
def create_user():
    global user_id
    request.data = request.get_json()

    user_id += 1

    USERS.append({"id": user_id,
                  "name": request.data['name'], })
    return jsonify(request.data)


# GET /records
# POST /record

@app.route("/records")
def get_records():
    return jsonify({"records": RECORDS})


@app.route("/record", methods=['POST'])
def create_record():
    global records_id
    request.data = request.get_json()

    records_id += 1

    RECORDS.append({"id": records_id,
                    "user_id": request.data['user_id'],
                    "category_id": request.data['category_id'],
                    "date": datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"),
                    "costs": request.data['costs'], })
    return jsonify(request.data)
