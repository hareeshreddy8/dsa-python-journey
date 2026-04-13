def create_task(task):
    task_view = {"name":task,"status":False}
    return task_view
tasks = []
print("how many tasks do you need to add")
no_of_tasks = int(input())
for _ in range(no_of_tasks):
    task = str(input("Enter task name :"))
    tasks.append(create_task(task))

def display_tasks(tasks):
    for index,task in enumerate(tasks):
        if not task["status"]:
            print(f"{index}.{task['name']} [ ]")

        else :
            print(f"{index}.{task['name']} [✔]")
                  
    
                  
display_tasks(tasks)

    