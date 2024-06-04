#!/usr/bin/python3
"""To be updated - this is just a fake documentation for now"""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    user = json.loads(user.text)
    user_tasks = requests.\
        get(f"https://jsonplaceholder.typicode.com/todos?userId={id}")
    user_tasks = json.loads(user_tasks.text)
    username = user.get('username')
    with open(f"{id}.csv", "a", encoding="utf-8") as csv_file:
        for task in user_tasks:
            status = task.get('completed')
            title = task.get('title')
            line = '"{}","{}","{}","{}"\n'.format(id, username, status, title)
            csv_file.write(line)
