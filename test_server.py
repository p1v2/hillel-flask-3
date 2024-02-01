import requests
from deserializers import deserialize_product, deserialize_category
def test_product_create():
    # Create a product
    response = requests.post('http://localhost:5001/products', json={
        'name': 'Sandora',
        'price': 0,
    })

    print(response.status_code)
    print(response.json())


def test_product_update():
    # Update a product
    response = requests.put('http://localhost:5001/products/4', json={
        'name': 'Моршинська',
        'price': 10,
    })

    print(response.status_code)
    print(response.json())


def test_product_delete():
    # Delete a product
    response = requests.delete('http://localhost:5001/products/2')

    print(response.status_code)
    print(response.content)


def test_product_invalid_price():
    # Create a product
    response = requests.post('http://localhost:5001/products', json={
        'name': 'Ліщина',
        'price': -10,
    })

    print(response.status_code)
    print(response.json())


def test_product_update_invalid_price():
    # Update a product
    response = requests.put('http://localhost:5001/products/4', json={
        'name': 'Моршинська',
        'price': -10,
    })

    print(response.status_code)
    print(response.json())


def test_product_update():
    # Update a product
    response = requests.patch('http://localhost:5001/products/4', json={
        'name': 'Borjomi',
        'price': 100,
    })

    print(response.status_code)
    print(response.json())


def test_create_beer():
    # Create a product
    response = requests.post('http://localhost:5001/products', json={
        'name': 'Львівське',
        'price': 50,
        'category': 5,
    })

    print(response.status_code)
    print(response.json())

def test_category_update_name_is_not_empty():
    # Update a category
    response = requests.put('http://localhost:5001/categories/10', json={
        'name': 'Butter',
        'is_adult_only': 0,
    })

    print(response.status_code)
    print(response.json())


def test_category_create_name_is_not_empty():
    # Create a category
    response = requests.post('http://localhost:5001/categories', json={
        'name': 'Butter',
        'is_adult_only': 0
    })

    if response.status_code == 500:
        print('Server')
    else:
        print(response.status_code)
        print(response.json())




if __name__ == "__main__":
    #test_category_update_name_is_not_empty()
    test_category_create_name_is_not_empty()
    #test_create_beer()