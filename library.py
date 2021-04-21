from csv import DictReader
from json import loads, dumps

users = []

with open('data/users.json', 'r') as file:
    j = file.read()
    n = loads(j)
    for user in n:
        reader = {'name': user['name'], 'gender': user['gender'], 'address': user['address'], 'books': []}
        users.append(reader)

with open('data/books.csv') as f:
    reader = DictReader(f)
    for index, book in enumerate(reader):
        if len(users) <= index:
            break
        users[index]['books'].append({'title': book['Title'], 'author': book['Author'], 'height': book['Height']})

with open('data/new_json.json', 'w') as file:
    s = dumps(users, indent=4)
    file.write(s)
