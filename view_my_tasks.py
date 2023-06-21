from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def view_mine(tasks, user):
    print("--------------------------------------------------------------------------------------------------------------")
    user_total_tasks = 0
    for t in tasks:
        
        # create string to display Ture or False status as yes or no for readability
        if t['completed'] == True:
            completed_status = 'Yes'
        else:
            completed_status = 'No'
        

        # display task data as string is username for task matches the current user
        if t['username'] == user:
            disp_str = f"Task Number: \t\t\t {t['task_number']}\n"
            disp_str += f"Task: \t\t\t\t {t['title']}\n"
            disp_str += f"Task Description: \t\t {t['description']}\n"
            disp_str += f"Assigned to: \t\t\t {t['username']}\n"
            disp_str += f"Date Assigned: \t\t\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t\t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Completed: \t\t {completed_status}\n"
            disp_str += "--------------------------------------------------------------------------------------------------------------"
            user_total_tasks += 1
        
            print(disp_str)
        
    return user_total_tasks