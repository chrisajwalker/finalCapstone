import percent

from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def task_overview(tasks):
    time_generated = str(datetime.now())
    time_generated = time_generated[:19:]

    total_tasks = len(tasks)
    
    completed_total = 0
    incomplete_total = 0


    # update totals for completed and incomplete tasks
    for t in tasks:
        if t['completed'] == True:
            completed_total += 1
        else:
            incomplete_total += 1
    
    # update overdue total if task is not marked as complete and today's date is greater than the task due date
    overdue_total = 0
    for t in tasks:
        due_date = str(t["due_date"])
        due_date = due_date[:10:]
        today_date = str(date.today())
        if t['completed'] != True and due_date < today_date:
            overdue_total += 1
    
    # use percent module to calculate percentages
    uncompleted_percent = percent.percentage_of(incomplete_total, total_tasks)
    overdue_percent = percent.percentage_of(overdue_total, total_tasks)
    task_report = f'''Task Overview for all users

Report generated: {time_generated}

-------------------------------------------------------    

Total number of tasks: \t\t\t\t\t\t {total_tasks}

Number of completed tasks: \t\t\t\t\t {completed_total}
Number of incomplete tasks: \t\t\t\t {incomplete_total}
Number of overdue tasks: \t\t\t\t\t {overdue_total}

Percentage of incomplete tasks: \t\t\t {uncompleted_percent}%
Percentage of tasks overdue: \t\t\t\t {overdue_percent}%

-------------------------------------------------------'''
    
    with open("task_overview.txt", 'w') as f:
        f.write(task_report)