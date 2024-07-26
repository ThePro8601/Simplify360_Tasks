from collections import defaultdict, deque

tasks = {
    'T_START': {'duration': 0, 'dependencies': []},
    'task1': {'duration': 4, 'dependencies': ['T_START']},
    'task2': {'duration': 3, 'dependencies': ['task1']},
    'task3': {'duration': 2, 'dependencies': ['task1']},
    'task4': {'duration': 1, 'dependencies': ['task2', 'task3']}
}

def topological_sort(tasks):
    in_degree = {task: 0 for task in tasks}
    
    zero_in_degree_queue = deque([task for task in tasks if in_degree[task] == 0])
    top_order = []

    while zero_in_degree_queue:
        current = zero_in_degree_queue.popleft()
        top_order.append(current)

        for neighbor in tasks:
            if current in tasks[neighbor]['dependencies']:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree_queue.append(neighbor)

    if len(top_order) != len(tasks):
        raise ValueError("There exists a cycle in the graph")

    return top_order

def calculate_earliest_times(tasks, top_order):
    est = {task: 0 for task in tasks}
    eft = {task: 0 for task in tasks}
    
    for task in top_order:
        task_duration = tasks[task]['duration']
        eft[task] = est[task] + task_duration
        for dependent in tasks:
            if task in tasks[dependent]['dependencies']:
                est[dependent] = max(est[dependent], eft[task])
    
    return est, eft

def calculate_latest_times(tasks, top_order, project_completion_time):
    lft = {task: project_completion_time for task in tasks}
    lst = {task: float('inf') for task in tasks}
    
    for task in reversed(top_order):
        task_duration = tasks[task]['duration']
        lst[task] = lft[task] - task_duration
        for dep in tasks[task]['dependencies']:
            lft[dep] = min(lft[dep], lst[task])
    
    return lst, lft

def find_project_completion_times(tasks):
    top_order = topological_sort(tasks)
    est, eft = calculate_earliest_times(tasks, top_order)
    earliest_completion_time = max(eft.values())
    
    lst, lft = calculate_latest_times(tasks, top_order, earliest_completion_time)
    latest_completion_time = max(lft.values())
    
    return earliest_completion_time, latest_completion_time

try:
    earliest_completion_time, latest_completion_time = find_project_completion_times(tasks)
    print(f"Earliest time all tasks will be completed: {earliest_completion_time}")
    print(f"Latest time all tasks will be completed: {latest_completion_time}")
except ValueError as e:
    print(e)

# Space and Time Complexity Analysis

# Time: O(V + E), Space: O(V + E)
