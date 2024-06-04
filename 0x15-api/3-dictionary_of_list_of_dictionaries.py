#!/usr/bin/python3
"""To be updated - this is just a fake documentation for now"""
import json
import requests
import sys


if __name__ == "__main__":
    users_dict = {}
    for id in range(0, 10):
        u = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
        u = json.loads(u.text)
        u_tasks = requests.\
            get(f"https://jsonplaceholder.typicode.com/todos?userId={id}")
        u_tasks = json.loads(u_tasks.text)
        user_tasks = []
        for task in u_tasks:
            task["task"] = task["title"]
            del task["id"]
            del task["title"]
            del task["userId"]
            task.update({"username": u.get('username')})
            user_tasks.append(task)
        users_dict.update({id: user_tasks})
    with open("todo_all_employees.json", 'w', encoding="utf-8") as json_file:
        json_file.write(json.dumps(users_dict))
