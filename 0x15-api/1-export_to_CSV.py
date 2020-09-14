#!/usr/bin/python3
''' Export to CSV '''
from requests import get
import sys
import csv

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(base_url, sys.argv[1])
    res = get(user)
    json_user = res.json()
    username = json_user.get('username')

    todos = '{}todos?userId={}'.format(base_url, sys.argv[1])
    res = get(todos)
    json_tasks = res.json()
    done_tasks = []

    for todo in json_tasks:
        done_tasks.append(
            [userid, username, todo.get('completed'), todo.get('title')])

    csv_file = sys.argv[1] + '.csv'
    with open(csv_file, mode='w', encoding='utf-8') as file:
        writer = csv.write(employee_file, delimiter=',',
                           quotechar='"', quoting=csv.QUOTE_ALL)

        for todo in json_tasks:
            write.writerow(todo)
