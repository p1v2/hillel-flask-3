from peewee import SqliteDatabase, CharField, Model, FloatField, ForeignKeyField, BooleanField, ManyToManyField
import logging

db = SqliteDatabase('db.sqlite')

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class Category(Model):
    name = CharField()
    is_adult_only = BooleanField(default=False)

    class Meta:
        database = db
        table_name = 'categories'


def get_categories(name_filter=None):
    # Get all categories
    query = Category.select().order_by(Category.name)

    if name_filter is not None:
        query = query.where(Category.name == name_filter)

    return query


def create_category(name, is_adult_only):
    # Create category and return category_name
    return Category.create(name=name, is_adult_only=is_adult_only)


def update_category(category_id, name, is_adult_only):
    # Update category
    category = Category.get_by_id(category_id)

    if name is not None:
        category.name = name

    if is_adult_only is not None:
        category.is_adult_only = is_adult_only

    category.save()

    return category


def delete_category(category_name):
    # Delete category
    Category.delete().where(Category.name == category_name).execute()
    return True


class Tag(Model):
    name = CharField()

    class Meta:
        database = db
        table_name = 'tags'


# Class is a Table in DB (model)
class Product(Model):
    # id INTEGER PRIMARY KEY
    # name TEXT
    # price REAL

    # Fields are columns in DB
    name = CharField()
    price = FloatField()
    category = ForeignKeyField(Category, backref='products')
    tags = ManyToManyField(Tag, backref='products')

    class Meta:
        database = db
        table_name = 'products'


def get_products(name_filter=None):
    # Get all products
    query = Product.select(
        Product, Category
    ).join(Category).order_by(-Product.name)

    if name_filter is not None:
        query = query.where(Product.name == name_filter)

    return query


def create_product(name, price, category_id):
    # Create product and return product id
    return Product.create(name=name, price=price, category_id=category_id)


def update_product(product_id, name, price, category_id):
    # Update product
    product = Product.get_by_id(product_id)

    if name is not None:
        product.name = name

    if price is not None:
        product.price = price

    if category_id is not None:
        product.category_id = category_id

    product.save()

    return product


def delete_product(product_id):
    # Delete product
    Product.delete().where(Product.id == product_id).execute()
    return True


if __name__ == '__main__':
    #Category.create(name='Detergents', is_adult_only=1)
    #delete_category(category_name='Detergents')
    update_category(category_id=10, name='Chips', is_adult_only=0)
    #create_category(name='', is_adult_only=0)

    Category.update()
