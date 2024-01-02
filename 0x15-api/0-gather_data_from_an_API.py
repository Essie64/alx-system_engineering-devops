#!/usr/bin/python3
"""
Script to gather data from a given REST API and display TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Extract employee ID from command line argument
    employee_id = sys.argv[1]

    # URL for the API endpoint
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = base_url + "users/{}".format(employee_id)
    todos_url = base_url + "todos?userId={}".format(employee_id)

    # Fetch user data
    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching user data:", e)
        sys.exit(1)

    # Fetch TODO list data
    try:
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching TODO list data:", e)
        sys.exit(1)

    # Extract relevant information
    employee_name = user_data.get("name")
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Display employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_number_of_tasks))

    # Display titles of completed tasks
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
