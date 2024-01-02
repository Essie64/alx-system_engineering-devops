#!/usr/bin/python3
"""
Script to gather data from a given REST API and display TODO list progress
"""

import requests
import sys


def fetch_user_data(employee_id):
    """Fetch user data from the API."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        return user_data
    except requests.exceptions.RequestException as e:
        print("Error fetching user data:", e)
        sys.exit(1)


def fetch_todo_data(employee_id):
    """Fetch TODO list data from the API."""
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    try:
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
        return todos_data
    except requests.exceptions.RequestException as e:
        print("Error fetching TODO list data:", e)
        sys.exit(1)


def display_todo_progress(employee_name, completed_tasks, total_tasks):
    """Display employee TODO list progress."""
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    # Extract employee ID from command line argument
    employee_id = sys.argv[1]

    # Fetch user data and TODO list data
    user_data = fetch_user_data(employee_id)
    todos_data = fetch_todo_data(employee_id)

    # Extract relevant information
    employee_name = user_data.get("name")
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)

    # Display employee TODO list progress
    display_todo_progress(employee_name, completed_tasks, total_tasks)
