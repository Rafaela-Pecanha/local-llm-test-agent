import requests
import json

def create_pet():
    url = "https://petstore.swagger.io/v2/pet"
    pet_data = {
        "id": 123,
        "name": "Rex",
        "status": "available"
    }

    response = requests.post(url, json=pet_data)

    if response.status_code == 200:
        print("Pet created successfully!")
    else:
        print(f"Error creating pet: {response.text}")

create_pet()