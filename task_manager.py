import os

# Import modules
import add_user
import new_task
import view_all_tasks
import view_my_tasks
import task_editor
import stats
import task_report
import user_report

from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['task_number'] = task_components[0]
    curr_t['username'] = task_components[1]
    curr_t['title'] = task_components[2]
    curr_t['description'] = task_components[3]
    curr_t['due_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[6] == "Yes" else False

    task_list.append(curr_t)

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View tasks assigned to me
ds - Display statistics
gr - Generate reports
e - Exit
: ''').lower()

    if menu == 'r':
        add_user.reg_user(username_password)
        
    elif menu == 'a':
        new_task.add_task(task_list, username_password)
    
    elif menu == 'va':
        if len(task_list) == 0:
            print("There are currently no tasks!")
            print("Returning to main menu...")
        else:
            view_all_tasks.view_all(task_list)
    
    elif menu == 'vm':
        user_tasks_total = view_my_tasks.view_mine(task_list, curr_user)
    
        if user_tasks_total == 0:
            print("You currently have no tasks assigned!")
        else:
            task_editor.edit_task(task_list, username_password)
    
    elif menu == 'ds' and curr_user == 'admin': 
        stats.display_stats()
    
    elif menu == 'ds' and curr_user != 'admin':
        print("You do not have the necessary privileges to use this option, please select another option")
    
    elif menu == 'gr':
        task_report.task_overview(task_list)
        user_report.user_overview(task_list, username, username_password)
    
    elif menu == 'e':
        print('Goodbye, enjoy the rest of your day!')
        exit()

    else:
        print("You have entered an incorrect command, please try again")