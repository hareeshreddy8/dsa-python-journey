#Creates task object with default status (not completed)
def create_task(task_name,priority,due_date):
    return {"name":task_name,"status":False,"priority":priority,"due_date":due_date}
    

#Mark task as done using its index
def mark_task_done(tasks,index):
    if not tasks:
        raise ValueError("No tasks available")
    if index >= len(tasks) or index < 0:
        raise IndexError(f"Invalid index.Please enter between {0} and {len(tasks)-1}")
    #update task with that index  
    tasks[index]["status"] = True


#Delete tasks using its index
def delete_task(tasks,index):
    if not tasks :
        raise ValueError("No tasks available. ")
    if index >= len(tasks) or index < 0 :
        raise IndexError(f"Invalid index.Please enter between {0} and {len(tasks)-1}")
    
    #update tasks by deleting using its index 
    tasks.pop(index)

#Edit name of existing task using index
def edit_task(tasks,index : int,new_name:str):
    if not tasks:
        raise ValueError("No tasks available.")
    if not 0 <= index < len(tasks) :
        raise IndexError(f"Invalid index.Please enter between {0} and {len(tasks) - 1}")
    tasks[index]["name"] = new_name

#Search tasks with task name 
def search_task(tasks,name):
    tasks_found = []
    for task in tasks:
        if name.lower() in task["name"].lower():
            tasks_found.append(task)
    return tasks_found


#filter task with priority 
def filter_tasks_by_priority(tasks,priority):
    filtered_tasks = []
    priority = priority.lower()
    for task in tasks:
        if task.get("priority") == priority.lower():
            filtered_tasks.append(task)

    return filtered_tasks

#sort tasks by duedate
def sort_tasks_by_due_date(tasks):
    return sorted(tasks,key = lambda x: x.get("due_date","9999-12-31"))

#sorting by priority
def sort_tasks_by_priority(tasks):
    priority_order = {"high" : 1,"medium": 2,"low":3}
    return sorted(tasks, key = lambda x : priority_order.get(x.get("priority").lower(),99))
