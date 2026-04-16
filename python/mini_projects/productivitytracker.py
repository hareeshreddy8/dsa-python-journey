# CLI Productivity Tracker(phase 1 - In memory version)
#--------------------------------------------------------
#Features :
#1.Add task
#2.Display Task
#3.Marks tasks as completed 
#4.File persistent(using JSON)
#5.Delete task
#6.Edit task
#Fault tolerance(JSONDecodeError)
#--------------------------------------------------------

import json
FILE_NAME = "tasks.json"
#load file contents into our memory
def load_tasks():
    try :
        with open(FILE_NAME,"r") as file :
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("File corrupted. Resetting... ")
        tasks = []
        save_tasks(tasks)
        return tasks
    

#to save the contents in memory to file to not lose them
def save_tasks(tasks):
    with open(FILE_NAME,"w") as file :
        json.dump(tasks,file)


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
def index_of_task(tasks):
    while True:
        try:
            index = int(input("enter task number: "))
            if index >= len(tasks) or index < 0 :
                print(f"Invalid index,Please enter between {0} to {len(tasks) - 1}")
            
            else:
                return index
        except ValueError:
            print(f"Invalid input.Please enter a number.")


           
#creating menu for users to decide what they want to do
def main():
    tasks = load_tasks()
    while True :
        print("===== MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Edit Task Name")
        print("6. Exit")
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
            if not tasks :
                print("NO tasks available")
                continue
            try:
                index = index_of_task(tasks)
                mark_task_done(tasks,index)
                save_tasks(tasks)
                print("Task marked as completed. Updated tasks:")
                display_tasks(tasks)
            except (ValueError,IndexError) as e :
                print(e)
            

        elif choice == 4 :
            if not tasks :
                print("NO tasks available")
                continue
            try :
                index = index_of_task(tasks)
                delete_task(tasks,index)
                save_tasks(tasks)
                print("Task deleted successfully. Updated tasks: ")
                display_tasks(tasks)

            except (ValueError,IndexError) as e:
                print(e)
        elif choice == 5:
            if not tasks:
                print("No tasks available")
                continue
            try :
                index = index_of_task(tasks)
                while True :
                    new_name = str(input("Enter a new name to task: "))
                    if new_name.strip():
                        break
                    else :
                        print("Please enter valid name")
                edit_task(tasks,index,new_name)
                save_tasks(tasks)
                print("Task name updated successfully. Updated tasks")
                display_tasks(tasks)

            except ValueError:
                print("Please enter a valid name.")

        elif choice == 6:
            break

        else :
            print("Invalid choice. Please try again.")


#using __name__ check 

if __name__ == "__main__" :
    main()

    