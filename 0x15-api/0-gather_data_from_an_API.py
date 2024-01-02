#!/usr/bin/python3
"""
Module Docs
"""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = '{}users/{}'.format(base_url, employee_id)
    todos_url = '{}todos?userId={}'.format(base_url, employee_id)
    employee_template = "Employee {} is done with tasks"

    user_response = requests.get(user_url)
    employee_name = user_response.json().get('name')
    print(employee_template.format(employee_name), end="")

    todos_response = requests.get(todos_url)
    completed_tasks = [task for task in todos_response.json() if task.get('completed')]
    
    print("({}/{}):".format(len(completed_tasks), len(todos_response.json())))
    
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
