import requests

def test_product_create():
    # Create a product
    response = requests.post('http://localhost:5001/products', json={
        'name': 'Jaffa Orange',
        'price': 10,
        'category': 2,
        'tags': '2 for 1',
    })

    print(response.status_code)
    print(response.headers.get('Content-Type'))
    #print(response.text)
    print(response.json())


def test_product_update():
    # Update a product
    response = requests.put('http://localhost:5001/products/12', json={
        'name': 'Torchin',
        'price': 30,
    })

    print(response.status_code)
    print(response.json())


def test_product_delete():
    # Delete a product
    response = requests.delete('http://localhost:5001/products/2')

    print(response.status_code)
    print(response.content)

# CATEGORIES



def test_category_create():
    # Create a category
    response = requests.post('http://localhost:5001/categories', json={
        'name': 'Juice',
        'is_adult_only': 0
    })

    if response.status_code == 500:
        print('Server error')
    else:
        print(response.status_code)
        print(response.json())


def test_category_update():
    # Update a category
    response = requests.put(f'http://localhost:5001/categories/2', json={
        'name': 'Butter Cream',
        'is_adult_only': 0,
    })

    print(response.status_code)
    print(response.json())

def test_category_delete(category_id):
    # Delete a category
    response = requests.delete(f'http://localhost:5001/categories/{category_id}')

    print(response.status_code)
    print('Category deleted')

def check_category_exist(category_id):

    response = requests.patch(f'http://localhost:5001/categories/{category_id}', json=None)

    if response.status_code == 404:
        print(f"Category with ID {category_id} does not exist.")
        return print(response.status_code)
    elif response.status_code == 200:
        print(f"Category with ID {category_id} exists.")
        return print(response.status_code), print(response.json())
    else:
        print(f"Unexpected status code: {response.status_code}")
        return print(response.status_code), print(response.text)



if __name__ == "__main__":
    #test_category_update()
    #test_category_create()
    check_category_exist(9)
    #test_product_create()
    #test_category_exist()
    #test_category_delete(10)
