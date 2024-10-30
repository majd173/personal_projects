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