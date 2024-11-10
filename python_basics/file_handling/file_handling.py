# file handling
import json
import os


def open_write_file(text):
    try:
        with open('file.txt', 'w') as file:
            file.write(text)
    except FileNotFoundError:
        print('file not found')


def open_read_file():
    try:
        with open('file.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('file not found')


open_write_file('hello world!')
open_read_file()

data = {
    'name': 'john',
    'email': 'john@x.com',
    'phone': '123-456-7890'
}

data_2 = {
    'name': 'jimmy',
    'email': 'jimy@x.com',
    'phone': '123-000-7890'
}


def open_dump_file_json(d):
    try:
        # Initialize an empty list to hold data
        data = []

        # Check if file.json already exists and has content
        if os.path.exists('file.json'):
            with open('file.json', 'r') as f:
                try:
                    data = json.load(f)  # Load existing data
                except json.JSONDecodeError:
                    print('Error in reading file. Starting with an empty list.')

        # Ensure the file content is a list, in case it was empty or a different structure
        if not isinstance(data, list):
            data = []

        # Append the new dictionary to the list
        data.append(d)

        # Write the updated list back to file.json
        with open('file.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")

    except Exception as e:
        print(f"Cannot save config. {e}")


# Example usage
open_dump_file_json(data)


def open_load_file_json():
    try:
        with open('file.json', 'r') as f:
            data = json.load(f)
            print(data)
    except Exception as e:
        print(f"Can not load config. {e}")
    except json.JSONDecodeError:
        print('error in reading file')

open_load_file_json()
