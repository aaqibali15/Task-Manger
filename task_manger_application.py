tasks = {}

def display_function():
    print("1.Add new Task.")
    print("2.View All tasks.")
    print("3.Edit tasks.")
    print("4.Delete Task.")
    print("5.Exit.")

#########  user prompt
def user_input(prompt):
    return input(prompt)

##########  
def add_task(task_des, status):
    tasks[task_des] = status
    return tasks

###########  add task feature
def add_task_feature():
    task_des = user_input("Enter the task description:")
    status = user_input("Enter the status is completed or pending:")
    add_task(task_des,status)
    print(tasks)

####### View all tasks
def view_all_tasks():
    for key,value in tasks.items():
        print(f"The task is '{key}' and status is '{value}'.")

###########  edit existing task
def edit_existing_task(task_des,status):
    tasks[task_des] = status
    return tasks

#########  edit existing task features
def edit_existing_task_feature():
    task_des = user_input("Enter the task name you update:")
    status = user_input("Enter the new status:")
    tasks = edit_existing_task(task_des,status)
    print(f"Upadated Tasks: {tasks}")

#########  delete tasks 
def delete_tasks(task_des):
    if task_des in tasks:
        del tasks[task_des]
    else:
        print("Task not found.")
    return tasks
########  delete task feature
def delete_task_feature():
    task_des = user_input("Enter the task you want to delete:")
    tasks = delete_tasks(task_des)
    print(tasks)
######## Main function
while True:
    try:
        display_function()
        choice = int(input("Enter the your choice:"))
        if choice == 1:
            add_task_feature()
        elif choice == 2:
            view_all_tasks()
        elif choice == 3:
            edit_existing_task_feature()
        elif choice == 4:
            delete_task_feature()
        elif choice == 5:
            break
        else:
            print("Invalid Input.")
    except:
        print("Enter Valid choice.")
