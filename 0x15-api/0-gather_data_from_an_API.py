#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    response = requests.get(url)
    if response.status_code != 200:
        print("Error retrieving TODO list: {}".format(response.text))
        sys.exit(1)

    tasks = response.json()

    total_tasks = len(tasks)
    done_tasks = sum(1 for task in tasks if task['completed'])
    employee_name = tasks[0]['userId']
    for task in tasks:
        if task['completed']:
            print("\t{}\t{}".format('\t', task['title']))

    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
