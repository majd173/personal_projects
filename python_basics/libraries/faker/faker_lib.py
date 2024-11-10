import json

from faker import Faker

faker = Faker()

contacts = {faker.name(): {
    "phone": faker.phone_number(),
    "address": faker.address(),
    "email": faker.email(),
}
    for _ in range(20)}


def save_file(data):
    try:
        with open('contacts.json', 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Can not save config. {e}")

save_file(contacts)

def load_file():
    try:
        with open('contacts.json'.lower(), 'r') as f:
            data = json.load(f)
            print(data)
    except Exception as e:
        print(f"Can not load config. {e}")

# load_file()