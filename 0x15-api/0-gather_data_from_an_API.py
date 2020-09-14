#!/usr/bin/python3
''' Gather data from an API '''
from requests import get
import sys


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(base_url, sys.argv[1])
    res = get(user)
    json_user = res.json()
    print('Employee {} is done with tasks'.format(
        json_user.get('name')), end='')

    todos = '{}todos?userId={}'.format(base_url, sys.argv[1])
    res = get(todos)
    json_tasks = res.json()
    done_tasks = []

    for todo in json_tasks:
        if todo.get('completed') is True:
            done_tasks.append(todo)

    print('({}/{}):'.format(len(done_tasks), len(json_tasks)))
    for task in done_tasks:
        print('\t {}'.format(task.get('title')))
