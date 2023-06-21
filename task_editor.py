from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def edit_task(tasks, user):

    task_update_user = ""
    task_update_date = ""
    max_task = len(tasks)
    
    
    while True:
        try:
            selected_task = int(input("Would you like to edit a task? Enter the task number you'd like to edit or enter -1 to exit to the main menu: "))
            i = selected_task - 1
            break
        except ValueError:
            print("You have entered an incorrect value!")
        except IndexError:
            print("You have entered a task number that doesn't exist!")

    # close task list
    if selected_task == -1:
        print('Task list closed')
    
    # prevent completed tasks from being updated
    elif tasks[i]['completed'] == True:
        print('The task you have selected has been marked as completed and cannot be edited')

    elif selected_task != -1 and selected_task <= max_task:
        print(f"You have chosen to edit Task {selected_task} - {tasks[i]['title']}\n")
        mark_complete = input("Would you like to mark the task as complete?: y or n: ").lower()
        if mark_complete == 'y':
            tasks[i].update({'completed': True}) # change last item in list from "No" to "Yes"
            print(f"Task number {selected_task} has been marked as complete")
        elif mark_complete == 'n':
            while True:
                    task_update_user = input("Which user should this task be assigned to?: ")
                    if task_update_user not in user.keys(): # prevent task from being updated with user that does not exist in user list
                        print("User does not exist")
                        continue
                    else:
                        break

            while True:
                    try:
                        task_due_date = input("When is this task now due? (YYYY-MM-DD): ")
                        task_update_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                        break
                    except ValueError:
                            print("Invalid datetime format. Please use the format specified")

            tasks[i]['username'] = task_update_user
            tasks[i]['due_date'] = task_update_date
            
            print(f'''-----------------------------------
Task number {selected_task} has been updated:
                
The assigned user is now {task_update_user}
The due date for the task is now {task_update_date}

-----------------------------------
''')

        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in tasks:
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

    elif selected_task > max_task:
        print("The task number you have entered does not exist!")

    else:
        print('You have made an incorrect choice, please enter either y or n to continue:')
