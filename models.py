from config import db

class User(db.Model):
    '''
        класс User с параметрами из таблицы user
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(100))
    last_name = db.Column(db.Text(100))
    age = db.Column(db.Integer)
    email = db.Column(db.Text(100))
    role = db.Column(db.Text(100))
    phone = db.Column(db.Text(100))

    def to_dict(self):
        '''
            метод возвращает данные из таблицы user в виде словаря
            :return:
        '''
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Order(db.Model):
    '''
       класс Order с параметрами из таблицы order
    '''
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(100))
    description = db.Column(db.Text(100))
    start_date = db.Column(db.Integer)
    end_date = db.Column(db.Integer)
    address = db.Column(db.Text(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))

    def to_dict(self):
        '''
               метод возвращает данные из таблицы order в виде словаря
            :return:
        '''
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }

class Offer(db.Model):
    '''
        класс Offer с параметрами из таблицы offer
    '''
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(f'{Order.__tablename__}.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))

    def to_dict(self):
        '''
               метод возвращает данные из таблицы offer в виде словаряя
            :return:
        '''
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }
