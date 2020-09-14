#!/usr/bin/python3
''' Export to JSON '''
import json
import requests
import sys

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(base_url, sys.argv[1])
    res = requests.get(user)
    json_user = res.json()
    username = json_user.get('username')

    todos = '{}todos?userId={}'.format(base_url, sys.argv[1])
    res = requests.get(todos)
    json_tasks = res.json()
    tasks = []

    for todo in json_tasks:
        to_json = {'task': todo.get(
            'title'), 'completed': todo.get('completed'), 'username': username}
        tasks.append(to_json)

    user_json = {str(sys.argv[1]): tasks}
    json_file = sys.argv[1] + '.json'

    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(user_json, file)
