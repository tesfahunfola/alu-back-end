#!/usr/bin/python3

"""
Python script to retrieve TODO list progress for a given employee ID.
"""

import requests
import sys


def get_employee_todo_list(employee_id):
    """
    Retrieves and displays the TODO list progress for a given employee ID.
    """

    # Making a GET request to the API endpoint
    response = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={'userId': employee_id}
    )

    # Checking if the request was successful
    if response.status_code != 200:
        print(f"Error: Failed to retrieve TODO list for employee {employee_id}")
        return

    todos = response.json()

    # Filter completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]

    # Displaying progress information
    employee_name = todos[0]['username']
    total_tasks = len(todos)
    completed_tasks_count = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks({completed_tasks_count}/{total_tasks}):"
    )

    # Displaying the titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list(employee_id)
