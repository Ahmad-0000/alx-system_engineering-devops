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
    with open(f"{id}.csv", "a", encoding="utf-8") as csv:
        for t in u_tasks:
            csv.write('"{}","{}","{}","{}"\n'.format(id, u.get('username'),
                                                        t.get('completed'),
                                                        t.get('title')))
