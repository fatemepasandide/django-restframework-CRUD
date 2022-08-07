# base
import requests

def product_list():
    endpoint="http://localhost:8000/product/"

    get_response = requests.get(endpoint) 
    print(get_response.json())


def product_create():
    endpoint = "http://127.0.0.1:8000/product/"

    data = {
        'name' : 'keyboard',
        'description' : 'barndnew keyboard',
        'price' : 4.5,
        'quantity' :3
    }

    get_response = requests.post(endpoint , json = data)

    print(get_response.json())


def product_update():
    endpoint = "http://127.0.0.1:8000/product/2/update/"

    data = {
        'name' : 'mouse',
        'description' : 'barndnew mouse',
        'price' : 4.5,
        'quantity' :3
    }

    get_response = requests.put(endpoint, json=data)



    print(get_response.json())

def product_delete():
    product_id = input("Enter your product id to delete: \n")

    try:
        product_id=int(product_id)
    except:
        product_id = None
        print(f"{product_id} is not valid")

    if product_id:
        endpoint = f"http://localhost:8000/product/{product_id}/delete/" 

        get_response = requests.delete(endpoint) 
        print(get_response.status_code)

