#!/usr/bin/python3
''' Export to CSV '''
import csv
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
    done_tasks = []

    for todo in json_tasks:
        done_tasks.append(
            [sys.argv[1], username, todo.get('completed'), todo.get('title')])

    csv_file = sys.argv[1] + '.csv'
    with open(csv_file, mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for todo in json_tasks:
            writer.writerow(todo)
