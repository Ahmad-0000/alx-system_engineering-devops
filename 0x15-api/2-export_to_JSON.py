#!/usr/bin/python3
"""To be updated - this is just a fake documentation for now"""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
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
    user_dict = {id: user_tasks}
    with open(f"{id}.json", 'w', encoding="utf-8") as json_file:
        json_file.write(json.dumps(user_dict))
