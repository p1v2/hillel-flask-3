from db import Product, Category


# Serialization is from Python object to JSON (or other format)
def serialize_category(category: Category):
    return {
        'id': category.id,
        'name': category.name,
        'is_adult_only': category.is_adult_only,
    }


def serialize_tag(tag):
    return tag.name


def serialize_product(product: Product):
    return {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'category': serialize_category(product.category),
        'tags': [serialize_tag(tag) for tag in product.tags],
    }
