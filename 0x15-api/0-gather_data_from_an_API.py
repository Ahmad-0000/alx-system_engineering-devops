#!/usr/bin/python3
"""To be updated - this is just a fake documentation for now"""
import requests
import json
import sys

id = sys.argv[1]

if __name__ == "__main__":
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    user = json.loads(user.text)
    user_tasks = requests.\
        get(f"https://jsonplaceholder.typicode.com/todos?userId={id}")
    user_tasks = json.loads(user_tasks.text)
    complete = 0
    all = 0
    tasks = []
    for task in user_tasks:
        if task.get('completed'):
            complete += 1
            tasks.append(task.get('title'))
        all += 1
    print(f"Employee {user.get('name')} is done with tasks({complete}/{all}):")
    for task in tasks:
        print(f"\t {task}")
