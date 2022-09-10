import json

from models import *
from config import *

def insert_data_model(model, input_data):
    '''
        Универсальный метод, который возвращает данные определённой модели класса
    :param model:
    :param input_data:
    :return:
    '''
    for row in input_data:
        db.session.add(
            model(
               **row
            )
        )
        db.session.commit()


def get_all(model):
    '''
    Универсальный метод, который возвращает все объекты модели класса
    :param model:
    :return:
    '''
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict())
    return result

def get_all_by_id(model, pid):
    '''
    Универсальный метод, который возвращает по id объект модели класса
    :param model:
    :param pid:
    :return:
    '''
    try:
        return db.session.query(model).get(pid).to_dict()
    except Exception:
        return {}

def get_all_union(model, model2, pid):
    '''
        Универсальный метод, который по id возвращает объект модели класса с обновленными перекрестными полями другого объекта модели класса
    :param model:
    :param model2:
    :param pid:
    :return:
    '''
    try:
        data = db.session.query(model, model2).join(model2).filter(model.id == pid).all()[0]
        result = data[0].to_dict()
        result.update(data[1].to_dict())
        return result
    except Exception:
        return {}

'''
def get_all_union(model, model2, pid):
    data = db.session.query(model, model2).join(model2).filter(model.id == pid).all()
    if len(data) == 0:
        return {}
    else:
        data = data[0]
        result = data[0].to_dict()
        result.update(data[1].to_dict())
        return result
   
    '''

def update_model(model, pid, values):
    '''
        Универсальный метод, который по id обновляет данные у объекта модели класса
    :param model:
    :param pid:
    :param values:
    :return:
    '''
    try:
        db.session.query(model).filter(model.id == pid).updates(values)
        db.session.commit()
    except Exception as e:
        print(e)
        return {}


def delete_model(model, pid):
    '''
          Универсальный метод, который по id удаляет объект модели класса
    :param model:
    :param pid:
    :return:
    '''
    try:
        db.session.query(model).filter(model.id == pid).delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return {}

def init_db():
    '''
    Универсальный метод, который удаляет таблицы, а затем создает их заново с данными из json файлов.
    Также используется универсальный метод по заполнению таблиц данными с учетом модели класса
    :return:
    '''
    db.drop_all()
    db.create_all()

    with open("data/users.json", encoding='utf-8') as file:
        data = json.load(file)
        insert_data_model(User, data)

    with open("data/orders.json", encoding='utf-8') as file:
        data = json.load(file)
        insert_data_model(Order, data)

    with open("data/offers.json", encoding='utf-8') as file:
        data = json.load(file)
        insert_data_model(Offer, data)


