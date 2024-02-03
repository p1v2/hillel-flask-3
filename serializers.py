from db import Product, Category
from typing import Union
from peewee import ModelSelect

# Serialization is from Python object to JSON (or other format)
def serialize_category(category: Union[Category, ModelSelect]):
    if isinstance(category, Category):
        return {
            'id': category.id,
            'name': category.name,
            'is_adult_only': category.is_adult_only,
        }
    else:
        return None

def serialize_tag(tag):
    return tag.name

def serialize_product(product: Union[Product, ModelSelect]):
    if isinstance(product, Product):
        return {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'category': serialize_category(product.category) if product.category else None,
            'tags': [serialize_tag(tag) for tag in product.tags],
        }
    else:
        return None
