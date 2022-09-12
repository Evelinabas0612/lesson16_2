import json
from flask import request
from config import app
from models import Order, User, Offer
from utils import init_db, get_all, get_all_by_id, update_model, insert_data_model, delete_model


@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    '''
    Метод, который возвращает представление всех Users
    :return:
    '''
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_model(User, request.json)
        elif isinstance(request.json, dict):
            insert_data_model(User, request.json)
        else:
            print("непонятный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():
    '''
    Метод, который возвращает представление всех Orders
    :return:
    '''
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Order), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_model(Order, request.json)
        elif isinstance(request.json, dict):
            insert_data_model(Order, request.json)
        else:
            print("непонятный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/", methods=['GET', 'POST'])
def get_offers():
    '''
    Метод, который возвращает представление всех Offers
    :return:
    '''
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_model(Offer, request.json)
        elif isinstance(request.json, dict):
            insert_data_model(Offer, request.json)
        else:
            print("непонятный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/users/<int:pid>", methods=['GET', 'PUT','DELETE'])
def get_user_by_id(pid):
    '''
    Метод, который возвращает представление User по заданному id
    :param pid:
    :return:
    '''
    if request.method == "GET":
        data = get_all_by_id(User, pid)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        data = request.json
        data_new = {

            "first_name": data.get("first_name"),
            "last_name": data.get("last_name"),
            "age": data.get("age"),
            "email": data.get("email"),
            "role": data.get("role"),
            "phone": data.get("phone")
        }
        update_model(User, pid, data_new)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

    elif request.method == "DELETE":
        delete_model(User, pid)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/<int:pid>", methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(pid):
    '''
    Метод, который возвращает представление Offer по заданному id
    :param pid:
    :return:
    '''
    if request.method == "GET":
        data = get_all_by_id(Offer, pid)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        data = request.json
        data_new = {
            "id": data.get("id"),
            "order_id": data.get("order_id"),
            "executor_id": data.get("executor_id")
        }
        update_model(Offer, pid, data_new)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete_model(Offer, pid)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

@app.route("/orders/<int:pid>", methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(pid):
    '''
    Метод, который возвращает представление Order по заданному id
    :param pid:
    :return:
    '''
    if request.method == "GET":
        data = get_all_by_id(Order, pid)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        data = request.json
        data_new = {

            "name": data.get("name"),
            "description": data.get("description"),
            "start_date": data.get("start_date"),
            "end_date": data.get("end_date"),
            "address": data.get("address"),
            "price": data.get("price"),
            "customer_id": data.get("customer_id"),
            "executor_id": data.get("executor_id")
        }
        update_model(Order, pid, data_new)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete_model(Order, pid)
        return app.response_class(
            response=json.dumps(["OK"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=8080, debug=True)
