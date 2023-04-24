#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees and exporting data in JSON format"""

import json
import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    # Export tasks to JSON
    tasks_json = {}
    tasks_json[employeeId] = []

    for task in tasks:
        tasks_json[employeeId].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': employeeName
        })
    with open(f"{employeeId}.json", 'w') as json_file:
        json.dump(tasks_json, json_file)

    done_tasks = [task for task in tasks if task['completed']]
    print(f"Employee {employeeName} is done with tasks ({len(done_tasks)}/{len(tasks)}):")
    for task in done_tasks:
        print(f"\t{task['title']}")
