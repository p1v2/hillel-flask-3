from peewee import SqliteDatabase, CharField, Model, FloatField, ForeignKeyField, \
BooleanField, ManyToManyField, PrimaryKeyField, AutoField
import logging

db = SqliteDatabase('db.sqlite')

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

class BaseModel(Model):
    class Meta:
        database = db

class Category(BaseModel):

    name = CharField()
    is_adult_only = BooleanField(default=False)

    class Meta:
        database = db
        table_name = 'categories'

def get_category_by_name(name_filter=None):
    # Get products by name
    query = Category.select(Category).order_by(-Category.name)

    if name_filter is not None:
        query = query.where(Category.name == name_filter)

    return query

def get_category_by_id(id_filter=None):
    # Get products by id
    query = Category.select(Category).order_by(-Category.id)

    if id_filter is not None:
        query = query.where(Category.id == id_filter)

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


def delete_category(category_id):
    # Delete category
    Category.delete().where(Category.id == category_id).execute()
    return True


class Tag(BaseModel):
    name = CharField()

    class Meta:
        database = db
        table_name = 'tags'


# Class is a Table in DB (model)
class Product(BaseModel):

    # Fields are columns in DB
    name = CharField()
    price = FloatField()
    category = ForeignKeyField(Category, backref='products')
    tags = ManyToManyField(Tag, backref='products')

    class Meta:
        database = db
        table_name = 'products'


def get_product_by_name(name_filter=None):
    # Get products by name
    query = Product.select(
        Product, Category
    ).join(Category).order_by(-Product.name)

    if name_filter is not None:
        query = query.where(Product.name == name_filter)

    return query

def get_product_by_id(id_filter=None):
    # Get products by id
    query = Product.select(
        Product, Category
    ).join(Category).order_by(-Product.id)

    if id_filter is not None:
        query = query.where(Product.id == id_filter)
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
    #update_category(category_id=10, name='Chips', is_adult_only=0)
    #create_category(name='', is_adult_only=0)

    get_products_by_id(1)
