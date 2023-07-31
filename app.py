from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/orders"
db.init_app(app)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    description = db.Column(db.String, unique=True)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,  nullable=False)
    order_count = db.Column(db.Integer)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)



@app.route('/')
def homepage():
    orders_list = db.session.execute(db.select(Orders)).scalars()
    clients = db.session.execute(db.select(Client)).scalars()
    cars = db.session.execute(db.select(Car)).scalars()
    return render_template('index.html', orders_list=orders_list, clients=clients, cars=cars)


@app.route('/orders/')
def orders_index():
    orders_list = db.session.execute(db.select(Orders)).scalars()
    return render_template('orders_homepage.html', orders_list=orders_list)

@app.route('/order/<int:id>')
def orders_detail(id):
    order = db.get_or_404(Orders, id)
    return render_template('orders_detail.html', order=order)

@app.route('/name/')
def name_list():
    name_list = db.session.execute(db.select(Client)).scalars()
    return render_template('name.html', name_list=name_list)

@app.route('/name/<int:id>')
def name_detail(id):
    name = db.get_or_404(Client, id)
    return render_template('names_detail.html', name=name)

@app.route('/cars/')
def cars_page():
    cars_list = db.session.execute(db.select(Car)).scalars()
    return render_template('cars_page.html', cars_list=cars_list)

@app.route('/car/<int:id>')
def cars_detail(id):
    car = db.get_or_404(Car, id)
    return render_template('cars_detail.html', car=car)



@app.route('/contacts')
def contact():
    contact_list1 = db.session.execute(db.select(Orders)).scalars()
    return render_template('contacts.html', contacts=contact_list1)

@app.route('/address')
def address():
    address_list1 = db.session.execute(db.select(Orders)).scalars()
    return render_template('address.html', address=address_list1)

@app.route('/description')
def description():
    description_list1 = db.session.execute(db.select(Orders)).scalars()
    return render_template('description.html', description=description_list1)


with app.app_context():
    db.create_all()
