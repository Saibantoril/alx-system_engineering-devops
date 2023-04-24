#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees and exporting data in CSV format"""

import requests
import sys
import csv


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    # Export tasks to CSV
    with open(f"{employeeId}.csv", mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in tasks:
            writer.writerow([employeeId, employeeName, task['completed'], task['title']])
            
    done_tasks = [task for task in tasks if task['completed']]
    print(f"Employee {employeeName} is done with tasks ({len(done_tasks)}/{len(tasks)}):")
    for task in done_tasks:
        print(f"\t{task['title']}")
