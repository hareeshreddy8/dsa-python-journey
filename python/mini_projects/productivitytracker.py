# CLI Productivity Tracker(phase 1 - In memory version)
#--------------------------------------------------------
#Features :
#1.Add task
#2.Display Task
#3.Marks tasks as completed 
#--------------------------------------------------------


#Creates task object with default status (not completed)
def create_task(task):
    task_view = {"name":task,"status":False}
    return task_view


#Mark task as done using its index
def mark_task_done(tasks,index):
    if not tasks:
        print("No tasks available.")
        return
    if index >= len(tasks) or index < 0:
        print("invalid index,Please try again.")
        return 
    #update task with that index  
    tasks[index]["status"] = True
    print("Task marked as completed.")
    print("Current tasks:")
    display_tasks(tasks)

#Display all tasks with their index and completion status
def display_tasks(tasks):
    if not tasks:
        print("No tasks to display")
        return
    for index,task in enumerate(tasks):
        if not task["status"]:
            print(f"{index}. {task['name']} [ ]")

        else :
            print(f"{index}. {task['name']} [✔]")
                  
    
                  

#Get a valid task index from the user with proper validation
def index_of_task_completed(tasks):
    while True:
        try:
            index = int(input("enter task number to mark as done:"))
            if index >= len(tasks) or index < 0 :
                print(f"Invalid index,Please enter between {0} to {len(tasks) - 1}")
            else:
                return index
        except:
            print(f"Invalid input.Please enter a number.")

#creating menu for users to decide what they want to do
tasks = []
while True :
    print("===== MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    print("================")
    try :
        choice = int(input("Enter your choice:"))

    except:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        print("Enter task name:")
        task = input()
        tasks.append(create_task(task))
        print("Task created succesfully.")

    elif choice == 2:
        display_tasks(tasks)

    elif choice == 3:
        if not tasks :
            print("No tasks available.")
        else :
            index = index_of_task_completed(tasks)
            mark_task_done(tasks,index)
        

    elif choice == 4 :
        break

    else :
        print("Invalid choice. Please try again.")

        


    