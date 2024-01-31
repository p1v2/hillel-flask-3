from flask import Flask, request

from db import Category, Product, delete_category, get_products, create_product, update_product, delete_product, get_category
from exceptions import ValidationError
from serializers import serialize_category, serialize_product
from deserializers import deserialize_category, deserialize_product

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    # Return hello world
    return "Hello, World!"


@app.route('/products', methods=['GET', 'POST'])
def products_api():
    if request.method == "GET":
        name_filter = request.args.get('name')

        products = get_products(name_filter)

        # Convert products to list of dicts
        products_dicts = [
            serialize_product(product)
            for product in products
        ]

        # Return products
        return products_dicts
    if request.method == "POST":
        # Create a product
        product = deserialize_product(request.get_json())

        # Return success
        return serialize_product(product), 201


@app.route('/products/<int:product_id>', methods=['PUT', 'PATCH', 'DELETE', 'GET'])
def product_api(product_id):
    try:
        if request.method == "GET":
            # Get a product
            product = get_products().where(Product.id == product_id).get()
            return serialize_product(product)
    except Product.DoesNotExist:
        return "такого продукту немає", 404
    if request.method == "PUT":
        # Update a product
        product = deserialize_product(request.get_json(), product_id)
        # Return success
        return serialize_product(product)
    if request.method == "PATCH":
        # Update a product
        product = deserialize_product(request.get_json(), product_id, partial=True)
        # Return success
        return serialize_product(product)
    if request.method == "DELETE":
        delete_product(product_id)

        return "", 204



@app.route('/categories', methods=['GET', 'POST'])
def categories_api():
    if request.method == "GET":
        # Get all categories

        name_filter = request.args.get('name')
        categories = get_category(name_filter)

        # Convert categories to list of dicts
        categories_dicts = [
            serialize_category(category)
            for category in categories
        ]

        # Return categories
        return categories_dicts
    if request.method == "POST":
        # Create a category
        category = deserialize_category(request.get_json())

        # Return success
        return serialize_category(category), 201


@app.route('/categories/<int:category_id>', methods=['PUT', 'PATCH', 'DELETE', 'GET'])
def category_api(category_id):
    try:
        if request.method == "GET":
            # Get a category
            category = get_category().where(Category.id == category_id).get()
            return serialize_category(category)
    except:
        return "такої категорії немає", 404
    if request.method == "PUT":
        # Update a category
        category = deserialize_category(request.get_json(), category_id)
        # Return success
        return serialize_category(category)
    if request.method == "PATCH":
        # Update a category
        category = deserialize_category(request.get_json(), category_id, partial=True)
        # Return success
        return serialize_category(category)
    if request.method == "DELETE":
        delete_category(category_id)

        return "", 204







@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return {
        'error': str(e)
    }, 422


if __name__ == '__main__':
    app.run(debug=True, port=5001)
