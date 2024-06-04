#!/usr/bin/python3
"""To be updated - this is just a fake documentation for now"""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    user_response = requests.\
        get(f"https://jsonplaceholder.typicode.com/users/{id}")
    user = json.loads(user_response.text)
    user_tasks_response = requests.\
        get(f"https://jsonplaceholder.typicode.com/todos?userId={id}")
    user_tasks = json.loads(user_tasks_response.text)
    user_tasks_list = []
    for task in user_tasks:
        task["task"] = task["title"]
        del task["id"]
        del task["title"]
        del task["userId"]
        task.update({"username": user.get('username')})
        user_tasks_list.append(task)
    user_dict = {id: user_tasks_list}
    with open(f"{id}.json", 'w', encoding="utf-8") as json_file:
        json_file.write(json.dumps(user_dict))
