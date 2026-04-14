# CLI Productivity Tracker(phase 1 - In memory version)
# Features :
#  -- Add task
#   -- display Task


#Creates task object with incomplete status
def create_task(task):
    task_view = {"name":task,"status":False}
    return task_view
tasks = []
#ask user how many tasks they want to add
print("how many tasks do you need to add")
no_of_tasks = int(input())
#loop to take multiple task inputs from users
for _ in range(no_of_tasks):
    task = str(input("Enter task name :"))
    tasks.append(create_task(task))


#Display all tasks with index and completion status
def display_tasks(tasks):
    for index,task in enumerate(tasks):
        if not task["status"]:
            print(f"{index}.{task['name']} [ ]")

        else :
            print(f"{index}.{task['name']} [✔]")
                  
    
                  
display_tasks(tasks)

    