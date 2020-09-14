#!/usr/bin/python3
''' Export to JSON for all users'''
import json
import requests
import sys


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users'.format(base_url)
    res = requests.get(user)
    json_user = res.json()

    all_tasks = {}
    for user in json_user:
        username = user.get('username')
        userid = user.get('id')

        todos = '{}todos?userId={}'.format(base_url, userid)
        res = requests.get(todos)
        json_tasks = res.json()
        tasks = []

        for todo in json_tasks:
            to_json = {'username': username,
                       'task': todo.get('title'),
                       'completed': todo.get('completed')}
            tasks.append(to_json)

        all_tasks[str(userid)] = tasks

    json_file = 'todo_all_employees.json'
    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(all_tasks, file)
