from flask import Flask, request, url_for

from db import get_product_by_id, get_product_by_name, create_product, update_product, \
    delete_product, delete_category, get_category_by_id, get_category_by_name,\
    create_category, update_category
from exceptions import ValidationError
from serializers import serialize_product, serialize_category
from deserializers import deserialize_product, deserialize_category

app = Flask(__name__)

@app.route('/')
def main_page_api():
    # Creating links to /categories and /products using url_for
    categories_link = url_for('categories_api')
    products_link = url_for('products_api')

    # Displaying links on the main page
    return f'<a href="{categories_link}">Categories</a><br><br><a href="{products_link}">Products</a>'

@app.route('/products', methods=['GET', 'POST'])
def products_api():
    if request.method == "GET":
        name_filter = request.args.get('name')
        id_filter = request.args.get('id')
        filtered_products = get_product_by_id()

        if id_filter is not None:
            filtered_products = get_product_by_id(id_filter)
        if name_filter is not None:
            filtered_products = get_product_by_name(name_filter)
        if not filtered_products:
            return "Product not found", 404
        else:
            products_dicts = [serialize_product(product) for product in filtered_products]
        return products_dicts

    if request.method == "POST":
        # Create a product
        product = deserialize_product(request.get_json())


        # Return success
        return serialize_product(product), 201

@app.route('/products/<int:product_id>', methods=['GET'])
def products_api_by_id(product_id):
    products_link = url_for('products_api')
    if request.method == "GET":
        product_by_id = get_product_by_id(product_id)
        searched_product = [serialize_product(product) for product in product_by_id]
        if searched_product:
            return searched_product, 200
        else:
            return f'<a>There is no such product yet</a><br><br><br><a href="{products_link}">BACK</a>', 404

@app.route('/products/<int:product_id>', methods=['PUT', 'PATCH', 'DELETE'])
def product_api(product_id):
    products_link = url_for('products_api')
    if request.method == "PUT":
        product_by_id = get_product_by_id(product_id)
        searched_product = [serialize_product(product) for product in product_by_id]
        if searched_product:
            # Update a category
            product = deserialize_product(request.get_json(), product_id)
            # Return success
            return serialize_product(product), 200
        else:
            return f'<a>There is no such product yet</a><br><br><br><a href="{products_link}">BACK</a>', 404
    if request.method == "PATCH":
        # Update a product
        product = deserialize_product(request.get_json(), product_id, partial=True)
        # Return success
        return serialize_product(product)
    if request.method == "DELETE":
        delete_product(product_id)
        return "Product has been Deleted", 204


@app.route('/categories', methods=['GET', 'POST'])
def categories_api():
    if request.method == "GET":
        categories_link = url_for('categories_api')
        name_filter = request.args.get('name')
        id_filter = request.args.get('id')
        filtered_dicts = get_category_by_id()

        # Convert categories to list of dicts
        if name_filter:
            filtered_dicts = get_category_by_name(name_filter)
        if id_filter:
            filtered_dicts = get_category_by_id(id_filter)
        if not filtered_dicts:
            return f'<a>There is no such category yet</a><br><br><br><a href="{categories_link}">BACK</a>', 404
        else:
            categories_dicts = [serialize_category(category) for category in filtered_dicts]
        # Return categories
        return categories_dicts

    if request.method == "POST":
        # Create a category
        category = deserialize_category(request.get_json())

        # Return success
        return serialize_category(category), 201

@app.route('/categories/<int:category_id>', methods=['GET'])
def categories_api_by_id(category_id):
    categories_link = url_for('categories_api')
    if request.method == "GET":
        category_by_id = get_category_by_id(category_id)
        searched_category = [serialize_category(category) for category in category_by_id]
        if searched_category:
            return searched_category, 200
        else:
            return f'<a>There is no such category yet</a><br><br><br><a href="{categories_link}">BACK</a>', 404


@app.route('/categories/<int:category_id>', methods=['PUT', 'PATCH', 'DELETE'])
def category_api(category_id):
    categories_link = url_for('categories_api')
    if request.method == "PUT":
        category_by_id = get_category_by_id(category_id)
        searched_category = [serialize_category(category) for category in category_by_id]
        if searched_category:
        # Update a category
            category = deserialize_category(request.get_json(), category_id)
        # Return success
            return serialize_category(category), 200
        else:
            return f'<a>There is no such category yet</a><br><br><br><a href="{categories_link}">BACK</a>', 404
    if request.method == "PATCH":
        # Update a category
        category = deserialize_category(request.get_json(), category_id, partial=True)
        # Return success
        return serialize_category(category)
    if request.method == "DELETE":
        delete_category(category_id)
        return "Category has been Deleted", 204


@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return {
        'error': str(e)
    }, 422


if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5001)
