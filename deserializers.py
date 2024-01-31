from db import create_product, update_product, create_category, update_category
from exceptions import ValidationError


# Deserialization is from JSON (or other format) to Python object
def deserialize_product(product_json, product_id=None, tags = None, partial=False):
    name = product_json.get('name')
    price = product_json.get('price')
    category_id = product_json.get('category')
    tags = product_json.get('tags')

    if name is None and not partial:
        raise ValidationError('name is required')
    if price is None and not partial:
        raise ValidationError('price is required')
    if category_id is None and not partial:
        raise ValidationError('category is required')

    if price is not None and price <= 0:
        raise ValidationError('price must be positive')

    if product_id is None:
        return create_product(name, price, category_id, tags)
    else:
        return update_product(product_id, name, price, category_id, tags)


def deserialize_category(category_json, category_id=None):
    # category_id = category_json.get('id')
    name = category_json.get('name')
    is_adult_only = category_json.get('is_adult_only')

    if name is None:
        raise ValidationError('name is required')
    
    if is_adult_only is None:
        raise ValidationError('is_adult_only is required')
    
    if category_id is None:
        return create_category(name, is_adult_only)
    else:
        return update_category(category_id, name, is_adult_only)