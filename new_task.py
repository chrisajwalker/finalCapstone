from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def add_task(task, user):
    task_number = 1

    with open('tasks.txt', 'r') as f:
        for line in enumerate(f): # count lines and assigned numerical value
            task_number += 1

    task_username = input("Name of person assigned to task: ")
    
    # check selected user is registered in user list
    while True:
        if task_username not in user.keys():
            print("User does not exist. Please enter a valid username")
            task_username = input("Name of person assigned to task: ")
        else:
            break
    
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    
    # request new completion date and format input
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "task_number": str(task_number),
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
        }
    task.append(new_task)
    
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task:
            str_attrs = [
                t['task_number'],
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    
    print("Task successfully added.")
