# CLI Productivity Tracker(phase 1 - In memory version)
#--------------------------------------------------------
#Features :
#1.Add task
#2.Display Task
#3.Marks tasks as completed 
#4.
#--------------------------------------------------------

import json
#Creates task object with default status (not completed)
def create_task(task):
    return {"name":task,"status":False}
    

#Mark task as done using its index
def mark_task_done(tasks,index):
    if not tasks:
        raise ValueError("No tasks available")
    if index >= len(tasks) or index < 0:
        raise IndexError(f"Invalid index.Please enter between {0} and {len(tasks)-1}")
    #update task with that index  
    tasks[index]["status"] = True

    

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
        except ValueError:
            print(f"Invalid input.Please enter a number.")
#load file contents into our memory
def load_tasks():
    try :
        with open("tasks.json","r") as file :
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []
    

#to save the contents in memory to file to not lose them
def save_tasks(tasks):
    with open("tasks.json","w") as file :
        json.dump(tasks,file)


           
#creating menu for users to decide what they want to do
tasks = load_tasks()
while True :
    print("===== MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    print("================")
    try :
        choice = int(input("Enter your choice: "))

    except:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        print("Enter task name: ")
        task = input()
        tasks.append(create_task(task))
        save_tasks(tasks)
        print("Task created successfully.")

    elif choice == 2:
        display_tasks(tasks)

    elif choice == 3:
        try:
            index = index_of_task_completed(tasks)
            mark_task_done(tasks,index)
            save_tasks(tasks)
            print("Task marked as completed. Updated tasks:")
            display_tasks(tasks)
        except (ValueError,IndexError) as e :
            print(e)
        

    elif choice == 4 :
        break

    else :
        print("Invalid choice. Please try again.")

        


    