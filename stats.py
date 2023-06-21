import os

def display_stats():

# create tasks.txt and user.txt if not present in directory
    if not os.path.exists("task_overview.txt"):
        with open("task_overview.txt", "w") as default_file:
            pass
        print("New blank task overview file created - please run Generate Reports from the main menu and then run Display Statistics again to see the most accurate data")

    if not os.path.exists("user_overview.txt"):
        with open("user_overview.txt", "w") as default_file:
            pass
        print("New blank user overview file created - please run Generate Reports from the main menu and then run Display Statistics again to see the most accurate data")
    
    with open("task_overview.txt", 'r') as f:
        task_overview = f.read().splitlines()
    
    for line in task_overview:          
        if "\t" in line:
            line_to_print = line.replace("\t", "")
        else:
            line_to_print = line
        print(line_to_print)

    with open("user_overview.txt", 'r') as f:
        user_overview = f.read().splitlines()[9:]

    for line in user_overview:
        if "\t" in line:
            line_to_print = line.replace("\t", "")
        else:
            line_to_print = line
        print(line_to_print)