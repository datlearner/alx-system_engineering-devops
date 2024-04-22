#!/usr/bin/python3
"""Script that uses JSONPlaceholder API to get information about an employee."""
import requests
import sys


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user_url = f'{base_url}users/{user_id}'
    user_res = requests.get(user_url)
    user_data = user_res.json()
    print(f"Employee {user_data.get('name')} is done with tasks", end="")
    todos_url = f'{base_url}todos?userId={user_id}'
    tasks = todos_res.json()
    completed_tasks = [task for task in tasks if task.get('completed')]
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
