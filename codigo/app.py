from flask import Flask, request, jsonify, render_template
from models import db, Product, Customer, Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chocolate_factory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# CRUD para produtos
@app.route('/products', methods=['GET', 'POST'])
def manage_products():
    if request.method == 'POST':
        data = request.get_json()
        new_product = Product(name=data['name'], price=data['price'])
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201

    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

# CRUD para clientes
@app.route('/customers', methods=['GET', 'POST'])
def manage_customers():
    if request.method == 'POST':
        data = request.get_json()
        new_customer = Customer(name=data['name'], email=data['email'])
        db.session.add(new_customer)
        db.session.commit()
        return jsonify(new_customer.to_dict()), 201

    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers]), 200

# CRUD para pedidos
@app.route('/orders', methods=['GET', 'POST'])
def manage_orders():
    if request.method == 'POST':
        data = request.get_json()
        new_order = Order(customer_id=data['customer_id'], product_id=data['product_id'])
        db.session.add(new_order)
        db.session.commit()
        return jsonify(new_order.to_dict()), 201

    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders]), 200

if __name__ == '__main__':
    app.run(debug=True)
