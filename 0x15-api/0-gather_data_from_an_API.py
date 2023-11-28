#!/usr/bin/python3
"""
Python script to gather data from a REST API for a given employee ID.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
    else:
        employee_id = int(argv[1])

        # Fetching user data
        user_response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
        )
        user_data = user_response.json()

        # Fetching TODO list for the user
        todo_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
        )
        todo_data = todo_response.json()

        # Calculating completed and total tasks
        total_tasks = len(todo_data)
        completed_tasks = sum(task['completed'] for task in todo_data)

        # Displaying the information
        print("Employee {} is done with tasks({}/{}):".format(
            user_data['name'], completed_tasks, total_tasks
        ))

        # Displaying the titles of completed tasks
        for task in todo_data:
            if task['completed']:
                print("\t{}".format(task['title']))
